import numpy as np
import pandas as pd

from src.risk_metrics import (
    calculate_simple_returns,
    calculate_portfolio_returns,
    calculate_cumulative_returns,
    calculate_drawdown,
    calculate_max_drawdown,
    calculate_historical_var,
    calculate_historical_cvar,
    calculate_risk_contribution,
)


def test_calculate_simple_returns():
    prices = pd.DataFrame({
        "Asset_A": [100, 101, 102, 103],
        "Asset_B": [200, 198, 202, 204],
    })

    returns = calculate_simple_returns(prices)

    assert isinstance(returns, pd.DataFrame)
    assert returns.shape == (3, 2)
    assert returns.isna().sum().sum() == 0


def test_calculate_portfolio_returns():
    returns = pd.DataFrame({
        "Asset_A": [0.01, 0.02, -0.01],
        "Asset_B": [0.00, 0.01, 0.02],
    })

    weights = np.array([0.60, 0.40])

    portfolio_returns = calculate_portfolio_returns(returns, weights)

    assert len(portfolio_returns) == 3
    assert np.isclose(portfolio_returns.iloc[0], 0.006)


def test_calculate_cumulative_returns():
    portfolio_returns = pd.Series([0.01, -0.02, 0.03])

    cumulative_returns = calculate_cumulative_returns(portfolio_returns)

    assert len(cumulative_returns) == 3
    assert np.isclose(cumulative_returns.iloc[0], 1.01)


def test_drawdown_functions():
    cumulative_returns = pd.Series([1.00, 1.10, 1.05, 1.20, 1.00])

    drawdown = calculate_drawdown(cumulative_returns)
    max_drawdown = calculate_max_drawdown(cumulative_returns)

    assert len(drawdown) == 5
    assert max_drawdown <= 0


def test_historical_var_and_cvar():
    portfolio_returns = pd.Series([0.01, -0.02, 0.005, -0.03, 0.02, -0.01])

    var_95 = calculate_historical_var(portfolio_returns, confidence_level=0.95)
    cvar_95 = calculate_historical_cvar(portfolio_returns, confidence_level=0.95)

    assert var_95 < 0
    assert cvar_95 <= var_95


def test_risk_contribution_sums_to_one():
    returns = pd.DataFrame({
        "Asset_A": [0.01, 0.02, -0.01, 0.015],
        "Asset_B": [0.005, 0.01, -0.005, 0.007],
    })

    weights = np.array([0.60, 0.40])

    risk_contribution = calculate_risk_contribution(returns, weights)

    total_risk_contribution = risk_contribution["Risk Contribution (%)"].sum()

    assert np.isclose(total_risk_contribution, 1.0)