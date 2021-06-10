from os import chdir, path, getcwd, environ


def change_directory():
    if __file__ == 'main.py':
        chdir('..')
    else:
        dir_name = path.dirname(path.dirname(__file__))
        if dir_name != '':
            chdir(dir_name) 


def main():
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    from game_engine import GameEngine
    change_directory()
    game_engine = GameEngine()
    game_engine.run()


if __name__ == "__main__":
    main()
