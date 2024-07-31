# ProjectM Overview

## Introduction

ProjectM explores the intersection of game theory and morality, demonstrating the optimal choice of morality and its application in programming.

## Fundamental Statements

1. There is life.
2. There is a path that sustains life (defined as good).
3. There is (are) path(s) that destroy life (defined as evil).

## Game Theory Framework

### Prisoner's Dilemma
- **Nash Equilibrium:** Both players defect.

### Coordination Game
- **Nash Equilibria:** Both players choose the same option (either Option A or Option B).

### Stag Hunt
- **Nash Equilibria:** Both players cooperate (stag) or both choose safety (hare).

### Moral Dilemma
- **Nash Equilibrium:** Both players choose good.

## Moral Path Estimation

The moral path estimation function combines a moral function \( M(g) \) with an error term \( e(g) \):
\[ \text{Estimated Moral Path} = M(g) + e(g) \]

- **Moral Function:** Linear function based on parameters.
- **Error Term:** Small random error to account for uncertainties.
