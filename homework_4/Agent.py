import numpy as np


class Agent:

    def __init__(self, n, k_armed_bandit):
        self.n = n
        self.k_armed_bandit = k_armed_bandit
        self.k = [0] * n
        self.q = [0] * n
        self.r = []
        self.t = 0

    def pull_arm(self, a):
        self.r.append(self.k_armed_bandit.pull_arm(a))
        self.k[a] += 1
        # Apply update function for the value expectation
        self.q[a] = self.q[a] + (self.r[self.t] - self.q[a]) / self.k[a]
        self.t += 1
        return np.mean(self.r)

    def print_all(self):
        print("k:", self.k)
        print("q:", self.q)
        print("m:", self.k_armed_bandit.get_means())
