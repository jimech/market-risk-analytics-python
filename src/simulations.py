import numpy as np
import pandas as pd


def run_portfolio_monte_carlo(
    portfolio_returns,
    num_simulations=10_000,
    forecast_horizon_days=252,
    initial_portfolio_value=10_000,
    random_seed=42
):
    """
    Run a portfolio-level normal Monte Carlo simulation.
    """
    np.random.seed(random_seed)

    daily_mean_return = portfolio_returns.mean()
    daily_volatility = portfolio_returns.std()

    simulated_daily_returns = np.random.normal(
        loc=daily_mean_return,
        scale=daily_volatility,
        size=(forecast_horizon_days, num_simulations)
    )

    simulated_paths = initial_portfolio_value * (1 + simulated_daily_returns).cumprod(axis=0)

    return simulated_paths


def run_bootstrap_simulation(
    portfolio_returns,
    num_simulations=10_000,
    forecast_horizon_days=252,
    initial_portfolio_value=10_000,
    random_seed=42
):
    """
    Run a bootstrap simulation by resampling historical portfolio returns.
    """
    np.random.seed(random_seed)

    bootstrap_daily_returns = np.random.choice(
        portfolio_returns.values,
        size=(forecast_horizon_days, num_simulations),
        replace=True
    )

    bootstrap_paths = initial_portfolio_value * (1 + bootstrap_daily_returns).cumprod(axis=0)

    return bootstrap_paths


def summarize_simulation_paths(simulated_paths, initial_portfolio_value=10_000):
    """
    Summarize ending values and one-year returns from simulated paths.
    """
    ending_values = simulated_paths[-1, :]
    one_year_returns = ending_values / initial_portfolio_value - 1

    summary = pd.DataFrame({
        "Metric": [
            "Mean Ending Value",
            "Median Ending Value",
            "5th Percentile Ending Value",
            "95th Percentile Ending Value",
            "Worst Simulated Ending Value",
            "Best Simulated Ending Value",
            "Mean One-Year Return",
            "Median One-Year Return",
            "5th Percentile One-Year Return",
            "95th Percentile One-Year Return"
        ],
        "Value": [
            ending_values.mean(),
            np.median(ending_values),
            np.percentile(ending_values, 5),
            np.percentile(ending_values, 95),
            ending_values.min(),
            ending_values.max(),
            one_year_returns.mean(),
            np.median(one_year_returns),
            np.percentile(one_year_returns, 5),
            np.percentile(one_year_returns, 95)
        ]
    })

    return summary


def calculate_simulation_var_cvar(simulated_paths, initial_portfolio_value=10_000, confidence_level=0.95):
    """
    Calculate VaR and CVaR from simulated ending values.
    """
    ending_values = simulated_paths[-1, :]
    one_year_returns = ending_values / initial_portfolio_value - 1

    var = np.percentile(one_year_returns, (1 - confidence_level) * 100)
    cvar = one_year_returns[one_year_returns <= var].mean()

    return var, cvar