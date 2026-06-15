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

## Decision 2: Analysis period

The selected analysis period is 2019-01-01 to 2024-12-31.

## Reasoning

This period includes multiple market regimes, including the pre-COVID market environment, the COVID-19 crash, the post-COVID recovery, the 2022 inflation and interest-rate shock, and the 2023–2024 recovery period.

This makes the period useful for studying volatility, drawdowns, correlation, downside risk, stress scenarios, and recovery behavior.

## Limitations

The analysis depends on the selected historical period. Results may change significantly if a longer or shorter period is used. Historical behavior may not represent future market behavior.

## Decision 3: Historical price data

Historical daily price data is downloaded using `yfinance`.

The project uses adjusted closing prices because adjusted prices account for dividends and splits, making them more suitable for return and risk calculations.

The selected start date is 2019-01-01. The end date is left open so the notebook uses the latest available market data whenever it is rerun.

## Reasoning

Using recent and automatically updated data makes the project behave like a living market risk analytics workflow instead of a static historical report.

## Limitations

The project depends on the availability and quality of data from `yfinance`. Data issues, missing values, ticker changes, or provider limitations may affect the results.

## Decision 4: Return calculation method

Daily simple percentage returns are calculated from adjusted closing prices using `pct_change()`.

## Reasoning

Returns are used instead of raw prices because risk metrics such as volatility, drawdown, VaR, CVaR, and portfolio risk contribution are based on changes in value, not price levels.

Simple returns are used in the first version of the project because they are easier to interpret and explain than log returns.

## Limitations

Simple returns may be less mathematically convenient than log returns for some advanced modeling tasks. A future version of the project may compare simple returns with log returns.