import pygame as pg
import pygame_menu as pgmen


class Panel:
    def __init__(self, width, height, game_window):
        self.width = width
        self.height = height
        self.game_window = game_window

    def get_theme(self):
        theme = pgmen.themes.THEME_DARK.copy()
        theme.title = False
        theme.title_font = pgmen.font.FONT_FRANCHISE
        theme.title_font_size = 40
        theme.title_font_color = (230, 230, 230, 80)
        theme.background_color = (168, 218, 220, 200)
        theme.title_bar_style = pgmen.widgets.MENUBAR_STYLE_NONE
        theme.widget_font = pgmen.font.FONT_FRANCHISE
        theme.cursor_color = (200, 75, 100)
        theme.widget_font_size = 25
        theme.widget_font_color = (255, 255, 255)
        return theme

    def draw(self, window):
        if self.menu.is_enabled():
            self.menu.draw(window)

        for panel in self.get_subpanels():
            if panel is not None:
                panel.draw(window)

    def handle(self, event):
        """events handling function"""
        if self.menu.is_enabled():
            self.menu.update([event])

        for panel in self.get_subpanels():
            if panel:
                panel.handle(event)

    def is_enabled(self):
        return self.menu.is_enabled()

    def enable(self):
        self.menu.enable()

    def disable(self):
        self.menu.disable()
        for panel in self.get_subpanels():
            if panel:
                panel.disable()

    def collide(self):
        """returns True if the mouse is hovering above this tile"""
        if not self.menu.is_enabled():
            return False

        position = self.menu.get_position()
        mouse_pos = pg.mouse.get_pos()

        if position[0] < mouse_pos[0] < position[0] + self.menu.get_width() and position[1] <= mouse_pos[1] <= position[1] + self.menu.get_height():
            return True

        for panel in self.get_subpanels():
            if panel is None:
                continue
            if panel.collide():
                return True

        return False

    def get_subpanels(self):
        """returns all panels attached to this panel"""
        return []

    def disable_subpanels(self):
        """hides all children/deriving panels"""
        for panel in self.get_subpanels():
            panel.disable_all_panels()

    def disable_all_panels(self):
        """hides all panels including the one this function is called in and all of its children/deriving panels"""
        self.menu.disable()
        for panel in self.get_subpanels():
            if panel is not None:
                panel.disable_all_panels()

    def unselect_selected_widget(self):
        self.menu.get_selected_widget().select(False)
