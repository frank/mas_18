import random

class Player:

    total_players = 0

    # To add a strategy include the number + name in __init__,
    # Add any parameters if needed
    # Add a function for that strategy
    # Have the function run depending on self.strategy in move()

    def __init__(self, game):
        Player.total_players += 1
        Player.game = game
        self.id = Player.total_players
        # Stores all previous moves as a 2D array. First element of each tuple
        # in the array is always the subject player
        self.previous_moves = []
        self.previous_payoffs = []
        self.score = 0
        print("P" + str(self.id), "strategy?")
        print("\t(1)  Tit for tat")
        print("\t(2)  Retaliator")
        print("\t(3)  Cooperator")
        print("\t(4)  Betrayer")
        print("\t(5)  Random")
        print("\t(6)  Occasional betrayer")
        print("\t(7)  Tit for two tats")
        print("\t(8)  Kind tit for tat")
        print("\t(9)  Initial pessimist")
        print("\t(10) Pessimistic tit for tat")
        strat_input = input()
        self.strategy = strat_input
        # retaliator parameter
        self.revenge_mode = False

    def move(self):
        if self.strategy == '1':
            return self.tit_for_tat()
        elif self.strategy == '2':
            return self.retaliator()
        elif self.strategy == '3':
            return self.cooperator()
        elif self.strategy == '4':
            return self.betrayer()
        elif self.strategy == '5':
            return self.random()
        elif self.strategy == '6':
            return self.occasional_betrayer()
        elif self.strategy == '7':
            return self.tit_for_two_tats()
        elif self.strategy == '8':
            return self.kind_tit_for_tat()
        elif self.strategy == '9':
            return self.initial_pessimist()
        elif self.strategy == '10':
            return self.pessimistic_tit_for_tat()
        return 'goof'

    def tit_for_tat(self):
        if not self.previous_moves:
            return 'quiet'
        elif self.previous_payoffs[-1] < -11.5:
            return 'confess'
        return 'quiet'

    def retaliator(self):
        if not self.revenge_mode:
            return 'quiet'
        return 'confess'

    def cooperator(self):
        return 'quiet'

    def betrayer(self):
        return 'confess'

    def occasional_betrayer(self):
        if Player.game.get_n_plays() % 5 == 0 and Player.game.get_n_plays() != 0:
            return 'confess'
        return 'quiet'

    def random(self):
        if random.uniform(0, 1) > 0.5:
            return 'quiet'
        return 'confess'

    def tit_for_two_tats(self):
        if len(self.previous_moves) < 2:
            return 'quiet'
        if self.previous_payoffs[-1] < -11.5 and self.previous_payoffs[-2] < -11.5:
            return 'confess'
        return 'quiet'

    def kind_tit_for_tat(self):
        if not self.previous_moves:
            return 'quiet'
        elif self.previous_payoffs[-1] < -11.5:
            if random.uniform(0, 1) < 0.1:
                return 'quiet'
            return 'confess'
        return 'quiet'

    def initial_pessimist(self):
        if self.game.get_n_plays() == 0:
            return 'confess'
        return 'quiet'

    def pessimistic_tit_for_tat(self):
        if not self.previous_moves or self.previous_payoffs[-1] < -11.5:
            return 'confess'
        return 'quiet'

    def update(self, own_move, other_move, utility):
        self.previous_moves.append((own_move, other_move))
        if other_move == 'confess':
            self.revenge_mode = True
        self.score += utility
        self.previous_payoffs.append(utility)

    def get_score(self):
        return self.score

    def get_previous_moves(self):
        return self.previous_moves

    def get_previous_payoffs(self):
        return self.previous_payoffs
