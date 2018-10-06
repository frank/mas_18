import sys

import K_Armed_Bandit


def argument_error():
    print("Usage: python3 k_arms.py [k]")
    sys.exit()
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        argument_error()

    # Get number of arms and check for its value
    k = int(sys.argv[1])
    if k < 5 or k > 20:
        print("Note: 5 <= k <= 20")
        sys.exit()

    k_armed_bandit = K_Armed_Bandit(k)

    # Now for each strategy run N epochs and store the average reward
