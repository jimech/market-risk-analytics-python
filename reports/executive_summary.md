# Executive Risk Summary

## Project Overview

This project analyzes the market risk of a multi-asset ETF portfolio using Python.

The portfolio includes exposure to U.S. equities, growth equities, small-cap equities, developed international equities, emerging-market equities, bonds, and gold.

The goal is to evaluate portfolio risk using historical returns, volatility, drawdowns, correlation analysis, VaR, CVaR, stress testing, Monte Carlo simulation, bootstrap simulation, and VaR backtesting.

## Portfolio Risk Profile

The portfolio is diversified across asset classes, but its risk is primarily driven by equity exposure.

SPY contributes the largest share of portfolio volatility because it has the highest allocation and represents broad U.S. equity exposure.

Gold has the lowest average correlation with the rest of the portfolio, making it the strongest diversifier among the selected assets.

## Key Risk Findings

The portfolio experienced a meaningful historical maximum drawdown, showing that the allocation can suffer significant losses during stressed market environments.

Historical VaR and CVaR show that downside losses can exceed normal daily fluctuations, especially during tail-risk events.

The stress testing results show that the portfolio is most vulnerable to a broad equity market crash.

The Monte Carlo and bootstrap simulations provide a range of possible one-year outcomes and highlight the importance of analyzing downside risk rather than relying only on expected return.

## Model Enhancements

The project includes several advanced risk analytics components:

* Rolling volatility and rolling Sharpe ratio
* Rolling drawdown analysis
* Rolling correlation with SPY
* Historical, parametric, and Monte Carlo VaR comparison
* VaR backtesting using a rolling historical VaR model
* Kupiec Proportion of Failures test
* Correlated asset-level Monte Carlo simulation
* Historical bootstrap simulation
* Reusable Python modules in the `src/` folder

## Main Risk Management Insight

The main risk is equity concentration.

Although the portfolio holds multiple ETFs, many of the equity assets may become highly correlated during stressed markets. This means the portfolio may appear diversified but still behave like an equity-heavy portfolio during market downturns.

## Recommendation

A risk manager or investor may consider reducing exposure to highly correlated equity assets or increasing exposure to assets with lower correlation and lower volatility.

The current allocation is useful for growth-oriented exposure, but it should be monitored carefully for downside risk, drawdown behavior, and changing correlations during market stress.

## Limitations

This analysis is based on historical market data and simplified modeling assumptions.

Important limitations include:

* Historical returns may not represent future returns.
* Correlations may change during crises.
* VaR may underestimate extreme losses.
* Normal Monte Carlo simulation may underestimate fat-tail risk.
* Bootstrap simulation is limited to historical observations.
* Stress scenarios are hypothetical and manually defined.
* The portfolio weights are assumed, not optimized.
* Taxes, transaction costs, liquidity risk, currency risk, and investor-specific constraints are not included.

## Conclusion

This project demonstrates a complete Python-based market risk analytics workflow.

It combines financial risk concepts with software engineering practices by using a documented notebook, reusable source modules, a decision log, and an executive summary.

The analysis shows that the portfolio is diversified by asset category, but its risk remains mainly driven by equity exposure.
