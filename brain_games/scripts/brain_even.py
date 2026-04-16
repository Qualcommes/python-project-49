from brain_games.even_cli import brain_even_game
from brain_games.game_engine import game


def main():
    stack = brain_even_game()
    game(stack)


if __name__ == "__main__":
    main()