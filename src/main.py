from game_engine import GameEngine
from os import chdir, path, getcwd


def change_directory():
    if __file__ == 'main.py':
        chdir('..')
    else:
        chdir(path.dirname(path.dirname(__file__)))


def main():
    change_directory()
    game_engine = GameEngine()
    game_engine.run()


if __name__ == "__main__":
    print(__file__)
    main()
