import numpy as np
import pandas as pd


def calculate_simple_returns(prices):
    """
    Calculate simple daily returns from price data.
    """
    return prices.pct_change().dropna()


def calculate_portfolio_returns(returns, weights):
    """
    Calculate portfolio returns from asset returns and portfolio weights.
    """
    return returns @ weights


def calculate_cumulative_returns(portfolio_returns):
    """
    Calculate cumulative portfolio growth from portfolio returns.
    """
    return (1 + portfolio_returns).cumprod()


def calculate_annualized_return(portfolio_returns, trading_days=252):
    """
    Calculate annualized return from daily portfolio returns.
    """
    return (1 + portfolio_returns.mean()) ** trading_days - 1


def calculate_annualized_volatility(portfolio_returns, trading_days=252):
    """
    Calculate annualized volatility from daily portfolio returns.
    """
    return portfolio_returns.std() * np.sqrt(trading_days)


def calculate_sharpe_ratio(portfolio_returns, risk_free_rate=0.0, trading_days=252):
    """
    Calculate annualized Sharpe ratio.
    """
    annualized_return = calculate_annualized_return(portfolio_returns, trading_days)
    annualized_volatility = calculate_annualized_volatility(portfolio_returns, trading_days)

    return (annualized_return - risk_free_rate) / annualized_volatility


def calculate_drawdown(cumulative_returns):
    """
    Calculate portfolio drawdown series.
    """
    running_max = cumulative_returns.cummax()
    drawdown = cumulative_returns / running_max - 1

    return drawdown


def calculate_max_drawdown(cumulative_returns):
    """
    Calculate maximum drawdown.
    """
    drawdown = calculate_drawdown(cumulative_returns)

    return drawdown.min()


def calculate_historical_var(portfolio_returns, confidence_level=0.95):
    """
    Calculate historical Value at Risk.
    """
    return portfolio_returns.quantile(1 - confidence_level)


def calculate_historical_cvar(portfolio_returns, confidence_level=0.95):
    """
    Calculate historical Conditional Value at Risk.
    """
    var = calculate_historical_var(portfolio_returns, confidence_level)

    return portfolio_returns[portfolio_returns <= var].mean()


def calculate_risk_summary(
    portfolio_returns,
    cumulative_returns,
    risk_free_rate=0.0,
    confidence_level=0.95,
    trading_days=252
):
    """
    Calculate a summary table of key portfolio risk metrics.
    """
    summary = pd.DataFrame({
        "Metric": [
            "Annualized Return",
            "Annualized Volatility",
            "Sharpe Ratio",
            "Maximum Drawdown",
            f"Historical VaR {confidence_level:.0%}",
            f"Historical CVaR {confidence_level:.0%}"
        ],
        "Value": [
            calculate_annualized_return(portfolio_returns, trading_days),
            calculate_annualized_volatility(portfolio_returns, trading_days),
            calculate_sharpe_ratio(portfolio_returns, risk_free_rate, trading_days),
            calculate_max_drawdown(cumulative_returns),
            calculate_historical_var(portfolio_returns, confidence_level),
            calculate_historical_cvar(portfolio_returns, confidence_level)
        ]
    })

    return summary


def calculate_risk_contribution(returns, weights, trading_days=252):
    """
    Calculate asset-level contribution to total portfolio volatility.
    """
    cov_matrix = returns.cov() * trading_days
    weights_series = pd.Series(weights, index=returns.columns)

    portfolio_variance = weights_series.T @ cov_matrix @ weights_series
    portfolio_volatility = np.sqrt(portfolio_variance)

    marginal_risk_contribution = cov_matrix @ weights_series / portfolio_volatility
    risk_contribution = weights_series * marginal_risk_contribution
    risk_contribution_percent = risk_contribution / portfolio_volatility

    risk_contribution_table = pd.DataFrame({
        "Weight": weights_series,
        "Marginal Risk Contribution": marginal_risk_contribution,
        "Risk Contribution": risk_contribution,
        "Risk Contribution (%)": risk_contribution_percent
    }).sort_values("Risk Contribution (%)", ascending=False)

    return risk_contribution_table