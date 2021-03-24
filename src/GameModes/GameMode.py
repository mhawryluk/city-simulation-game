from abc import ABC, abstractmethod
from SaveManager import SaveManager

class GameMode(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle(self, event: SaveManager):
        pass
