* Centralize FlowTrigger and FlowMethodDecorator so start/listen/router and the boolean trigger helpers share one contract.
* Update the flow guide to use or_(...) / and_(...)

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Touches flow trigger parsing and runtime condition evaluation; changes are mostly typing and sequence validation, but incorrect tuple/string handling could affect listener routing edge cases.
>
> **Overview**
> Introduces shared **`FlowTrigger`** and **`FlowMethodDecorator`** types in `dsl/_types.py` and wires them through **`@start`**, **`@listen`**, **`@router`**, **`or_()`**, and **`and_()`** so trigger arguments and decorator return types use one contract instead of ad hoc `Callable` unions.
>
> **Condition handling** is tightened: **`is_flow_condition_dict`** and normalization accept non-string sequences (e.g. tuples) via **`_is_non_string_sequence`**, and **`FlowCondition`** / runtime **`_evaluate_condition`** allow plain **`str`** route labels alongside method names. Docs show multi-trigger **`@listen(or_(...))`** instead of variadic string args.
>
> Minor cleanup: drops a **`type: ignore`** on **`RecallFlow.re_decide_depth`**, plus a unit test for tuple-based condition dicts.
>
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 988d1e8cfd069d83ec835ee730495578cafda317. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Standardized Flow decorator API enabling clearer multi-event trigger syntax for defining flow handlers.

* **Documentation**
  * Updated guides and examples to show the new multi-event trigger syntax and usage.

* **Bug Fixes**
  * Minor fix to recall flow decision path to ensure consistent post-search behavior.

* **Tests**
  * Added tests validating acceptance of non-string sequence conditions in flow definitions.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
