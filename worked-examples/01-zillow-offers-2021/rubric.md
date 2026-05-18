status: operator-review-draft
source_ref: src-zillow-offers-shutdown-2021
primary_source: Zillow Group Q3 2021 shareholder letter + Form 8-K (Nov 2 2021) + 2021 Form 10-K
supporting_primary_source: Zillow Group Q3 2021 earnings call transcript + Rich Barton public Q3-announcement statements
scoring_mode: binary
do_not_publish_until: operator validates against sources

This rubric scores whether a model output materially understands the November 2021 Zillow Offers shutdown as Zillow itself described it. It does not score prose quality, confidence, or rhetorical polish.

Each item is pass/fail. Default: no partial credit. Record near misses in reviewer notes, not in the binary score.

---

## RUBRIC-Z1

**Binary check:** Does the answer separate the operating-capacity and capital-allocation story from the shallow algorithm-failure story?

**Why it matters:** This is the load-bearing check. The methodology should recover Zillow's stated causal stack, not repeat the popular shorthand.

**Pass criteria:** The answer names forecast volatility, labor/supply-chain or renovation capacity, inventory exposure, and balance-sheet or equity-capital volatility as linked causes. It may mention pricing models, but only as one layer in the operating system.

**Fail criteria:** The answer says, or strongly implies, that the shutdown happened simply because the algorithm, AI, Zestimate, or automated valuation model failed. It also fails if it omits the operating-capacity and capital-allocation layers.

**Source anchor:** The Form 8-K ties the Board's decision to home-pricing unpredictability, capacity constraints, and operational challenges; the Q3 shareholder letter ties further scaling to equity capital, earnings and balance-sheet volatility, and return on equity.

---

## RUBRIC-Z2

**Binary check:** Does the answer name labor, supply-chain, renovation, and resale capacity constraints as Zillow named them?

**Why it matters:** The wind-down was not only a pricing event. The operating pipeline could not process homes at the pace the acquisition engine produced.

**Pass criteria:** The answer says Zillow faced renovation and resale capacity constraints, a difficult labor and supply-chain environment, and/or third-party contractor/vendor execution risk. It connects those constraints to delayed closings, longer holding times, or reduced returns.

**Fail criteria:** The answer mentions only home-price forecasting, algorithmic pricing, or a housing-market swing, with no operating-throughput layer.

**Source anchor:** The Q3 shareholder letter says Homes revenue missed outlook because renovation and resale capacity constraints shifted closings into Q4; the 10-K says Zillow Offers depended on contractors and vendors for renovation and repair, and longer renovation periods could harm timing, resale value, and returns.

---

## RUBRIC-Z3

**Binary check:** Does the answer treat inventory turn and capital exposure as structural constraints, not just metrics?

**Why it matters:** The methodology should see inventory as the bridge from forecast error to balance-sheet risk.

**Pass criteria:** The answer describes Zillow buying homes faster than it sold or processed them, or explains that delayed turns increased holding costs, price exposure, financing exposure, or return-on-equity pressure.

**Fail criteria:** The answer lists the $304 million write-down but does not explain inventory velocity, homes under contract, or why holding homes changed the risk profile.

**Source anchor:** The Q3 shareholder letter reports 9,680 homes purchased, 3,032 homes sold, 9,790 homes in inventory, and 8,172 homes under contract at Q3 end; the 2021 10-K says sales below forecast could create oversupply, downward price pressure, lower profitability, and increased average days to sale.

---

## RUBRIC-Z4

**Binary check:** Does the answer capture Zillow's wind-down decision criteria, not just the fact of shutdown?

**Why it matters:** A postmortem should identify the decision rule. Zillow's decision was about whether the business could be stable, scalable, capital-efficient, and aligned with the wider company.

**Pass criteria:** The answer says Zillow judged further scaling too volatile, too capital-intensive, too low-return, or not stable enough for the company's goals. It should connect the decision to earnings volatility, balance-sheet volatility, return on equity, and customer reach.

