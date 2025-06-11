class GameOfLife:
    """
       Klasa realizująca logikę symulacji gry w życie Conwaya ("Game of Life").

       Odpowiada za:
           - Przechowywanie stanu planszy (macierz komórek)
           - Obliczanie liczby żywych sąsiadów dla każdej komórki
           - Generowanie kolejnych pokoleń zgodnie z zasadami gry
           - Zliczanie narodzin i zgonów w trakcie symulacji
           - Resetowanie planszy do stanu początkowego

       Metody:
           - reset(): Czyści planszę i zeruje liczniki.
           - count_neighbors: Zwraca liczbę żywych sąsiadów komórki.
           - new_generation: Oblicza i zapisuje kolejną generację planszy, aktualizuje liczniki narodzin i zgonów.
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.reset()
        self.total_births = 0
        self.total_deaths = 0

    def reset(self):
        self.cells = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.total_births = 0
        self.total_deaths = 0

    def count_neighbors(self, x, y):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                xi = (x + i) % self.rows
                yj = (y + j) % self.cols
                count += self.cells[xi][yj]
        return count

    def new_generation(self):
        births = 0
        deaths = 0
        new_cells = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.count_neighbors(row, col)
                alive = self.cells[row][col]
                if alive:
                    if neighbors in [2, 3]:
                        new_cells[row][col] = True
                    else:
                        deaths += 1
                else:
                    if neighbors == 3:
                        new_cells[row][col] = True
                        births += 1
        self.total_births += births
        self.total_deaths += deaths
        self.cells = new_cells