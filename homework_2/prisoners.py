import random
from game import Game

def main():
    game = Game()
    while game.get_n_plays() < 20: # game loop
        game.play()
    game.print_stats()

if __name__ == '__main__':
    main()
