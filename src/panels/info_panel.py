import pygame_menu as pgmen
from panels.panel import Panel


class InfoPanel(Panel):
    def __init__(self, width, height, position, game_window, simulator):
        super().__init__(width, height, game_window)

        self.simulator = simulator

        # menu
        self.menu = pgmen.Menu('your city: ', width=width,
                               height=height, position=position,
                               theme=self.get_theme(),
                               )

        # info
        funds_label = self.menu.add.label('             funds')
        happiness_label = self.menu.add.label('         happiness')
        population_label = self.menu.add.label('        population')
        res_demand_label = self.menu.add.label('residential demand')
        comm_demand_label = self.menu.add.label(' commercial demand')
        indu_demand_label = self.menu.add.label(' industrial demand')

        funds_label.add_draw_callback(self.update_label('funds'))
        population_label.add_draw_callback(self.update_label('population'))
        happiness_label.add_draw_callback(self.update_label('resident_happyness'))
        res_demand_label.add_draw_callback(
            self.update_label('residential demand'))
        comm_demand_label.add_draw_callback(
            self.update_label('commercial demand'))
        indu_demand_label.add_draw_callback(
            self.update_label('industrail demand'))

        self.labels = [funds_label, happiness_label,
                       res_demand_label, comm_demand_label, indu_demand_label]

    def update_label(self, key):
        def update(widget, menu):
            text = widget.get_title().split(':')[0]
            widget.set_title(f'{text}: {self.simulator.get_data(key)}')
        return update

    def force_update_labels(self):
        for label in self.labels:
            label.apply_draw_callbacks()

    def get_theme(self):
        theme = super().get_theme()
        theme.widget_font_size = 20
        theme.widget_padding = 0
        theme.widget_margin = (-30, 0)
        theme.widget_alignment = pgmen.locals.ALIGN_RIGHT
        return theme
