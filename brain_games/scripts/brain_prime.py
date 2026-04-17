from brain_games.game_engine import game
from brain_games.prime_cli import brain_prime_game


def main():
    stack = brain_prime_game()
    game(stack)


if __name__ == "__main__":
    main()