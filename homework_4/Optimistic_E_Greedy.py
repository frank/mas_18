from E_Greedy import E_Greedy


class Optimistic_E_Greedy(E_Greedy):

    def __init__(self, n, k_armed_bandit, e=0.1, start=100):
        E_Greedy.__init__(self, n, k_armed_bandit, e)
        self.q = [1000] * n

    def __str__(self):
        return "Optimistic E-Greedy"
