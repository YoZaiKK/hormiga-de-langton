from ant import Ant
import math
from random import randint as rint
import pygame
import numpy as np

running = True
pauseExect = True


def inicializar():
    # colors
    bg_color = 255, 255, 255
    width, height = 500, 500
    dimentionalCellWidth = 2
    screen = pygame.display.set_mode(
        (height*dimentionalCellWidth, width*dimentionalCellWidth))
    screen.fill(bg_color)
    # Inicializamos el mapa
    mapa = np.ones((width, height))
    hormigas, mapaHormigas = generarHormigas(width, height, screen) 
    animate(mapa, hormigas, mapaHormigas)


def event_handler(es):
    global running, pauseExect
    for e in es:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                pauseExect = True if not pauseExect else False 


def animate(mapa, hormigas, mapaHormigas):
    global running, pauseExect
    pygame.display.init()
    while running:
        event_handler(pygame.event.get())
        if not pauseExect: 
            for hormiga in hormigas:
                mapa, mapaHormigas = hormiga.run(mapa, mapaHormigas, hormigas) 
            pygame.display.update()


# def generarHormigas(width, height, screen):
def generarHormigas(width, height, screen):
    hormigas = []
    # Creamos una matriz llena de ceros, que luego usaremos para poner cosillas ahi
    mapaHormigas = [width*[0]] * height
    numHormigas = 100
    queens: int = int(numHormigas*.01)
    workers: int = int(numHormigas*.55)
    reps: int = int(numHormigas*.09)
    soldiers: int = int(numHormigas*.35)
    # Aqui lo que planeaba hacer es un for que nos recorra todas las instancias de nuestras hormigas, hacerlas y meterlas a nuestra lista llamada hormigas, luego hacer un return de la lista y dentro del while de nuestro mainloop, hacer un foreach de las hormigas
    for i in range(0, queens):
        x, y = colocarHormiga(width, mapaHormigas)
        nuevaHormiga = Ant(x, y, width, height, screen, 1)
        hormigas.append(nuevaHormiga)
        mapaHormigas[x][y] = (
            nuevaHormiga.edad, nuevaHormiga.mirandoHacia, nuevaHormiga.clase) 

    for i in range(0, workers):
        x, y = colocarHormiga(width, mapaHormigas)
        nuevaHormiga = Ant(x, y, width, height, screen, 2)
        hormigas.append(nuevaHormiga)
        mapaHormigas[x][y] = (
            nuevaHormiga.edad, nuevaHormiga.mirandoHacia, nuevaHormiga.clase)

    for i in range(0, reps):
        x, y = colocarHormiga(width, mapaHormigas)
        nuevaHormiga = Ant(x, y, width, height, screen, 3)
        hormigas.append(nuevaHormiga)
        mapaHormigas[x][y] = (
            nuevaHormiga.edad, nuevaHormiga.mirandoHacia, nuevaHormiga.clase)

    for i in range(0, soldiers):
        x, y = colocarHormiga(width, mapaHormigas)
        nuevaHormiga = Ant(x, y, width, height, screen, 4)
        hormigas.append(nuevaHormiga)
        mapaHormigas[x][y] = (
            nuevaHormiga.edad, nuevaHormiga.mirandoHacia, nuevaHormiga.clase) 
    print("Total de hormigas generados: {}".format(len(hormigas)))
    return hormigas, mapaHormigas


def colocarHormiga(width, mapaHormigas):
    # # Default area: The Whole map
    # x = rint(0, width-1)
    # y = rint(0, width-1)
    
    # User area, change values
    startArea = 0
    endAreaX = 300
    endAreaY = 300
    x = rint(startArea, endAreaX)
    y = rint(startArea, endAreaY)
    while(mapaHormigas[x][y] != 0): 
        x = rint(startArea, endAreaX)
        y = rint(startArea, endAreaY)
    return x, y
