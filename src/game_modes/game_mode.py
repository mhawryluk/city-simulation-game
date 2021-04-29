from abc import ABC, abstractmethod
from game_engine_tools.save_manager import SaveManager

class GameMode(ABC):
    def __init__(self, WINDOW, save: SaveManager):
        self.window = WINDOW
        self.save_manager = save

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle(self, event: SaveManager):
        pass