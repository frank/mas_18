import numpy as np
from Agent import Agent


class UCB(Agent):

    def __init__(self, n, k_armed_bandit, c=1):
        Agent.__init__(self, n, k_armed_bandit)
        self.c = c
        self.k = np.array(self.k)
        self.q = np.array(self.q)

    def play(self):
        confidence_bounds = self.q + self.c * (np.log(self.t) / 2 * self.k)
        self.pull_arm(np.argmax(confidence_bounds))
        print(confidence_bounds)
