class MoralDilemma:
    def __init__(self):
        self.matrix = {
            'good_good': (10, 10),
            'good_evil': (10, -10),
            'evil_good': (-10, 10),
            'evil_evil': (-10, -10)
        }

    def evaluate_choice(self, choice1, choice2):
        key = f"{choice1}_{choice2}"
        return self.matrix.get(key, (0, 0))

    def find_nash_equilibrium(self):
        choices = ['good', 'evil']
        nash_equilibria = []
        
        for choice1 in choices:
            for choice2 in choices:
                payoff1, payoff2 = self.evaluate_choice(choice1, choice2)

                other1 = 'evil' if choice1 == 'good' else 'good'
                other2 = 'evil' if choice2 == 'good' else 'good'

                # Evaluate the other choice for the first player while keeping the second player's choice the same
                other_payoff1, _ = self.evaluate_choice(other1, choice2)
                other_total_payoff1 = other_payoff1 + payoff2

                # Evaluate the other choice for the second player while keeping the first player's choice the same
                _, other_payoff2 = self.evaluate_choice(choice1, other2)
                other_total_payoff2 = payoff1 + other_payoff2

                # Check for Nash equilibrium conditions based on total payoffs
                if payoff1 + payoff2 >= other_total_payoff1 and payoff1 + payoff2 >= other_total_payoff2:
                    nash_equilibria.append((choice1, choice2))
        
        return nash_equilibria

# Usage
if __name__ == "__main__":
    dilemma = MoralDilemma()
    nash_equilibria = dilemma.find_nash_equilibrium()
    print("Nash Equilibria:")
    for equilibrium in nash_equilibria:
        print(equilibrium)