**Fail criteria:** The answer says only that Zillow shut down Zillow Offers after a write-down. It fails if it treats the write-down as the sole decision criterion.

**Source anchor:** The 10-K says the stated factors led Zillow to conclude Zillow Offers was unlikely to be a stable enough line of business for Zillow's goals and needs; the Q3 letter says scale would require too much equity capital and create too much volatility.

---

## RUBRIC-Z5

**Binary check:** Does the answer avoid unsupported claims about AI, Zestimate, or a broken pricing algorithm?

**Why it matters:** The popular narrative can smuggle in claims Zillow did not make in the cited sources. This is the second load-bearing check after Z1.

**Pass criteria:** The answer may say pricing forecasts were volatile or inaccurate relative to Zillow's modeled expectations. If it discusses algorithms, it states that Zillow's 10-K described algorithms as one input among in-person evaluations, market data, update costs, holding costs, and resale assumptions.

**Fail criteria:** The answer says the Zestimate failed, the AI could not price homes, the algorithm caused the shutdown, or executives blindly trusted a model, without a Zillow-source anchor.

**Source anchor:** The 10-K describes underwriting and pricing as using in-person evaluations, market and property data, data science, and proprietary algorithms among multiple factors; the Q3 wind-down language centers forecast volatility and operating/capital constraints rather than a named AI failure.

---

## RUBRIC-Z6

**Binary check:** Does the answer identify what Zillow preserved and why that distinction matters?

**Why it matters:** Zillow did not abandon the housing marketplace. It exited the balance-sheet-principal version of iBuying while keeping asset-light and capital-light paths.

**Pass criteria:** The answer names at least two preserved areas, such as Premier Agent, Home Loans, Closing Services, Rentals, ShowingTime, Zillow 360, seller tools, audience, brand, or the broader Zillow 2.0 strategy. It explains that preserving these businesses matters because the wind-down was a capital-allocation choice, not a retreat from real-estate transactions.

**Fail criteria:** The answer implies Zillow exited real estate, abandoned Zillow 2.0, or shut down its core marketplace.

**Source anchor:** The Q3 shareholder letter says the core business was strong and describes continued focus on Premier Agent, Home Loans, Closing Services, ShowingTime, Zillow 360, and more asset-light seller solutions.

---

## RUBRIC-Z7

**Binary check:** Does the answer include COVID-era housing-market context without overweighting it as the sole cause?

**Why it matters:** COVID-era volatility is source-supported, but overusing it turns a scaling and capital-allocation lesson into a one-off excuse.

**Pass criteria:** The answer notes the pandemic, temporary housing-market freeze, unprecedented home-price movement, supply-demand imbalance, and/or difficult labor and supply-chain environment as conditions that intensified Zillow's problems. It still names the deeper operating and capital constraints.

**Fail criteria:** The answer says Zillow Offers failed simply because of COVID, simply because home prices moved, or simply because the housing market was unusual.

**Source anchor:** Zillow cited the pandemic, a temporary housing-market freeze, supply-demand imbalance, unprecedented price movement, labor and supply-chain conditions, and operational challenges as part of the environment around the wind-down.

---

## RUBRIC-Z8

**Binary check:** Does the answer avoid unsupported claims about Zillow's internal decision process?

**Why it matters:** The methodology should not invent internal debates, warnings, motives, blame, fraud, panic, or executive psychology. This is the anti-slop guardrail.

**Pass criteria:** The answer says the Board determined on November 2, 2021 to wind down Zillow Offers, and it uses Zillow's stated reasons. It may analyze the implications, but it labels that analysis as operator inference.

**Fail criteria:** The answer claims, without source support, that executives ignored warnings, concealed losses, overrode risk teams, intentionally manipulated offers, panicked, or had specific internal disagreements.

**Source anchor:** The Form 8-K states the Board's November 2 determination and gives the filed reasons and expected wind-down actions; it does not disclose internal deliberations beyond those stated reasons.
