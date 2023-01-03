from ant import Ant
import math
import pygame
import numpy as np

running = True
pauseExect = True


def inicializar():
    # colors
    cell_color = 0, 0, 0
    bg_color = 255, 255, 255
    width, height = 500, 500
    screen = pygame.display.set_mode((height, width))
    screen.fill(bg_color)
    # Inicializamos el mapa
    mapa = np.ones((width, height))
    # inicializacion de la hormiga
    hormiga = Ant(50, 50, width, height, screen)
    animate(hormiga, mapa)


def event_handler(es):
    global running, pauseExect
    for e in es:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                pauseExect = True if not pauseExect else False
        # Get cursor pos and draw


def animate(hormiga, mapa):
    global running, pauseExect
    pygame.display.init()
    while running:
        event_handler(pygame.event.get())
        if not pauseExect:
            mapa = hormiga.run(mapa)
            pygame.display.update()
