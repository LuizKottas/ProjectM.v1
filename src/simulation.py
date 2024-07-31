import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Ensure the correct path is added to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prisoners_dilemma import PrisonersDilemma
from src.coordination_game import CoordinationGame
from src.stag_hunt import StagHunt
from src.moral_dilemma import MoralDilemma
from src.moral_path import MoralPath

def run_game_theory_simulations(iterations=100):
    # Initialize game theory models
    pd = PrisonersDilemma()
    cg = CoordinationGame()
    sh = StagHunt()
    md = MoralDilemma()

    # Run simulations and collect results
    pd_results = [pd.find_nash_equilibrium() for _ in range(iterations)]
    cg_results = [cg.find_nash_equilibrium() for _ in range(iterations)]
    sh_results = [sh.find_nash_equilibrium() for _ in range(iterations)]
    md_results = [md.find_nash_equilibrium() for _ in range(iterations)]

    return pd_results, cg_results, sh_results, md_results

def run_moral_path_simulations(iterations=100):
    parameters = np.array([1, 2, 3])  # Example parameters for the moral function
    g_values = np.random.rand(iterations, 3)  # Example input values for iterations

    moral_path_estimator = MoralPath(parameters)
    estimated_paths = [moral_path_estimator.estimate_moral_path(g) for g in g_values]

    return estimated_paths

def visualize_results(estimated_paths):
    plt.figure(figsize=(10, 6))
    for idx, path in enumerate(estimated_paths):
        plt.plot(path, label=f'Iteration {idx}')
    plt.xlabel('Dimension')
    plt.ylabel('Moral Path Value')
    plt.title('Moral Path Estimation Over Iterations')
    plt.legend()
    plt.show()

def main():
    iterations = 100

    # Run game theory simulations
    pd_results, cg_results, sh_results, md_results = run_game_theory_simulations(iterations)
    print(f"Prisoner's Dilemma Results: {pd_results}")
    print(f"Coordination Game Results: {cg_results}")
    print(f"Stag Hunt Results: {sh_results}")
    print(f"Moral Dilemma Results: {md_results}")

    # Run moral path simulations
    estimated_paths = run_moral_path_simulations(iterations)
    print(f"Estimated Moral Paths: {estimated_paths}")

    # Visualize results
    visualize_results(estimated_paths)

if __name__ == "__main__":
    main()
