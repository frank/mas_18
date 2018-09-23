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
        self.score = 0
        print("P" + str(self.id), "strategy?")
        print("\t(1) Tit for tat")
        print("\t(2) Retaliator")
        print("\t(3) Cooperator")
        print("\t(4) Betrayer")
        print("\t(5) Random")
        print("\t(6) Occasional betrayer")
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
        return 'goof'

    def tit_for_tat(self):
        if not self.previous_moves:
            return 'quiet'
        elif self.previous_moves[-1][1] == 'confess':
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

    def update(self, own_move, other_move, utility):
        self.previous_moves.append((own_move, other_move))
        if other_move == 'confess':
            self.revenge_mode = True
        self.score += utility

    def get_score(self):
        return self.score

    def get_previous_moves(self):
        return self.previous_moves
