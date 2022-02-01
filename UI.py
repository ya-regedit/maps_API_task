import pygame
import pygame_gui
from main import SIZE

pygame.init()
screen = pygame.display.set_mode(SIZE)
manager = pygame_gui.UIManager(SIZE)
menu = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(['map', 'sat', 'sat,skl'], 'map', pygame.Rect(0, 0, 60, 40),
                                                            manager)
