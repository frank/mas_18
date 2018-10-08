import sys
from K_Armed_Bandit import K_Armed_Bandit
from E_Greedy import E_Greedy
from Optimistic_E_Greedy import Optimistic_E_Greedy
from UCB import UCB


def argument_error():
    print("Usage: python3 k_arms.py [k] [seed] [spread]")
    sys.exit()
    return


if __name__ == '__main__':
    if len(sys.argv) > 4:
        argument_error()

    # Get number of arms and check for its value
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    if n < 5 or n > 20:
        print("Note: 5 <= k <= 20")
        sys.exit()

    # Set seed for the random generator
    seed = float(sys.argv[2]) if len(sys.argv) > 2 else 0

    # Set spread for the value distributions
    spread = float(sys.argv[3]) if len(sys.argv) > 3 else 2

    k_armed_bandit = K_Armed_Bandit(seed, n, spread)

    e = 0.1
    start = 100
    c = 1.0
    e_greedy = E_Greedy(n, k_armed_bandit, e)
    optimistic_e_greedy = Optimistic_E_Greedy(n, k_armed_bandit, e, start)
    ucb = UCB(n, k_armed_bandit, c)

    for i in range(5):
        ucb.play()
