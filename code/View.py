import pygame

class View:
    """
        Klasa View odpowiada za wizualizację planszy gry oraz rysowanie komórek i siatki.

        Główne zadania:
            - Rysowanie siatki (grid) o zadanej liczbie wierszy i kolumn
            - Wyświetlanie żywych komórek w odpowiednich miejscach
            - Obsługa zmiany koloru żywych komórek
            - Czyszczenie ekranu (wypełnianie tłem)

        Metody:
            - draw_grid: Rysuje siatkę o podanej liczbie kolumn i wierszy.
            - draw_cells: Rysuje żywe komórki na planszy na podstawie macierzy cells.
            - change_color: Umożliwia zmianę koloru żywych komórek.
            - clear: Czyści ekran, wypełniając go kolorem tła.
        """
    def __init__(self, screen, cell_size, grid_color, live_color, bg_color):
        self.screen = screen
        self.cell_size = cell_size
        self.grid_color = grid_color
        self.live_color = live_color
        self.bg_color = bg_color

    def draw_grid(self, cols, rows):
        for x in range(0, cols * self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, self.grid_color, (x, 0), (x, rows * self.cell_size))
        for y in range(0, rows * self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, self.grid_color, (0, y), (cols * self.cell_size, y))

    def draw_cells(self, cells):
        for row in range(len(cells)):
            for col in range(len(cells[0])):
                if cells[row][col]:
                    rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, self.live_color, rect)

    def change_color(self, live_color):
        self.live_color = live_color

    def clear(self):
        self.screen.fill(self.bg_color)
