# Market Basket Optimisation — Association Rule Learning

Discovers frequently co-purchased products from a week's worth of grocery transaction data using two classic association rule learning algorithms — **Apriori** and **ECLAT**.

## Problem Statement

Retailers want to understand which products are commonly bought together so they can optimise store layouts, design bundle promotions, and improve recommendation engines. Association Rule Learning mines these patterns automatically from transaction data.

## Dataset

**File:** `Market_Basket_Optimisation.csv`

- **7,500 transactions** from a French grocery store over one week
- Each row is a customer's shopping basket containing up to **20 items**
- No header row — each column is a product slot (some may be empty)

## Algorithms

### Model 1 — Apriori (`Apriori.py`)

Apriori generates rules of the form **"If a customer buys X, they also buy Y"** and ranks them by three metrics:

| Metric | Definition | Threshold Used |
|---|---|---|
| **Support** | Fraction of transactions containing both items | ≥ 0.003 (3 in 1000) |
| **Confidence** | P(Y \| X) — how often the rule is correct | ≥ 0.2 |
| **Lift** | How much more likely Y is given X vs. by chance | ≥ 3 |

**Parameters:**
- `min_length = 2`, `max_length = 2` — itemsets of exactly 2 products
- Results displayed as a sorted DataFrame, top 10 rules by **Lift**

### Model 2 — ECLAT (`Eclat.py`)

ECLAT is a simpler, faster variant that works with **vertical data representation** (transaction ID sets). Unlike Apriori it focuses purely on **co-occurrence frequency (Support)** without computing confidence or lift.

**Parameters:** Same support threshold (≥ 0.003), itemsets of exactly 2 products.

Results displayed as top 10 product pairs ranked by **Support**.

## Key Difference Between the Two Models

| | Apriori | ECLAT |
|---|---|---|
| Output | Support, Confidence, Lift | Support only |
| Use case | Directional rules ("X → Y") | Symmetric co-occurrence |
| Ranking | By Lift (strength of association) | By Support (frequency) |

## Requirements

```
numpy
pandas
matplotlib
apyori
```

Install with:
```bash
pip install numpy pandas matplotlib apyori
```

> **Note:** Both scripts auto-install `apyori` at runtime using `subprocess`.

## Usage

```bash
# Run Apriori association rule mining
python Apriori.py

# Run ECLAT co-occurrence mining
python Eclat.py
```

Ensure `Market_Basket_Optimisation.csv` is in the same directory as the scripts.

## Output

- **Apriori:** A table of the top 10 product pairs ranked by Lift, with Support, Confidence, and Lift values
- **ECLAT:** A table of the top 10 most frequently co-purchased product pairs ranked by Support
