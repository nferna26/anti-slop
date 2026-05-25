---
artifact: judge-packet-case-context
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
condition_blinded: true
---

# Case Context

This is the condition-neutral context for judging anonymised OUT-NN answers. It
carries the scenario, the question the answers respond to, what a good answer
must do, and the failure modes to watch for. It names no answer origin; every
OUT-NN answers the same question, and how each was produced is withheld.

## Scenario

Synthetic and invented - no real museum, artwork, lender, person, vendor, or
incident.

Marrow House Museum stores unframed nineteenth-century prints in Vault 3. The
vault is kept dry through a building-management system, a vestibule air curtain,
and a compact dehumidifier serving one corner stack. Over the last ten months,
the system has logged twenty-one short "RH slope" notices. Each notice meant the
relative-humidity trend rose faster than expected for part of an hour, then
returned inside the allowed band. No visible mold, foxing, or paper loss has
been reported, and every weekly gallery-facing condition summary says Vault 3 is
"within range."

The handling team has made several process improvements. After the fifth notice,
staff added a move log for every cart entering Vault 3. After the ninth, the
registrar required a second person to initial each exception note. After the
fourteenth, a dashboard began showing a green tile whenever the one-hour average
stayed inside the allowed band by the next morning. The facilities manager says
these layers show the vault is ready for a six-week print-loan surge from a
partner museum.

The paper conservator is less certain. The phrase "normalized by morning trend"
appears in thirteen of the last fifteen exception notes. Six notes have no
attached handheld hygrometer reading even though the procedure asks for one.
Three cart logs show the vestibule door was held open for less than two minutes,
yet the nearby pressure sensor briefly flipped direction during the same window.
Two unrelated work orders mention faint rippling on packing tissue near the
north stack after rainy delivery days; both were closed as handling marks. The
dehumidifier's condensate pump passed a dry bench test after a float alarm, but
no wet-load test is attached. A vendor also replaced a damper actuator in March;
since then, the dashboard's one-hour average has looked smoother, while the
ten-minute raw readings show slightly sharper peaks during moves.

Marrow House must decide in nine days whether to accept the partner museum's
surge. Accepting it would increase Vault 3 cart entries by about 35 percent for
six weeks and would avoid cancellation fees and public-program losses. Declining
would protect the loan schedule but damage the partnership. There is one
six-hour overnight access window before the decision. It is enough for only one
package:

- Turn on a new dashboard rule that suppresses repeated RH-slope notices after
  the one-hour average returns to range, sends one daily digest to the registrar,
  and requires a second initial on any remaining red tile.
- Open the north-stack air path, wet-load test the condensate pump, check the
  damper actuator against ten-minute raw readings, and audit the twenty-one
  notices against cart logs, handheld readings, weather, and packing-tissue
  notes.
- Decline the surge until after the rainy season and revisit the partnership
  later.

The case is built so the evidence does not settle itself. The clean condition
record, weekly range summaries, short door holds, and business cost of declining
are real counterevidence. So are the repeated closure phrase, missing handheld
readings, pressure flips, tissue notes, dry-only pump test, actuator change, and
raw-versus-smoothed reading mismatch.

## The question the answers respond to

Every OUT-NN answer responds to this question:

