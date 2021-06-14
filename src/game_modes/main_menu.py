from random import choice

import pygame as pg
import pygame_menu as pgmen

from game_engine_tools import load_asset, volume_up, volume_down
from game_engine_tools.save_manager import SaveManager
from game_modes.game_mode import GameMode


class MainMenu(GameMode):
    def __init__(self, window, save: SaveManager):
        super().__init__(window, save)
        self.change_mode = False

        self.menu = None
        self.save_menu = None
        self.settings_menu = None
        self.warning_menu = None

        self.play_button = None
        self.save_button = None
        self.settings_button = None
        self.quit_button = None

        backgrounds = ['menu_background1.jpg', 'menu_background3.png', 'menu_background4.jpg']

        self.background = load_asset('MenuBackgrounds', choice(backgrounds))
        self.background = pg.transform.scale(
            self.background, self.window.get_size())

        self.make_main_menu()

    def make_main_menu(self):
        width, height = self.window.get_size()

        self.menu = pgmen.Menu(title='City Simulation Game', width=width * 0.6, height=height * 0.85,
                               theme=self.get_theme(),
                               mouse_enabled=True, mouse_motion_selection=True)

        if self.save_manager.has_active_save():
            self.play_button = self.menu.add.button('Play', self.play)
            self.save_button = self.menu.add.button(
                'Choose save', self.change_save_menu_status)
        else:
            self.play_button = None
            self.save_button = self.menu.add.button(
                'Create save', self.change_save_menu_status)

        self.settings_button = self.menu.add.button(
            'Settings', self.change_settings_menu_status)
        self.quit_button = self.menu.add.button('Quit', self.quit_screen)

    def make_save_menu(self, width, height):
        self.save_menu = pgmen.Menu(title='Saves', width=width, height=height, theme=self.get_theme(),
                                    mouse_enabled=True, mouse_motion_selection=True)
        are_saves_active = self.save_manager.has_active_save()

        if are_saves_active:
            def switch_save(selected_value, *args, **kwargs):
                item, _ = selected_value
                id = int(item[1])
                self.save_manager.activate_save(id)

            items = self.save_manager.list_saves()
            self.save_menu.add.selector(
                title='Active save',
                items=items,
                onreturn=switch_save,
                onchange=switch_save
            )

            def delete_save():
                self.save_manager.delete_save()
                self.update(redraw=True)

            self.save_menu.add.button('Delete save', delete_save)

        def create_save():
            name = txt_input.get_value()
            if len(name) == 0:
                pass
            else:
                self.save_manager.create_save(name)
                self.update(redraw=True)

        txt_input = self.save_menu.add.text_input(
            title='New save name: ', default="new save")
        self.save_menu.add.button(
            'Create save', create_save)

        self.save_menu.add.button('Back', self.change_save_menu_status)

    def make_settings_menu(self, width, height):
        self.settings_menu = pgmen.Menu(title='Settings', width=width, height=height, theme=self.get_theme(),
                                        mouse_enabled=True, mouse_motion_selection=True)
        self.settings_menu.add.button('volume up', volume_up)
        self.settings_menu.add.button('volume down', volume_down)
        self.settings_menu.add.button('Back', self.change_settings_menu_status)

    def create_warning_menu(self, message, if_yes, if_no, parent_width, parent_height):
        theme = self.get_theme()
        theme.title_bar_style = pgmen.widgets.MENUBAR_STYLE_UNDERLINE
        warning = pgmen.Menu(title=message, width=parent_width, height=parent_height * 0.6, theme=theme,
                             mouse_enabled=True, mouse_motion_selection=True)
        warning.add.button('YES', if_yes)
        warning.add.button('NO', if_no)
        return warning

    def close_warning_menu(self):
        self.warning_menu = None

    def change_save_menu_status(self):
        if self.save_menu:
            self.save_menu = None
        else:
            width, height = self.window.get_size()
            self.make_save_menu(width, height)
        self.update(redraw=True)

    def change_settings_menu_status(self):
        if self.settings_menu:
            self.settings_menu = None
        else:
            width, height = self.window.get_size()
            self.make_settings_menu(width, height)

    def quit_screen(self):
        width, height = self.menu.get_size()
        self.warning_menu = self.create_warning_menu(
            'Do you really want to quit?', pgmen.events.PYGAME_QUIT, self.close_warning_menu, width, height)

    def play(self):
        self.change_mode = True
        self.save_manager.load_save()

    def update(self, redraw=False):
        self.draw(redraw)

    def handle(self, event):
        if self.warning_menu:
            self.warning_menu.update([event])
        elif self.save_menu:
            self.save_menu.update([event])
        elif self.settings_menu:
            self.settings_menu.update([event])
        else:
            self.menu.update([event])

        self.draw()

    def draw(self, redraw=False):
        self.window.blit(self.background, (0, 0))
        if self.save_menu:
            if redraw:
                width, height = self.save_menu.get_size()
                self.make_save_menu(width, height)
            self.save_menu.draw(self.window)
        elif self.settings_menu:
            if redraw:
                width, height = self.settings_menu.get_size()
                self.make_settings_menu(width, height)
            self.settings_menu.draw(self.window)
        else:
            if redraw:
                self.make_main_menu()
            self.menu.draw(self.window)

        if self.warning_menu:
            self.warning_menu.draw(self.window)

        pg.display.update()

    @staticmethod
    def get_theme():
        theme = pgmen.themes.THEME_DARK.copy()
        theme.title_font = pgmen.font.FONT_FRANCHISE
        theme.title_font_size = 70
        theme.title_background_color = (0, 0, 0)
        theme.title_font_color = (255, 255, 255)
        theme.title_bar_style = pgmen.widgets.MENUBAR_STYLE_NONE
        theme.background_color = (35, 35, 35, 60)
        theme.widget_font = pgmen.font.FONT_FRANCHISE
        theme.cursor_color = (200, 75, 100)
        theme.widget_border_width = 3
        theme.widget_background_color = (35, 35, 35)
        theme.widget_font_size = 44
        theme.widget_padding = 20
        theme.widget_alignment = pgmen.locals.ALIGN_CENTER
        return theme
