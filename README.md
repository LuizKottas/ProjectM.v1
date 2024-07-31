#ProjectM: ProjectM is designed to explore the intersection of game theory and morality, demonstrating the optimal choice of morality and its application in programming. 

![License](https://img.shields.io/badge/license-MIT-blue.svg)

A project exploring the intersection of game theory and morality.

## Table of Contents
- [Introduction](#introduction)
- [Structure](#structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to use game theory to demonstrate the optimal choice of morality and its application in programming.

## Structure

- `docs/`: Documentation files
- `src/`: Source code for the project
    - `game_theory.py`: Implementation of the game theory model
    - `moral_path.py`: Implementation of the moral path estimation
    - `simulation.py`: Code to run simulations and analyze results
    - `utils.py`: Utility functions
- `tests/`: Unit tests for the project
    - `test_game_theory.py`: Unit tests for game_theory.py
    - `test_moral_path.py`: Unit tests for moral_path.py
    - `test_simulation.py`: Unit tests for simulation.py

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ProjectM.git
    cd ProjectM
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the game theory simulation:
```bash
python src/simulation.py