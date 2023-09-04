import pygame
class Enemy:
    x = 0
    y = 0
    health = 0
    speed = 0
    damage = 0
    sprites = []
    i = 0
    def __init__(self, pl_x, pl_y, h, sp, d, sprite_game = [
    pygame.image.load('image/pngwing.png'),
    pygame.image.load('image/pngwing2.png')
    ], i =0):
        self.x = pl_x
        self.y = pl_y
        self.damage = d 
        self.health  = h
        self.speed = sp
        self.sprites = sprite_game
        self.i = i
    def rect(self):
        return self.sprites[0].get_rect(topleft=(self.x, self.y))
    def walk_enemy (self):
        if self.y < 619 and self.i == 0:
                if self.y == 618:
                    self.i = 1
                self.y += self.speed
        elif self.y > 17 and self.i == 1: 
                if self.y == 18:
                    self.i= 0
                self.y -= self.speed
        else:
            self.x= 640
            self.y =18