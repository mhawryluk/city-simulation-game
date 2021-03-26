from GameEngine import GameEngine

def main():
    game_engine = GameEngine()
    # game_engine.save_manager.load_save_manager_data()
    # game_engine.save_manager.create_save('mimimi')
    # game_engine.save_manager.create_save('foch')
    # game_engine.save_manager.create_save('fist')
    # game_engine.save_manager.create_save('gugu')
    # for i in range(1, 5):
    #     game_engine.save_manager.delete_save(1)
    game_engine.run()

if __name__ == "__main__":
    main()