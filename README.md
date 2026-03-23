# Phoenix Autocall Pricing — Monte Carlo Simulation

Pricing of a 3-year Phoenix autocall structured product using Monte Carlo simulation in Python.

## Product Description
A Phoenix autocall pays a periodic coupon if the underlying stays above a coupon barrier,
and reimburses capital early (autocall) if the underlying reaches the initial spot.
Capital loss occurs only if the underlying breaches the capital barrier at maturity.

- **Underlying spot** : 100
- **Coupon** : 8% per year
- **Coupon barrier** : 70% of initial spot
- **Capital barrier** : 60% of initial spot
- **Maturity** : 3 years
- **Autocall trigger** : 100% of initial spot (observed annually)
- **Volatility** : 25%
- **Drift** : 2%

## Methodology
- Monte Carlo simulation with **10 000 paths**
- Underlying modelled via **Geometric Brownian Motion (GBM)**
- Annual observations for autocall trigger and coupon payment
- Three scenarios at maturity if not autocalled :
  - S_final ≥ 70% × S0 → full capital + coupon
  - 60% × S0 ≤ S_final < 70% × S0 → capital only
  - S_final < 60% × S0 → capital loss (proportional to underlying)

## Key Results
| Metric | Structured | Equity |
|---|---|---|
| Average payoff | ~105 | ~106 |
| Proba autocall T=1 | ~50% | — |
| Proba capital loss | ~13% | — |
| Worst case | ~40 | ~40 |

## Key Takeaway
The Phoenix autocall matches equity average returns while limiting downside
to -40% maximum — suitable for a conservative client profile seeking
yield enhancement with partial capital protection.

## Tech Stack
- Python 3
- NumPy

## Author
Mathis Sebilleau — [LinkedIn](https://www.linkedin.com/in/mathis-sebilleau)
