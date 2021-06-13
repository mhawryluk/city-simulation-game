from city import VERTICAL, HORIZONTAL


class RoadSystem:
    def __init__(self, save_source=None):

        # roads in sets of tuples divided according to their directions:
        self.vertical = set()
        self.horizontal = set()

        # mouse hovering
        self.hovered_road = None
        self.hovered_direction = VERTICAL

        self.changes = False  # whether roads were recently modified (for rebuilding the graph)

        # reading from save file
        if save_source is not None:
            for road in save_source['vertical']:
                self.vertical.add(tuple(road))
            for road in save_source['horizontal']:
                self.horizontal.add(tuple(road))

    def remove_road(self, direction, pos):
        self.changes = True
        if direction == VERTICAL:
            self.vertical.remove(pos)
        elif direction == HORIZONTAL:
            self.horizontal.remove(pos)

    def add_road(self, direction, pos):
        self.changes = True
        if direction == VERTICAL:
            self.vertical.add(pos)
        elif direction == HORIZONTAL:
            self.horizontal.add(pos)

    def has_road(self, x, y, vertical):
        if vertical == VERTICAL:
            return (x, y) in self.vertical
        elif vertical == HORIZONTAL:
            return (x, y) in self.horizontal

    def get_road_count(self):
        return len(self.vertical) + len(self.horizontal)

    def road_clicked(self):
        if self.hovered_road is None:
            return
        if self.hovered_direction == VERTICAL and self.hovered_road in self.vertical:
            self.remove_road(VERTICAL, self.hovered_road)
        elif self.hovered_direction == HORIZONTAL and self.hovered_road in self.horizontal:
            self.remove_road(HORIZONTAL, self.hovered_road)
        else:
            self.add_road(self.hovered_direction, self.hovered_road)

    def hovered(self, road):
        if self.hovered_direction == VERTICAL:
            round_x, round_y = round, int
        else:
            round_x, round_y = int, round
        if road is not None:
            x, y = road
            self.hovered_road = round_x(x), round_y(y)
        else:
            self.hovered_road = None

    def compress2save(self):
        return {
            'vertical': list(self.vertical),
            'horizontal': list(self.horizontal)
        }
