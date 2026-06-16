# Market Risk Analytics in Python

This project builds a Python-based market risk analytics workflow for a multi-asset ETF portfolio.

The goal is to measure portfolio risk using historical returns, volatility, drawdowns, correlation analysis, Value at Risk, Conditional Value at Risk, stress testing, and Monte Carlo simulation.

This project is for educational and analytical purposes only and is not investment advice.

## Project Objective

The objective of this project is to analyze the downside risk and diversification of a multi-asset portfolio using Python.

The portfolio includes exposure to:

* U.S. large-cap equities
* U.S. growth equities
* U.S. small-cap equities
* Developed international equities
* Emerging-market equities
* U.S. investment-grade bonds
* Gold

## Portfolio

| Ticker | Weight | Role                                    |
| ------ | -----: | --------------------------------------- |
| SPY    |    30% | U.S. large-cap equity exposure          |
| QQQ    |    20% | U.S. growth and technology exposure     |
| IWM    |    10% | U.S. small-cap equity exposure          |
| EFA    |    10% | Developed international equity exposure |
| EEM    |    10% | Emerging-market equity exposure         |
| AGG    |    15% | U.S. investment-grade bond exposure     |
| GLD    |     5% | Gold / alternative defensive exposure   |

## Methods Used

The project includes:

* Historical price data collection using `yfinance`
* Daily return calculation
* Portfolio return construction
* Annualized return and volatility
* Sharpe ratio
* Maximum drawdown
* Historical VaR and CVaR
* Correlation analysis
* Asset-level risk contribution
* Stress scenario analysis
* Monte Carlo simulation
* Final risk interpretation and limitations

## Key Findings

The portfolio is diversified across asset classes, but the analysis shows that risk is still primarily driven by equity exposure.

SPY contributes the largest share of portfolio risk because it has the largest allocation and represents broad U.S. equity exposure.

Gold has the lowest average correlation with the rest of the portfolio, making it the strongest diversifier among the selected assets.

The stress testing results show that the portfolio is most vulnerable to a broad equity market crash.

The Monte Carlo simulation provides a range of possible one-year outcomes and highlights the importance of downside risk analysis.

## Limitations

This project uses historical data and simplified assumptions.

Important limitations include:

* Historical returns may not represent future market behavior.
* Correlations can change during periods of stress.
* Stress scenarios are manually defined and hypothetical.
* The Monte Carlo simulation assumes normally distributed returns.
* The portfolio weights are assumed, not optimized.
* The analysis does not include taxes, transaction costs, liquidity risk, or investor-specific constraints.

## Project Structure

```text
market-risk-analytics-python/
│
├── notebooks/
│   └── 01_portfolio_risk_modeling.ipynb
│
├── reports/
│   └── decision_log.md
│
├── src/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/jimech/market-risk-analytics-python.git
cd market-risk-analytics-python
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/01_portfolio_risk_modeling.ipynb
```

## Tools

* Python
* pandas
* numpy
* matplotlib
* yfinance
* Jupyter Notebook
