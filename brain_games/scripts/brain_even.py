from brain_games.game_engine import game
from brain_games.games.even_cli import brain_even_game


def main():
    stack = brain_even_game()
    game(stack)


if __name__ == "__main__":
    main()