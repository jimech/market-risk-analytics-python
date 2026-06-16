from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


CHART_DIR = Path("output/charts")
CHART_DIR.mkdir(parents=True, exist_ok=True)

tickers = ["SPY", "QQQ", "IWM", "EFA", "EEM", "AGG", "GLD"]
weights = np.array([0.30, 0.20, 0.10, 0.10, 0.10, 0.15, 0.05])
weights_series = pd.Series(weights, index=tickers)

start_date = "2019-01-01"
initial_portfolio_value = 10_000
trading_days = 252

price_data = yf.download(
    tickers,
    start=start_date,
    end=None,
    auto_adjust=True,
    progress=False,
)

prices = price_data["Close"].dropna()
if prices.empty:
    raise RuntimeError("No price data downloaded. Check network access and yfinance.")

returns = prices.pct_change().dropna()
if returns.empty:
    raise RuntimeError("No return data available after price download.")

portfolio_returns = returns @ weights
cumulative_returns = (1 + portfolio_returns).cumprod()


def save_current_figure(filename: str) -> None:
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=180, bbox_inches="tight")
    plt.close()


plt.figure(figsize=(12, 6))
plt.plot(cumulative_returns, linewidth=2)
plt.title("Portfolio Growth Over Time")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.grid(True, alpha=0.3)
save_current_figure("portfolio_growth.png")


running_max = cumulative_returns.cummax()
drawdown = cumulative_returns / running_max - 1

plt.figure(figsize=(12, 6))
plt.plot(drawdown, linewidth=2)
plt.title("Portfolio Drawdown Over Time")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.grid(True, alpha=0.3)
save_current_figure("portfolio_drawdown.png")


cov_matrix = returns.cov()
portfolio_variance = weights_series.T @ cov_matrix @ weights_series
portfolio_volatility_from_cov = np.sqrt(portfolio_variance)
marginal_risk_contribution = cov_matrix @ weights_series / portfolio_volatility_from_cov
risk_contribution = weights_series * marginal_risk_contribution
risk_contribution_percent = risk_contribution / portfolio_volatility_from_cov

risk_contribution_table = pd.DataFrame(
    {
        "Weight": weights_series,
        "Marginal Risk Contribution": marginal_risk_contribution,
        "Risk Contribution": risk_contribution,
        "Risk Contribution (%)": risk_contribution_percent,
    }
)

plt.figure(figsize=(10, 6))
plt.bar(risk_contribution_table.index, risk_contribution_table["Risk Contribution (%)"])
plt.title("Risk Contribution by Asset")
plt.xlabel("Asset")
plt.ylabel("Contribution to Portfolio Risk")
plt.grid(True, axis="y", alpha=0.3)
save_current_figure("risk_contribution.png")


stress_scenarios = pd.DataFrame(
    {
        "Equity Market Crash": {
            "SPY": -0.25,
            "QQQ": -0.35,
            "IWM": -0.30,
            "EFA": -0.25,
            "EEM": -0.30,
            "AGG": 0.04,
            "GLD": 0.08,
        },
        "Interest Rate Shock": {
            "SPY": -0.08,
            "QQQ": -0.12,
            "IWM": -0.10,
            "EFA": -0.07,
            "EEM": -0.10,
            "AGG": -0.08,
            "GLD": -0.03,
        },
        "Inflation Shock": {
            "SPY": -0.10,
            "QQQ": -0.15,
            "IWM": -0.12,
            "EFA": -0.10,
            "EEM": -0.12,
            "AGG": -0.06,
            "GLD": 0.10,
        },
        "Growth Selloff": {
            "SPY": -0.10,
            "QQQ": -0.25,
            "IWM": -0.12,
            "EFA": -0.08,
            "EEM": -0.10,
            "AGG": 0.02,
            "GLD": 0.03,
        },
        "Emerging Market Crisis": {
            "SPY": -0.06,
            "QQQ": -0.08,
            "IWM": -0.08,
            "EFA": -0.10,
            "EEM": -0.30,
            "AGG": 0.03,
            "GLD": 0.06,
        },
        "Defensive Rally": {
            "SPY": -0.03,
            "QQQ": -0.04,
            "IWM": -0.05,
            "EFA": -0.03,
            "EEM": -0.04,
            "AGG": 0.05,
            "GLD": 0.12,
        },
    }
).T

stress_results = stress_scenarios.copy()
stress_results["Portfolio Impact"] = stress_scenarios @ weights_series

plt.figure(figsize=(12, 6))
plt.bar(stress_results.index, stress_results["Portfolio Impact"])
plt.title("Portfolio Impact Under Stress Scenarios")
plt.xlabel("Stress Scenario")
plt.ylabel("Estimated Portfolio Impact")
plt.xticks(rotation=45, ha="right")
plt.grid(True, axis="y", alpha=0.3)
save_current_figure("stress_scenarios.png")


np.random.seed(42)
num_simulations = 10_000
forecast_horizon_days = 252
daily_mean_return = portfolio_returns.mean()
daily_volatility = portfolio_returns.std()

simulated_daily_returns = np.random.normal(
    loc=daily_mean_return,
    scale=daily_volatility,
    size=(forecast_horizon_days, num_simulations),
)

simulated_portfolio_paths = initial_portfolio_value * (
    1 + simulated_daily_returns
).cumprod(axis=0)

percentiles = np.percentile(
    simulated_portfolio_paths,
    [5, 25, 50, 75, 95],
    axis=1,
)

percentile_paths = pd.DataFrame(
    {
        "5th Percentile": percentiles[0],
        "25th Percentile": percentiles[1],
        "Median": percentiles[2],
        "75th Percentile": percentiles[3],
        "95th Percentile": percentiles[4],
    }
)

plt.figure(figsize=(12, 6))
for column in percentile_paths.columns:
    plt.plot(percentile_paths[column], label=column)
plt.title("Monte Carlo Simulation: One-Year Portfolio Value Paths")
plt.xlabel("Trading Days")
plt.ylabel("Portfolio Value")
plt.legend()
plt.grid(True, alpha=0.3)
save_current_figure("monte_carlo_paths.png")


backtest_window = 252
backtest_tail_probability = 0.05
rolling_historical_var_95 = portfolio_returns.rolling(window=backtest_window).quantile(
    backtest_tail_probability
)

var_backtest = pd.DataFrame(
    {
        "Portfolio Return": portfolio_returns,
        "Rolling Historical VaR 95%": rolling_historical_var_95,
    }
).dropna()

var_backtest["VaR Exception"] = (
    var_backtest["Portfolio Return"] < var_backtest["Rolling Historical VaR 95%"]
)

plt.figure(figsize=(12, 6))
plt.plot(var_backtest.index, var_backtest["Portfolio Return"], label="Portfolio Return")
plt.plot(
    var_backtest.index,
    var_backtest["Rolling Historical VaR 95%"],
    label="Rolling Historical VaR 95%",
)

exceptions = var_backtest[var_backtest["VaR Exception"]]
plt.scatter(
    exceptions.index,
    exceptions["Portfolio Return"],
    color="red",
    label="VaR Exceptions",
    zorder=3,
)

plt.title("VaR Backtesting: Portfolio Returns vs Rolling Historical VaR")
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.legend()
plt.grid(True, alpha=0.3)
save_current_figure("var_backtesting.png")

for path in sorted(CHART_DIR.glob("*.png")):
    print(path)
