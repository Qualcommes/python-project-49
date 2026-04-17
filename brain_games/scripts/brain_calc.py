from brain_games.game_engine import game
from brain_games.games.calc_cli import brain_calc_game


def main():
    stack = brain_calc_game()
    game(stack)


if __name__ == "__main__":
    main()