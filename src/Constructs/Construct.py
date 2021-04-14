
class Construct:
    def __init__(self, construct_type):
        self.attributes = attributes.copy()
        self.construct_level = 0
        self.type = construct_type
        self.human_resources = 0
    
    def level_up(self, level_up_by):
        prev = self.construct_level
        self.construct_level = min(self.attributes['max_level'], self.construct_level + level_up_by)
        return self.construct_level - prev

    def delevel(self, delevel_by):
        prev = self.construct_level
        self.construct_level = max(0, self.construct_level - delevel_by)
        return prev - self.construct_level
