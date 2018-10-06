import Arm


class K_Armed_Bandit:

    def __init__(self, k=10):
        self.k = k
        self.arms = []
        for i in range(k):
            self.arms.append(Arm())

    def pull_arm(self, arm):
        return self.arms[arm].pull()
