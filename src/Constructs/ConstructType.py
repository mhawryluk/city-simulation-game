from enum import Enum, auto

class ConstantType(Enum):
    HOSPITAL = auto()
    HOUSE = auto()

    def get_info(self, type):
        pass

    def new_object(self, type) -> Construct:
        pass








