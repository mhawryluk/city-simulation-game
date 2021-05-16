import pygame_menu as pgmen
from panels.panel import Panel
from game_engine_tools import get_asset_path


class InfoPanel(Panel):
    def __init__(self, width, height, position, game_window, simulator):
        super().__init__(width, height, game_window)

        self.simulator = simulator

        # menu
        self.menu = pgmen.Menu('your city: ', width=width,
                               height=height, position=position,
                               theme=self.get_theme(), columns=2, rows=12
                               )

        # info
        self.menu.add.label('-------resources------')
        funds_label = self.menu.add.label('             funds')
        happiness_label = self.menu.add.label('         happiness')
        population_label = self.menu.add.label('        population')
        water_label = self.menu.add.label('      water supply')
        waste_label = self.menu.add.label('      waste piled up')
        power_label = self.menu.add.label('      power supply')
        pollution_label = self.menu.add.label('         pollution')

        self.menu.add.label('--------demand-------')
        res_demand_label = self.menu.add.label('residential')
        comm_demand_label = self.menu.add.label(' commercial')
        indu_demand_label = self.menu.add.label(' industrial')

        scale = (0.048, 0.048)
        self.menu.add.label('')
        self.menu.add.image(get_asset_path(
            'Icons', 'banknote.png'), scale=scale)
        self.menu.add.image(get_asset_path(
            'Icons', 'heart-inside.png'), scale=scale)
        self.menu.add.image(get_asset_path('Icons', 'person.png'), scale=scale)
        self.menu.add.image(get_asset_path('Icons', 'drop.png'), scale=scale)
        self.menu.add.image(get_asset_path(
            'Icons', 'trash-can.png'), scale=scale)
        self.menu.add.image(get_asset_path('Icons', 'plug.png'), scale=scale)
        self.menu.add.image(get_asset_path(
            'Icons', 'recycle.png'), scale=scale)

        self.menu.add.label('')
        self.menu.add.image(get_asset_path('Icons', 'house.png'), scale=scale)
        self.menu.add.image(get_asset_path('Icons', 'shop.png'), scale=scale)
        self.menu.add.image(get_asset_path(
            'Icons', 'factory.png'), scale=scale)

        funds_label.add_draw_callback(self.update_label('funds'))
        population_label.add_draw_callback(self.update_label('population'))
        happiness_label.add_draw_callback(
            self.update_label('resident_happyness'))

        res_demand_label.add_draw_callback(
            self.update_label('residential demand'))
        comm_demand_label.add_draw_callback(
            self.update_label('commercial demand'))
        indu_demand_label.add_draw_callback(
            self.update_label('industrial demand'))
        water_label.add_draw_callback(
            self.update_label('water'))
        waste_label.add_draw_callback(
            self.update_label('waste'))
        power_label.add_draw_callback(
            self.update_label('power'))
        pollution_label.add_draw_callback(
            self.update_label('pollution'))

        self.labels = [funds_label, happiness_label,
                       res_demand_label, comm_demand_label, indu_demand_label,
                       water_label, waste_label, power_label, pollution_label]

    def update_label(self, key):
        def update(widget, menu):
            text = widget.get_title().split(':')[0]
            if text.strip() == 'happiness':
                widget.set_title(
                    f'happiness: {self.simulator.get_data(key):.1%}')
            else:
                widget.set_title(f'{text}: {self.simulator.get_data(key)}')
        return update

    def force_update_labels(self):
        for label in self.labels:
            label.apply_draw_callbacks()

    def get_theme(self):
        theme = super().get_theme()
        theme.widget_padding = 2
        theme.widget_margin = (-10, 0)
        theme.widget_alignment = pgmen.locals.ALIGN_RIGHT
        return theme
