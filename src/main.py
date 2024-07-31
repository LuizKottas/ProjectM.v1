import sys
import os
import numpy as np

# Ensure the correct path is added to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prisoners_dilemma import PrisonersDilemma
from src.coordination_game import CoordinationGame
from src.stag_hunt import StagHunt
from src.moral_path import MoralPath
from src.moral_dilemma import MoralDilemma

def main():
    # Initialize and run game theory models
    pd = PrisonersDilemma()
    pd_equilibria = pd.find_nash_equilibrium()
    print("Prisoner's Dilemma Nash Equilibria:", pd_equilibria)

    cg = CoordinationGame()
    cg_equilibria = cg.find_nash_equilibrium()
    print("Coordination Game Nash Equilibria:", cg_equilibria)

    sh = StagHunt()
    sh_equilibria = sh.find_nash_equilibrium()
    print("Stag Hunt Nash Equilibria:", sh_equilibria)

    md = MoralDilemma()
    md_equilibria = md.find_nash_equilibrium()
    print("Moral Dilemma Nash Equilibria:", md_equilibria)

    # Initialize and run moral path estimation
    parameters = np.array([1, 2, 3])  # Example parameters for the moral function
    g_values = np.array([0.5, 0.3, 0.2])  # Example input values

    moral_path_estimator = MoralPath(parameters)
    estimated_path = moral_path_estimator.estimate_moral_path(g_values)
    print("Estimated Moral Path:", estimated_path)

if __name__ == "__main__":
    main()
