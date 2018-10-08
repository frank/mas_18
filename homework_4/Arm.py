import numpy as np


class Arm:

    def __init__(self, seed, spread=2):
        np.random.seed(seed)
        self.mean = np.random.uniform(-spread, spread)
        self.stdev = 1

    def pull(self):
        return np.random.normal(self.mean, self.stdev)

    def get_mean(self):
        return self.mean
