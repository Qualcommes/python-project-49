from brain_games.calc_cli import brain_calc_game
from brain_games.game_engine import game


def main():
    stack = brain_calc_game()
    game(stack)


if __name__ == "__main__":
    main()