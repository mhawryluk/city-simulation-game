import pygame_menu as pgmen

from city_graphics.city_images import CityImages
from panels.panel import Panel


class InfoPanel(Panel):
    ICON_SCALE = (0.048, 0.048)
    city_images = CityImages()

    def __init__(self, width, height, position, game_window, simulator):
        super().__init__(width, height, game_window)

        self.simulator = simulator

        # menu
        self.menu = pgmen.Menu('your city: ', width=width,
                               height=height, position=position,
                               theme=self.get_theme(), columns=2, rows=12)

        # info
        self.menu.add.label('---- r e s o u r c e s ----')
        funds_label = self.menu.add.label('             funds')
        happiness_label = self.menu.add.label('         happiness')
        population_label = self.menu.add.label('        population')
        water_label = self.menu.add.label('      water supply')
        waste_label = self.menu.add.label('      waste piled up')
        power_label = self.menu.add.label('      power supply')

        self.menu.add.label('')
        self.menu.add.label('----- d e m a n d -----')
        res_demand_label = self.menu.add.label('residential')
        comm_demand_label = self.menu.add.label(' commercial')
        indu_demand_label = self.menu.add.label(' industrial')

        self.menu.add.label('')

        self.images = {
            'funds': (self.menu.add.image(self.city_images.get_icon('banknote'), scale=self.ICON_SCALE), 'banknote'),
            'resident_happyness': (self.menu.add.image(self.city_images.get_icon('heart-inside'), scale=self.ICON_SCALE), 'heart-inside'),
            'population': (self.menu.add.image(self.city_images.get_icon('person'), scale=self.ICON_SCALE), 'person'),
            'water': (self.menu.add.image(self.city_images.get_icon('drop'), scale=self.ICON_SCALE), 'drop'),
            'waste': (self.menu.add.image(self.city_images.get_icon(
                'trash-can'), scale=self.ICON_SCALE), 'trash-can'),
            'power': (self.menu.add.image(self.city_images.get_icon(
                'plug'), scale=self.ICON_SCALE), 'plug')
        }

        self.menu.add.label('')
        self.menu.add.label('')
        self.images['residential demand'] = (self.menu.add.image(self.city_images.get_icon(
            'house'), scale=self.ICON_SCALE), 'house')
        self.images['commercial demand'] = (self.menu.add.image(self.city_images.get_icon(
            'shop'), scale=self.ICON_SCALE), 'shop')
        self.images['industrial demand'] = (self.menu.add.image(self.city_images.get_icon(
            'factory'), scale=self.ICON_SCALE), 'factory')

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

        self.labels = [funds_label, happiness_label,
                       res_demand_label, comm_demand_label, indu_demand_label,
                       water_label, waste_label, power_label]

        for image in self.images.values():
            image[0].red = False

    def update_label(self, key):
        def update(widget, menu):
            text = widget.get_title().split(':')[0]
            value = self.simulator.get_data(key)

            if text.strip() == 'happiness':
                widget.set_title(
                    f'happiness: {value:.1%}')
            else:
                widget.set_title(f'{text}: {value}')

            image, image_key = self.images[key]
            if isinstance(value, str):
                if value == 'Very high' and not image.red:
                    image.red = True
                    image.set_image(pgmen.baseimage.BaseImage(
                        self.city_images.get_warning_icon(image_key)).scale(*self.ICON_SCALE))
                elif value != 'Very high' and image.red:
                    image.red = False
                    image.set_image(pgmen.baseimage.BaseImage(
                        self.city_images.get_icon(image_key)).scale(*self.ICON_SCALE))

            elif value < 0.1 and text.strip() != 'pollution' and not image.red:
                image.red = True
                image.set_image(pgmen.baseimage.BaseImage(
                    self.city_images.get_warning_icon(image_key)).scale(*self.ICON_SCALE))
            elif value >= 0.1 and image.red:
                image.red = False
                image.set_image(pgmen.baseimage.BaseImage(
                    self.city_images.get_icon(image_key)).scale(*self.ICON_SCALE))

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
