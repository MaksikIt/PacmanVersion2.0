class Obj():
    x = 0
    y = 0
    sprites = []
    def __init__(self, pl_x, pl_y, spr):
        self.sprites = spr
        self.x = pl_x
        self.y = pl_y
    def rect(self):
        return self.sprites[0].get_rect(topleft=(self.x, self.y))