from brain_games.game_engine import game
from brain_games.games.progression_cli import brain_progression_game


def main():
    stack = brain_progression_game()
    game(stack)


if __name__ == "__main__":
    main()