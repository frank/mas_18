import sys
import matplotlib.pyplot as plt
from K_Armed_Bandit import K_Armed_Bandit
from E_Greedy import E_Greedy
from Optimistic_E_Greedy import Optimistic_E_Greedy
from UCB import UCB


def argument_error():
    print("Usage: python3 k_arms.py [k] [seed] [spread]")
    sys.exit()
    return

if __name__ == '__main__':

    ##############
    # PARAMETERS #
    ##############
    n = 7  # number of arms, 5 <= n <= 20
    seed = n  # seed for random generation
    spread = 4  # spread of the means assigned to the arms
    e = 0.05  # epsilon for the e-greedy agent
    start = 100  # starting initialization for the optimistic e-greedy agent
    c = 0.3  # width parameter for ucb
    ##############

    k_armed_bandit = K_Armed_Bandit(seed, n, spread)

    # Agents
    e_greedy = E_Greedy(n, k_armed_bandit, e)
    optimistic_e_greedy = Optimistic_E_Greedy(n, k_armed_bandit, e, start)
    ucb = UCB(n, k_armed_bandit, c)

    # Mean rewards
    e_greedy_mean_rewards = []
    optimistic_e_greedy_mean_rewards = []
    ucb_mean_rewards = []

    moves = 1000
    for i in range(moves):
        e_greedy_mean_rewards.append(e_greedy.play())
        optimistic_e_greedy_mean_rewards.append(optimistic_e_greedy.play())
        ucb_mean_rewards.append(ucb.play())

    # Plot
    plt.plot(e_greedy_mean_rewards, ',-')
    plt.plot(optimistic_e_greedy_mean_rewards, ',-')
    plt.plot(ucb_mean_rewards, ',-')
    plt.legend(['$\epsilon$-greedy', 'optimistic $\epsilon$-greedy', 'UCB'])
    plt.ylabel('Mean reward')
    plt.xlabel('Time')
    plt.title('Mean reward over time')
    plt.show()
