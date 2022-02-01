import pygame
import pygame_gui

SIZE = (600, 400)
pygame.init()
screen = pygame.display.set_mode(SIZE)
manager = pygame_gui.UIManager(SIZE)
menu = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(['map', 'sat', 'sat,skl'], 'map', pygame.Rect(0, 0, 80, 40),
                                                            manager)
