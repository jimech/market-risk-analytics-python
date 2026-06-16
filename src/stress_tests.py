import pandas as pd


def calculate_stress_results(stress_scenarios, weights):
    """
    Calculate portfolio impact under each stress scenario.
    """
    stress_results = stress_scenarios.copy()
    stress_results["Portfolio Impact"] = stress_scenarios @ weights

    return stress_results


def calculate_stress_loss_table(stress_results, initial_portfolio_value=10_000):
    """
    Calculate estimated portfolio value and gain/loss under stress scenarios.
    """
    stress_loss_table = pd.DataFrame({
        "Scenario": stress_results.index,
        "Portfolio Impact": stress_results["Portfolio Impact"],
        "Estimated Portfolio Value": initial_portfolio_value * (1 + stress_results["Portfolio Impact"]),
        "Estimated Dollar Gain/Loss": initial_portfolio_value * stress_results["Portfolio Impact"]
    })

    return stress_loss_table