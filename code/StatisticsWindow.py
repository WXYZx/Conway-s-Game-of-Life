import pygame
import pygame_gui

class StatisticsWindow:
    """
        Klasa zawiera informację o wyglądzie oraz co wyświetla okienko statystyk.

        Okienko pokazuje aktualną liczbę narodzin (Births) oraz zgonów (Deaths)
        w symulacji Game of Life.

        Metody:
            - show: Wyświetla okno ze statystykami.
            - handle_event: Obsługuje zamknięcie okna statystyk.
    """
    def __init__(self, manager, window_width, window_height):
        self.manager = manager
        self.window_width = window_width
        self.window_height = window_height
        self.window = None

    def show(self, births, deaths):
        message = (f"<b>Births:</b> {births}"
                   f"<br><b>Deaths:</b> {deaths}")
        if self.window is not None:
            self.window.kill()
        self.window = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((self.window_width // 2 - 150, self.window_height // 2 - 60), (300, 120)),
            html_message=message,
            manager=self.manager,
            window_title='Generation statistics'
        )

    def handle_event(self, event):
        if self.window is not None and event.type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == self.window:
                self.window = None
