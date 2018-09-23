from player import Player

class Game:

    def __init__(self):
        self.p_one = Player(self)
        self.p_two = Player(self)
        self.n_plays = 0

    def play(self):
        # player one and player two produce moves
        m_one, m_two = self.p_one.move(), self.p_two.move()
        # get the respective utilities
        u_one, u_two = self.get_utilities(m_one, m_two)
        self.p_one.update(m_one, m_two, u_one)
        self.p_two.update(m_two, m_one, u_two)
        self.n_plays += 1

    def get_utilities(self, m_one, m_two):
        if m_one == m_two == 'quiet':
            return -1, -1
        if m_one == m_two == 'confess':
            return -8, -8
        if m_one == 'quiet' and m_two == 'confess':
            return -12, 0
        if m_one == 'confess' and m_two == 'quiet':
            return 0, -12
        else:
            print("Error! Illegal moves:", m_one, m_two)
            return 0, 0

    def print_stats(self):
        print()
        print("Moves:")
        for i, move in enumerate(self.p_one.get_previous_moves()):
            nr = str(i + 1) + '. ' if i + 1 < 10 else str(i + 1) + '.'
            print(nr, move[0], "\t" , move[1])
        print()
        print("Scores:")
        print("Player 1:", self.p_one.get_score())
        print("Player 2:", self.p_two.get_score())

    def get_n_plays(self):
        if self.n_plays == None:
            return 0
        return self.n_plays
