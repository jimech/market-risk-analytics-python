import numpy as np
import pandas as pd

from src.stress_tests import calculate_stress_results, calculate_stress_loss_table


def test_calculate_stress_results():
    stress_scenarios = pd.DataFrame({
        "Asset_A": [-0.10, -0.20],
        "Asset_B": [0.02, -0.05],
    }, index=["Scenario_1", "Scenario_2"])

    weights = pd.Series({
        "Asset_A": 0.60,
        "Asset_B": 0.40,
    })

    results = calculate_stress_results(stress_scenarios, weights)

    assert "Portfolio Impact" in results.columns
    assert np.isclose(results.loc["Scenario_1", "Portfolio Impact"], -0.052)


def test_calculate_stress_loss_table():
    stress_results = pd.DataFrame({
        "Portfolio Impact": [-0.10, 0.05],
    }, index=["Scenario_1", "Scenario_2"])

    loss_table = calculate_stress_loss_table(
        stress_results,
        initial_portfolio_value=10_000
    )

    assert "Estimated Portfolio Value" in loss_table.columns
    assert "Estimated Dollar Gain/Loss" in loss_table.columns
    assert loss_table.iloc[0]["Estimated Portfolio Value"] == 9000
    assert loss_table.iloc[1]["Estimated Portfolio Value"] == 10500