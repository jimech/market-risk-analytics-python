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

## Decision 5: Historical risk metrics

The project calculates annualized return, annualized volatility, Sharpe ratio, maximum drawdown, historical VaR, and historical CVaR.

## Reasoning

These metrics provide a first view of portfolio performance, volatility, downside risk, and tail risk.

Annualized return and volatility summarize the portfolio’s average yearly behavior.  
Maximum drawdown measures the worst historical decline from a previous peak.  
VaR estimates a loss threshold under normal historical conditions.  
CVaR estimates the average loss during the worst historical outcomes.

## Decision 6: Risk-free rate assumption

For the first version of the Sharpe ratio calculation, I use a 0% annual risk-free rate.

## Reasoning

This keeps the first version simple and focused on the mechanics of risk measurement. A future version can improve the model by using an actual Treasury yield or another market-based risk-free rate.

## Limitations

Historical risk metrics depend on the selected time period and assume that historical behavior is informative. VaR and CVaR based on historical returns may not fully capture future crises or market regimes that did not appear in the sample.

## Decision 7: Correlation and risk contribution analysis

The project includes a correlation matrix and asset-level risk contribution analysis.

## Reasoning

Correlation helps evaluate whether the portfolio is truly diversified or whether assets tend to move together.

Risk contribution analysis helps identify which holdings drive the largest share of total portfolio volatility. This is more informative than looking at portfolio weights alone because a smaller position can still contribute significantly to risk if it is volatile or highly correlated with other assets.

## Limitations

Correlation is estimated using historical returns and may change over time, especially during market stress. Risk contribution is based on volatility and covariance, so it does not fully capture tail risk, liquidity risk, or sudden regime changes.

## Decision 8: Stress testing framework

The project includes several hypothetical stress scenarios:

- Equity Market Crash
- Technology Selloff
- Interest Rate Shock
- Emerging Market Crisis
- Broad Risk-Off Event

Each scenario applies assumed percentage shocks to the assets in the portfolio. The total portfolio impact is calculated as the weighted sum of asset-level shocks.

## Reasoning

Stress testing helps evaluate how the portfolio may behave under adverse market conditions. This is useful because historical averages, volatility, and VaR may not fully communicate the impact of specific market events.

## Limitations

The stress scenarios are hypothetical and simplified. They are not forecasts. The assumed shocks are manually selected and may not match real future market behavior. The analysis also assumes instant price changes and does not model liquidity, trading costs, changing correlations, or investor behavior during stress.

## Decision 9: Monte Carlo simulation

The project includes a one-year Monte Carlo simulation with 10,000 simulated portfolio paths.

The simulation uses the historical daily mean return and daily volatility of the portfolio as inputs.

## Reasoning

Monte Carlo simulation helps estimate a range of possible future outcomes instead of relying on a single expected return. It allows the project to analyze downside and upside scenarios, simulated ending values, and simulated one-year VaR and CVaR.

## Limitations

This first version assumes normally distributed daily portfolio returns. This is a simplified assumption and may underestimate extreme losses. The model also assumes that historical mean and volatility are reasonable inputs for future simulations.

Future improvements may include bootstrapped historical returns, fat-tailed distributions, asset-level correlated simulations, or regime-based simulations.

## Decision 10: Results interpretation framework

The project includes a final interpretation section that summarizes the main findings from the historical risk metrics, correlation analysis, risk contribution analysis, stress testing, and Monte Carlo simulation.

## Reasoning

Risk analytics is not only about calculating metrics. The results must be translated into clear insights about diversification, downside risk, concentration risk, and model limitations.

## Limitations

The interpretation depends on the selected portfolio, time period, assumptions, and data source. The conclusions should be treated as analytical observations, not investment advice.

## Decision 11: Rolling risk analytics

The project adds rolling volatility, rolling Sharpe ratio, rolling maximum drawdown, and rolling correlation with SPY using a 63-day rolling window.

## Reasoning

Risk is not constant over time. Rolling metrics help identify how portfolio risk, risk-adjusted performance, drawdowns, and equity-market dependence change across different market environments.

A 63-day window is used because it approximates one trading quarter, making it short enough to detect changing risk conditions while still containing enough observations to calculate meaningful statistics.

## Limitations

Rolling metrics are sensitive to the selected window size. A shorter window may be noisy, while a longer window may react slowly to new market conditions. These metrics are backward-looking and do not predict future risk.

## Decision 12: VaR method comparison

The project compares historical VaR, parametric normal VaR, and Monte Carlo normal VaR at 95% and 99% confidence levels.

## Reasoning

Different VaR methods rely on different assumptions. Historical VaR uses the actual observed return distribution. Parametric VaR assumes normally distributed returns. Monte Carlo VaR estimates risk through simulation.

Comparing these methods helps evaluate whether downside risk estimates are sensitive to the selected methodology.

## Limitations

The parametric and Monte Carlo methods in this version assume normally distributed returns. This may underestimate extreme market losses if returns have fat tails, skewness, volatility clustering, or regime changes.

## Decision 13: VaR backtesting

The project includes VaR backtesting using a 252-day rolling historical VaR model at the 95% confidence level.

A VaR exception occurs when the actual daily portfolio return is worse than the estimated VaR threshold.

The project also applies the Kupiec Proportion of Failures test to compare the actual exception rate against the expected exception rate.

## Reasoning

Backtesting helps evaluate whether the VaR model is reasonably calibrated. Instead of only calculating VaR, the project tests how often actual losses exceeded the estimated VaR threshold.

## Limitations

The Kupiec test evaluates the number of exceptions but does not test whether exceptions are clustered over time. The backtest also depends on the selected rolling window, confidence level, and historical sample.