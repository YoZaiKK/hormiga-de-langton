from ant import Ant
import math
import pygame
import numpy as np

running = True
pauseExect = True


def inicializar():
    # colors
    bg_color = 255, 255, 255
    width, height = 500, 500
    screen = pygame.display.set_mode((height, width))
    screen.fill(bg_color)
    # Inicializamos el mapa
    mapa = np.ones((width, height))
    # inicializacion de la hormiga
    hormiga = Ant(50, 50, width, height, screen, 1)
    hormiga2 = Ant(60, 10, width, height, screen, 1)
    hormiga3 = Ant(100, 10, width, height, screen, 1)
    animate(hormiga, mapa, hormiga2, hormiga3)


def event_handler(es):
    global running, pauseExect
    for e in es:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                pauseExect = True if not pauseExect else False
        # Get cursor pos and draw


def animate(hormiga, mapa, hormiga2, hormiga3):
    global running, pauseExect 
    pygame.display.init()
    while running:
        event_handler(pygame.event.get())
        if not pauseExect:
            # mapa = hormiga.run(mapa)
            # mapa = hormiga2.run(mapa)
            mapa = hormiga3.run(mapa)
            pygame.display.update()


# def generarHormigas(width, height, screen):
def generarHormigas():
    hormigas = []
    numHormigas = 100
    queens: int = int(numHormigas*.01)
    workers: int = int(numHormigas*.55)
    reps: int =int(numHormigas*.09)
    soldiers: int = int(numHormigas*.35) 
    # Aqui lo que planeaba hacer es un for que nos recorra todas las instancias de nuestras hormigas, hacerlas y meterlas a nuestra lista llamada hormigas, luego hacer un return de la lista y dentro del while de nuestro mainloop, hacer un foreach de las hormigas
    # '''Hay que checar que ocurre si agregas numeros a algo que estas recorriendo, si se sigue o si se queda ahi''' '''SI'''
    for i in range(0,queens):
        print(i)
    for i in range(0,workers):
        print(i)
    for i in range(0,reps):
        print(i)
    for i in range(0,soldiers):
        print(i)
    # Prueva de si se agrega algo a una lista igual lo recorre y sip
    # numerosTest = [1,2,3,4]
    # for i in numerosTest:
    #     print(i)
    #     if(i == 2): 
    #         numerosTest.append(6)
    pass
