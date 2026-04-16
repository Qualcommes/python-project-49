from brain_games.game_engine import game
from brain_games.gcd_cli import brain_gcd_game


def main():
    stack = brain_gcd_game()
    game(stack)


if __name__ == "__main__":
    main()