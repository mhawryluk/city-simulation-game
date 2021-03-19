import pygame as pg

class GameEngine:
    def __init__(self):
        self.running = False
        self.status = None
        self.MEASUREMENTS = (1000, 600)
        self.WINDOW = pg.display.set_mode(self.MEASUREMENTS)

    def run(self):
        self.running = True

        while self.running:
            pg.display.update()
            for event in pg.event.get():
                self.handle(event)
                
             
    
    def handle(self, event):
        if event == pg.QUIT:
            self.running = False
            pg.quit()
        