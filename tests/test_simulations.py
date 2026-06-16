import numpy as np
import pandas as pd

from src.simulations import (
    run_portfolio_monte_carlo,
    run_bootstrap_simulation,
    summarize_simulation_paths,
    calculate_simulation_var_cvar,
)


def test_run_portfolio_monte_carlo_shape():
    portfolio_returns = pd.Series([0.01, -0.005, 0.002, 0.004, -0.003])

    simulated_paths = run_portfolio_monte_carlo(
        portfolio_returns,
        num_simulations=100,
        forecast_horizon_days=10,
        initial_portfolio_value=10_000,
        random_seed=42
    )

    assert simulated_paths.shape == (10, 100)


def test_run_bootstrap_simulation_shape():
    portfolio_returns = pd.Series([0.01, -0.005, 0.002, 0.004, -0.003])

    bootstrap_paths = run_bootstrap_simulation(
        portfolio_returns,
        num_simulations=100,
        forecast_horizon_days=10,
        initial_portfolio_value=10_000,
        random_seed=42
    )

    assert bootstrap_paths.shape == (10, 100)


def test_summarize_simulation_paths():
    simulated_paths = np.array([
        [10000, 10000, 10000],
        [10100, 9900, 10200],
        [10300, 9700, 10400],
    ])

    summary = summarize_simulation_paths(
        simulated_paths,
        initial_portfolio_value=10_000
    )

    assert "Metric" in summary.columns
    assert "Value" in summary.columns
    assert len(summary) == 10


def test_calculate_simulation_var_cvar():
    simulated_paths = np.array([
        [10000, 10000, 10000, 10000],
        [10100, 9900, 9800, 10200],
        [10300, 9700, 9600, 10400],
    ])

    var, cvar = calculate_simulation_var_cvar(
        simulated_paths,
        initial_portfolio_value=10_000,
        confidence_level=0.95
    )

    assert var < 0
    assert cvar <= var