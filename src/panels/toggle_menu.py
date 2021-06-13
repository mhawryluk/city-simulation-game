import pygame_menu as pgmen

from panels.panel import Panel


class ToggleMenu(Panel):
    """menu with the button that hides GameWindowPanel (the panel on the left)"""

    def __init__(self, width, height, position, game_window, panel):
        super().__init__(width, height, game_window)
        self.subpanel = panel
        self.menu = pgmen.Menu(
            title="toggle", theme=self.get_theme(), width=width, height=height, position=position)
        self.button = self.menu.add.button("show menu", self.toggle)

    def toggle(self):
        if self.subpanel.menu.is_enabled():
            self.button.select(False)
        else:
            self.button.select(True)

        self.subpanel.disable_subpanels()
        self.subpanel.unselect_selected_widget()
        self.subpanel.menu.toggle()
        self.game_window.info_panel.menu.toggle()
        self.game_window.speed_panel.menu.toggle()

    def get_theme(self):
        theme = super().get_theme()
        theme.background_color = (0, 0, 0, 0)
        theme.widget_font_size -= 2
        theme.widget_box_margin = (0, 0)
        return theme
