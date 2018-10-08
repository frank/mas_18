import numpy as np
import random
from Agent import Agent


class E_Greedy(Agent):

    def __init__(self, n, k_armed_bandit, e=0.1):
        Agent.__init__(self, n, k_armed_bandit)
        self.n = n
        self.e = e
        np.random.seed(2)
        random.seed(2)

    def play(self):
        if np.random.uniform(0, 1) < self.e:
            self.pull_arm(random.randrange(self.n))
            return
        self.pull_greedy()
