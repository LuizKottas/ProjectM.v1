class CoordinationGame:
    def __init__(self):
        self.matrix = {
            'optionA_optionA': (4, 4),
            'optionA_optionB': (0, 0),
            'optionB_optionA': (0, 0),
            'optionB_optionB': (3, 3)
        }

    def evaluate_choice(self, choice1, choice2):
        key = f"{choice1}_{choice2}"
        return self.matrix.get(key, (0, 0))

    def find_nash_equilibrium(self):
        choices = ['optionA', 'optionB']
        nash_equilibria = []
        
        for choice1 in choices:
            for choice2 in choices:
                payoff1, payoff2 = self.evaluate_choice(choice1, choice2)

                other1 = 'optionB' if choice1 == 'optionA' else 'optionA'
                other2 = 'optionB' if choice2 == 'optionA' else 'optionA'

                other_payoff1, _ = self.evaluate_choice(other1, choice2)
                _, other_payoff2 = self.evaluate_choice(choice1, other2)

                if payoff1 >= other_payoff1 and payoff2 >= other_payoff2:
                    nash_equilibria.append((choice1, choice2))
        
        return nash_equilibria

# Usage
if __name__ == "__main__":
    game = CoordinationGame()
    nash_equilibria = game.find_nash_equilibrium()
    print("Nash Equilibria:")
    for equilibrium in nash_equilibria:
        print(equilibrium)
