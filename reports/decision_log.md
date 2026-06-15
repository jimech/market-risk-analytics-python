# Decision Log

## Decision 1: Portfolio definition

For the first version of this project, I selected a 7-asset ETF portfolio:

| Ticker | Weight | Role |
|---|---:|---|
| SPY | 30% | U.S. large-cap equity exposure |
| QQQ | 20% | U.S. growth and technology exposure |
| IWM | 10% | U.S. small-cap equity exposure |
| EFA | 10% | Developed international equity exposure |
| EEM | 10% | Emerging-market equity exposure |
| AGG | 15% | U.S. investment-grade bond exposure |
| GLD | 5% | Gold / alternative defensive exposure |

## Reasoning

This portfolio was selected because it is simple enough for a first risk modeling project but diversified enough to analyze meaningful risk relationships.

It includes equities, bonds, and gold, which allows the project to study volatility, correlation, downside risk, diversification, and stress scenario behavior.

## Limitations

The weights are assumed, not optimized.  
The portfolio is ETF-based and simplified.  
It does not include individual stocks, derivatives, currencies, commodities other than gold, private assets, or real estate.  
The portfolio should be treated as an educational case study, not an investment recommendation.