import pygame as pg

class GameEngine:
    def __init__(self):
        self.running = False

        self.MEASUREMENTS = (1000, 600)
        self.WINDOW = pg.display.set_mode(self.MEASUREMENTS)
        self.FPS = 60
        self.clock = pg.time.Clock()
        #self.save = SaveManager()

        self.game_mode = MainMenu(self.WINDOW)

    def run(self):
        self.running = True
        

        while self.running:
            self.clock.tick(self.FPS)
            pg.display.update()
            self.game_mode.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                else:
                    self.game_mode.handle(event)

                    if self.game_mode.change_mode:
                        self.change_mode()

    def change_mode(self):
        pass


class SaveManager:
    def __init__(self):
        pass

