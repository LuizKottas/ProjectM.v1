class PrisonersDilemma:
    def __init__(self):
        self.matrix = {
            'cooperate_cooperate': (3, 3),
            'cooperate_defect': (0, 5),
            'defect_cooperate': (5, 0),
            'defect_defect': (1, 1)
        }

    def evaluate_choice(self, choice1, choice2):
        key = f"{choice1}_{choice2}"
        return self.matrix.get(key, (0, 0))

    def find_nash_equilibrium(self):
        choices = ['cooperate', 'defect']
        nash_equilibria = []
        
        for choice1 in choices:
            for choice2 in choices:
                payoff1, payoff2 = self.evaluate_choice(choice1, choice2)

                other1 = 'defect' if choice1 == 'cooperate' else 'cooperate'
                other2 = 'defect' if choice2 == 'cooperate' else 'cooperate'

                other_payoff1, _ = self.evaluate_choice(other1, choice2)
                _, other_payoff2 = self.evaluate_choice(choice1, other2)

                if payoff1 >= other_payoff1 and payoff2 >= other_payoff2:
                    nash_equilibria.append((choice1, choice2))
        
        return nash_equilibria

# Usage
if __name__ == "__main__":
    dilemma = PrisonersDilemma()
    nash_equilibria = dilemma.find_nash_equilibrium()
    print("Nash Equilibria:")
    for equilibrium in nash_equilibria:
        print(equilibrium)
