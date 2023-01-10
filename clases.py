from ant import Ant


class Hormigas(Ant):
    def __init__(
        self, x, y, mapX, mapY, screen, clase
    ):
        super().__init__(x, y, mapX, mapY, screen)
        self.clase = clase 
