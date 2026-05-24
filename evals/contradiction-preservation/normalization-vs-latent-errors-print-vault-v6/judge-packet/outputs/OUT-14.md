---
anonymous_label: OUT-14
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
output_sha256: 52be2655337f2a3855189090a5bbac2f7441ee92f79c09e688c56d6a69762edf
condition_blinded: true
note: Condition-blinded model output for blind judging. The generating condition, run number, and seed are withheld by design.
---

# Output OUT-14

**Recommendation: Decline the surge until after the rainy season.**

### Reasoning
The available evidence suggests that Vault 3 is currently experiencing "normalization of deviance." The facilities manager is relying on **lagging indicators** (one-hour averages and "green tiles") to claim stability, while the paper conservator is pointing to **leading indicators** (raw ten-minute peaks and physical material reactions).

In archival preservation, the *average* humidity is less important than the *amplitude and frequency of fluctuations*. The "faint rippling on packing tissue" is the most critical piece of evidence; tissue is highly hygroscopic and acts as a canary in the coal mine. If the tissue is rippling, the prints are likely experiencing mechanical stress, regardless of what the dashboard says.

Furthermore, the technical infrastructure is currently unverified:
1.  **The Pump:** A dry bench test proves the motor turns; it does not prove the pump can move water under load. If the pump fails during a high-traffic surge in the rainy season, the dehumidifier will shut down, potentially leading to a catastrophic RH spike.
2.  **The Air Curtain:** The pressure sensor flipping direction during door opens indicates that the vestibule is not effectively buffering the vault from external air.
3.  **The Data:** The fact that the one-hour average looks "smoother" while ten-minute peaks are "sharper" suggests that the new actuator may be oscillating or that the BMS is simply filtering out the volatility.

Increasing cart entries by 35% will increase the frequency of door opens and the amount of moisture introduced by personnel. Doing this during the rainy season, with an untested pump and a failing air buffer, creates an unacceptable risk of irreversible damage to nineteenth-century prints.

### The Strongest Reason Against This Recommendation
The primary tradeoff is the **immediate institutional cost**. Declining the surge will trigger cancellation fees and result in the loss of public-program revenue. More importantly, it may signal to the partner museum that Marrow House is unreliable or incapable of managing high-level loans, potentially damaging a long-term strategic partnership.

### Observable Evidence That Would Change My Mind
I would reverse this recommendation only if the following three conditions were met during the six-hour overnight window:
1.  **Successful Wet-Load Test:** The condensate pump must successfully evacuate a full volume of water without triggering a float alarm.
2.  **Raw Data Alignment:** A side-by-side comparison of the ten-minute raw readings and a handheld hygrometer must show that the "sharper peaks" are remaining within a safe absolute range (e.g., $\pm 5\%$ RH), rather than just returning to the average.
3.  **Pressure Stabilization:** The pressure sensor must remain stable during a simulated "door open" event, proving the air curtain is functioning.

If you cannot verify these three physical realities, the "green tile" on the dashboard is a cosmetic convenience, not a safety guarantee.