> I oversee collections operations at Marrow House Museum. Vault 3 stores
> unframed nineteenth-century prints. It is kept dry through a
> building-management system, a vestibule air curtain, and a compact
> dehumidifier serving one corner stack. Over the last ten months, the system
> has logged twenty-one short "RH slope" notices. Each notice meant the
> relative-humidity trend rose faster than expected for part of an hour, then
> returned inside the allowed band. No visible mold, foxing, or paper loss has
> been reported, and every weekly condition summary says Vault 3 is "within
> range."
>
> We added a move log for every cart entering Vault 3 after the fifth notice, a
> second-person initial on each exception note after the ninth, and a dashboard
> green tile after the fourteenth whenever the one-hour average stayed inside
> the allowed band by the next morning. The facilities manager says these layers
> show the vault is ready for a six-week print-loan surge from a partner museum.
>
> The paper conservator is less certain. The phrase "normalized by morning
> trend" appears in thirteen of the last fifteen exception notes. Six notes have
> no attached handheld hygrometer reading even though the procedure asks for
> one. Three cart logs show the vestibule door was held open for less than two
> minutes, yet the nearby pressure sensor briefly flipped direction during the
> same window. Two unrelated work orders mention faint rippling on packing
> tissue near the north stack after rainy delivery days; both were closed as
> handling marks. The dehumidifier's condensate pump passed a dry bench test
> after a float alarm, but no wet-load test is attached. A vendor replaced a
> damper actuator in March; since then, the dashboard's one-hour average has
> looked smoother, while the ten-minute raw readings show slightly sharper peaks
> during moves.
>
> We must decide in nine days whether to accept the partner museum's surge.
> Accepting it would increase Vault 3 cart entries by about 35 percent for six
> weeks and would avoid cancellation fees and public-program losses. Declining
> would protect the loan schedule but damage the partnership. We have one
> six-hour overnight access window before the decision, enough for only one
> package: turn on a new dashboard rule that suppresses repeated RH-slope
> notices after the one-hour average returns to range, sends one daily digest to
> the registrar, and requires a second initial on any remaining red tile; open
> the north-stack air path, wet-load test the condensate pump, check the damper
> actuator against ten-minute raw readings, and audit the twenty-one notices; or
> decline the surge until after the rainy season.
>
> What should I recommend, and why? Give one concrete recommendation, the
> strongest reason against it, and the observable evidence that would change
> your mind. Avoid generic "do both" advice unless you explain what is actually
> sacrificed.

## What a good answer must do

A strong answer must:

1. Infer that the case is not just a storage-quality problem, a dashboard
   problem, or a relationship-cost problem. It has two live explanations: the
   exception process may be making short humidity notices easier to close as
   normal, and the air-handling / moisture-defence stack may contain a dormant
   weakness that emerges during rainy cart movement.
2. Use scenario facts in a discriminating way, including facts that cut against
   the recommendation. A passing answer cannot win by reciting the list.
3. Preserve the acceptance-threshold concern without relying on a label. It
   should infer this from traces such as repeated "normalized by morning trend"
   notes, missing handheld readings, second initials becoming part of closure,
   and dashboard smoothing making exceptions look calmer.
4. Preserve the dormant-defect / defence concern without treating all monitoring
   as useless. It should name a concrete path involving air-pressure reversal,
   north-stack moisture, condensate pump wet-load behavior, damper actuator
   timing, raw ten-minute peaks, or delivery-day moisture.
5. Weigh the intervention boundary. The new dashboard rule may reduce red-tile
   noise and improve escalation discipline, but it can also suppress the very
   repeated notices and raw peaks needed to test the pattern. The air-path /
   wet-load / audit package may learn whether the pattern is real and repairable,
   but it leaves no new digest/escalation layer before the surge. Declining the
   surge avoids added exposure but may preserve ignorance about Vault 3.
6. Make one recommendation under the nine-day / six-hour constraint, name a
   concrete failure path for that recommendation, and state observable evidence
   that would change the answer.

## Failure modes to watch for

- **Dashboard smoothing shortcut.** Turns on the new dashboard rule because
  fewer red tiles and second initials sound like better control, without facing
  that repeated notices and raw peaks may be the evidence to preserve.
- **Clean-range shortcut.** Treats no visible damage and weekly "within range"
  summaries as proof that Vault 3 is safe for the surge.
- **Audit-only flattening.** Chooses the air-path / wet-load / audit package as
  root-cause work while ignoring that it leaves no new digest or escalation
  layer before a six-week entry surge.
- **Decline-only flattening.** Declines the surge without explaining what the
  museum still needs to learn about Vault 3.
- **Label default.** Names normalization of deviance, latent errors, Swiss
  cheese, defence-in-depth, or a famous source as the answer rather than using
  the scenario facts.
- **Free hybrid.** Recommends activating the dashboard rule, opening the air
  path, wet-load testing, auditing all notices, and deciding later without
  naming what the six-hour window cannot do.

Score against rubric.md, criterion by criterion. The dependency rule in
rubric.md is mandatory.
