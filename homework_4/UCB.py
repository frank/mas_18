import numpy as np
from Agent import Agent


class UCB(Agent):

    def __init__(self, n, k_armed_bandit, c=1):
        Agent.__init__(self, n, k_armed_bandit)
        self.c = c
        self.k = np.array(self.k)
        self.q = np.array(self.q)

    def play(self):
        confidence_bounds = []
        for a in range(self.n):
            if self.k[a] == 0:
                confidence_bounds.append(np.Inf)
            else:
                confidence_bounds.append(self.q[a] + self.c * np.sqrt(np.log(self.t) / 2 * self.k[a]))
        return self.pull_arm(np.argmax(confidence_bounds))

    def __str__(self):
        return "UCB"
