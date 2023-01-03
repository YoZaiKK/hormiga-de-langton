import pygame


class Ant:
    def __init__(self, x, y, mapX, mapY, screen):
        # 0,1,2,3 : arriba, derecha, abajo, izquierda
        self.mirandoHacia = 0
        self.edad = 0
        self.color = (255, 0, 0)
        self.color_negro = (0, 0, 0)
        self.color_blanco = (255, 255, 255)
        self.x, self.y = x, y
        self.dimMapa = [mapX, mapY]
        self.screen = screen
        self.dimention_cell_width = 1
        self.dimention_cell_height = 1
        print("mapX={}, mapY={}".format(mapX, mapY))
        # each square
        self.polygon = [
            (x, y),
            (x+1, y),
            (x+1, y+1),
            (x, y+1)
        ]

    def actualizarPoligono(self):
        self.polygon = [
            (self.x, self.y),
            (self.x+1, self.y),
            (self.x+1, self.y+1),
            (self.x, self.y+1)
        ]

    def run(self, mapa):
        # Si la celda es blanca, entonces gira a la izquierda
        self.mapa = mapa
        if self.mapa[self.x][self.y] == 1:
            self.mapa[self.x][self.y] = 0  # cambiamos a cero el valor
            self.mirandoHacia = (self.mirandoHacia - 1) % 4
            '''Haremos un return para que se cambie el valor del mapa en esa celda'''
        else:
            self.mapa[self.x][self.y] = 1
            self.mirandoHacia = (self.mirandoHacia + 1) % 4
            '''Haremos un return para que se cambie el valor del mapa en esa celda'''
        self.moverse()
        return self.mapa

    def moverse(self):
        celdaQueCambia = self.polygon
        colorPorPintar = self.mapa[self.x][self.y]
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

        self.actualizarPoligono()
        # pintamos la celda en la que se encuentra la hormiga
        self.dibujarse(self.polygon, self.color)
        # lo pintamos del color contrario al que está
        self.dibujarse(
            celdaQueCambia,
            self.color_negro
            if colorPorPintar == 0 else self.color_blanco
        )

    def dibujarse(self, poligono, color):
        pygame.draw.polygon(self.screen, color, poligono, 0)


'''
podemos hacer que la hormiga sea quien pinta cada cuadrito unicamente si lo cambia
entonces no tendriamos que refrescar toda la pantalla en cada iteracion

el tablero tendra una matriz de estados a la que todas las hormigas tendran acceso pa saber el estado del piso en ese momento

'''
# cell_color = 255, 255, 255
# si el numero aleatorio está dentro de un rango será un tipo de hormiga
# hormiga = ant(2, 2)
# print(hormiga.coordenadas)
