import numpy as np


class Arm:

    def __init__(self):
        self.mean = np.random.normal(0, 0.4)
        self.stdev = 1

    def pull(self):
        return np.random.normal(self.mean, self.stdev)

    def get_mean(self):
        return self.mean
