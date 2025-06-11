"""
Plik Main.py - uruchamia symulację gry w życie Conwaya.
Zawiera kod inicjalizujący widok, planszę, menedżera i główną pętlę programu.
"""

import pygame
import pygame_gui

from View import View
from StatisticsWindow import StatisticsWindow
from GameController import GameController
from GameOfLife import GameOfLife


cellSize = 20
gridCols, gridRows = 40, 40
window_Width = gridCols * cellSize
window_Height = gridRows * cellSize

pygame.init()
screen = pygame.display.set_mode((window_Width, window_Height))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((window_Width, window_Height))

game = GameOfLife(gridRows, gridCols)
view = View(screen, cellSize, (0, 0, 0), (255, 255, 0), (255, 255, 255))
stats_window = StatisticsWindow(manager, window_Width, window_Height)
controller = GameController(game, view, stats_window, manager, clock)

if __name__ == "__main__":
    controller.run()
