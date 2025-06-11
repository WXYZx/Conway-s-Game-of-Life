import pygame
import time
import random

class GameController:
    """
        GameController zarządza główną pętlą gry, obsługą zdarzeń użytkownika oraz synchronizacją widoku, logiki gry i GUI.

        Odpowiada za:
            - Przetwarzanie zdarzeń wejściowych (klawiatura, mysz)
            - Aktualizację i rysowanie planszy gry (poprzez View)
            - Zarządzanie stanem symulacji (start/stop/reset, pokolenia)
            - Wyświetlanie statystyk (przez StatisticsWindow)

        Obsługiwane klawisze:

        +----------+---------------------------------------------------------------+
        | Klawisz  | Działanie                                                     |
        +==========+===============================================================+
        | Enter    | Start symulacji, zeruje liczniki narodzin i śmierci           |
        +----------+---------------------------------------------------------------+
        | R        | Resetuje planszę do pustej                                    |
        +----------+---------------------------------------------------------------+
        | Space    | Wyświetla okno statystyk                                      |
        +----------+---------------------------------------------------------------+
        | C        | Zmienia kolor żywych komórek na losowy                        |
        +----------+---------------------------------------------------------------+
        | Escape   | Zamyka grę                                                    |
        +----------+---------------------------------------------------------------+

        Metody:
            - handle_event: Obsługuje pojedyncze zdarzenie Pygame (mysz, klawiatura, zamykanie okienek GUI)
            - run: Główna pętla gry, wywołuje rysowanie oraz obsługę zdarzeń i aktualizację generacji

    """
    def __init__(self, game, view, stats_window, manager, clock, interval=0.2):
        self.game = game
        self.view = view
        self.stats_window = stats_window
        self.manager = manager
        self.clock = clock
        self.interval = interval
        self.simulation_running = False
        self.drawing = False
        self.running = True
        self.last_generation = time.time()

    def handle_event(self, event):
        if self.stats_window.window is not None:
            self.manager.process_events(event)
            self.stats_window.handle_event(event)
            return

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.drawing = True
            mouseX, mouseY = event.pos
            col = mouseX // self.view.cell_size
            row = mouseY // self.view.cell_size
            if 0 <= col < self.game.cols and 0 <= row < self.game.rows:
                self.game.cells[row][col] = not self.game.cells[row][col]

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.drawing = False

        elif event.type == pygame.MOUSEMOTION and self.drawing:
            mouseX, mouseY = event.pos
            col = mouseX // self.view.cell_size
            row = mouseY // self.view.cell_size
            if 0 <= col < self.game.cols and 0 <= row < self.game.rows:
                self.game.cells[row][col] = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.drawing = False
                self.simulation_running = not self.simulation_running
                self.game.total_deaths = 0
                self.game.total_births = 0
            elif event.key == pygame.K_r:
                self.simulation_running = False
                self.game.reset()
            elif event.key == pygame.K_SPACE:
                self.stats_window.show(self.game.total_births, self.game.total_deaths)

            elif event.key == pygame.K_c:
                color = [
                    random.randint(0,255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                ]
                self.view.change_color(color)

            self.manager.process_events(event)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            if self.simulation_running:
                current_time = time.time()
                if current_time - self.last_generation >= self.interval:
                    self.game.new_generation()
                    self.last_generation = current_time

            self.view.clear()
            self.view.draw_grid(self.game.cols, self.game.rows)
            self.view.draw_cells(self.game.cells)
            self.manager.update(self.clock.get_time() / 1000.0)
            self.manager.draw_ui(self.view.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
