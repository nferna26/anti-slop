## Summary

`transform_schema()` drops a top-level `$defs` when the schema root is a `$ref`, leaving a dangling reference that the API rejects.

The early return at the top of `transform_schema` copies `$ref` and discards every sibling key — including `$defs` — before the `$defs` handling below it can run:

```python
ref = json_schema.pop("$ref", None)
if ref is not None:
    strict_schema["$ref"] = ref
    return strict_schema
```

That's fine for the recursive case (a nested property that is just `{"$ref": ...}`), but wrong at the root: `$ref` with a sibling `$defs` is valid JSON Schema (draft 2019-09+), and it's exactly what Pydantic v2 emits for `RootModel` types:

```python
TypeAdapter(RootModel[Tier]).json_schema()
# {"$ref": "#/$defs/Tier", "$defs": {"Tier": {...}}}
```

Any `RootModel` output type fed through the strict-mode bindings hits this. Reported by a user; verified present from at least v0.84.0 through v0.105.2.

## Repro

```python
from anthropic.lib._parse._transform import transform_schema

schema = {
    "$ref": "#/$defs/Tier",
    "$defs": {"Tier": {"type": "string", "enum": ["free", "pro", "enterprise"], "title": "Tier"}},
}
transform_schema(schema)
# before: {"$ref": "#/$defs/Tier"}            <- $defs dropped, dangling ref
# after:  {"$defs": {"Tier": {...}}, "$ref": "#/$defs/Tier"}
```

## Fix

Process `$defs` before the `$ref` early return. Bare-`$ref` schemas (no siblings) are unchanged — `$defs` is only emitted when present in the input.

Not addressed here: other root-`$ref` siblings (e.g. `title`) are still dropped by the early return. `$defs` is the one that makes the schema invalid; the rest are cosmetic.

## Tests

- Added `test_ref_schema_with_defs` covering the `RootModel` shape (root `$ref` + sibling `$defs`); the existing `test_ref_schema` covers the bare-`$ref` case.
- `tests/lib/_parse/test_transform.py`: 14/14 pass.
