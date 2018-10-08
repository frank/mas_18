from Arm import Arm


class K_Armed_Bandit:

    def __init__(self, seed=0, n=10, spread=2):
        self.n = n
        self.spread = spread
        self.arms = []
        for s in range(n):
            self.arms.append(Arm(seed + s, spread))

    def pull_arm(self, arm):
        return self.arms[arm].pull()

    def get_means(self):
        return [arm.get_mean() for arm in self.arms]
