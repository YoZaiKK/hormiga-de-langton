import pygame
from random import randint as rint


class Ant:
    def __init__(self, x, y, mapX, mapY, screen, clase):
        # 0,1,2,3 : arriba, derecha, abajo, izquierda
        self.mirandoHacia = rint(0, 3)
        self.edad = 0
        self.color = (255, 0, 0)
        self.color_negro = (0, 0, 0)
        self.color_blanco = (255, 255, 255)
        self.x, self.y = x, y
        self.dimMapa = [mapX, mapY]
        self.screen = screen
        self.clase = clase
        self.dimention_cell_width = 2
        self.dimention_cell_height = 2
        # print("mapX={}, mapY={}".format(mapX, mapY))
        # each square
        self.polygon = [
            (x*self.dimention_cell_width, y*self.dimention_cell_width),
            ((x+1)*self.dimention_cell_width, y*self.dimention_cell_width),
            ((x+1)*self.dimention_cell_width, (y+1)*self.dimention_cell_width),
            (x*self.dimention_cell_width, (y+1)*self.dimention_cell_width)
        ]

    def actualizarPoligono(self):
        self.polygon = [
            (self.x*self.dimention_cell_width, self.y*self.dimention_cell_width),
            ((self.x+1)*self.dimention_cell_width,
             self.y*self.dimention_cell_width),
            ((self.x+1)*self.dimention_cell_width,
             (self.y+1)*self.dimention_cell_width),
            (self.x*self.dimention_cell_width, (self.y+1)*self.dimention_cell_width)
        ]

    def run(self, mapa, mapaHormigas, hormigas):
        # '''La hormiga mira hacia otro lado, dependiendo del color de la casilla sobre la que está parada'''
        # Su edad avanza con cada iteracion/llamada del metodo
        self.edad += 1
        self.mapaHormigas = mapaHormigas
        # Toggle del color/valor de la celda actual
        self.mapa = mapa
        if self.mapa[self.x][self.y] == 1:
            self.mapa[self.x][self.y] = 0  # cambiamos a cero el valor
            self.mirandoHacia = (self.mirandoHacia - 1) % 4
        else:
            self.mapa[self.x][self.y] = 1
            self.mirandoHacia = (self.mirandoHacia + 1) % 4

        # if not self.chocaConAlguien():
        #     self.moverse()
        # else:
        #     # mira hacia otro lado
        #     self.mirandoHacia = rint(0, 3)
        #     if not self.chocaConAlguien(): 
        #         self.moverse()
        # print(mapaHormigas)
        self.moverse()
        return self.mapa, self.mapaHormigas

    def moverse(self):
        self.mapaHormigas[self.x][self.y] = 0
        # '''La hormiga avanza en la direccion en la que está mirando, pinta la casilla anterior y la nueva, a la que se movio'''
        celdaQueCambia = self.polygon
        colorPorPintar = self.mapa[self.x][self.y]
        # movemos a la hormiga un piexel en la direccion que esta mirando
        # Arriba
        if self.mirandoHacia == 0:
            self.y = (self.y - 1) % self.dimMapa[0]
        # derecha
        if self.mirandoHacia == 1:
            self.x = (self.x + 1) % self.dimMapa[0]
        # abajo
        if self.mirandoHacia == 2:
            self.y = (self.y + 1) % self.dimMapa[0]
        # izquierda
        if self.mirandoHacia == 3:
            self.x = (self.x - 1) % self.dimMapa[0]

        # self.mapaHormigas[self.x][self.y] = (
        #     self.edad, self.mirandoHacia, self.clase)

        self.actualizarPoligono()
        # pintamos la celda en la que se encuentra la hormiga
        self.dibujarse(self.polygon, self.color)
        # lo pintamos del color contrario al que está
        self.dibujarse(
            celdaQueCambia,
            # # Togle to only see the ants
            # self.color_blanco
            # Togle to see the b/w map
            self.color_negro
            if colorPorPintar == 0
            else self.color_blanco
        )

        self.mapaHormigas[self.x][self.y] = (
            self.edad, self.mirandoHacia, self.clase)

    def dibujarse(self, poligono, color):
        # '''Se dibuja un cuadrado en el mapa'''
        pygame.draw.polygon(self.screen, color, poligono, 0)

    def hayHormigasReinaAlrededor(self):
        pass

    def chocaConAlguien(self):
        # Si lo que esta en la proxima celda es diferene de cero, esá ocupada, enonces si choca
        if self.mirandoHacia == 0:
            return self.mapaHormigas[self.x][(self.y-1) % self.dimMapa[0]] != 0
        elif self.mirandoHacia == 1:
            return self.mapaHormigas[(self.x+1) % self.dimMapa[0]][self.y] != 0
        elif self.mirandoHacia == 2:
            return self.mapaHormigas[self.x][(self.y+1) % self.dimMapa[0]] != 0
        else:
            return self.mapaHormigas[(self.x-1) % self.dimMapa[0]][self.y] != 0


# # Hay q hacer una funcion para hacer clases de manera aleatoria
# newBorn = Ant(self.x, self.y, self.mapX, self.mapY, self.screen, 1)
# return newBorn, False
'''
podemos hacer que la hormiga sea quien pinta cada cuadrito unicamente si lo cambia
entonces no tendriamos que refrescar toda la pantalla en cada iteracion

el tablero tendra una matriz de estados a la que todas las hormigas tendran acceso pa saber el estado del piso en ese momento

'''
# cell_color = 255, 255, 255
# si el numero aleatorio está dentro de un rango será un tipo de hormiga
# hormiga = ant(2, 2)
# print(hormiga.coordenadas)
