import pygame
class Person():
    health = 0
    speed = 0
    coin = 0
    name = ""
    surname = ""
    x = 0
    y = 0
    sprites = []
    def __init__(self, pl_x, pl_y, h, sp, coins,name, surname, sprite_game = [    
    pygame.image.load('image/PacMan_Only (2).png'),
    pygame.image.load('image/PacMan_Only (2).png'),
    pygame.image.load('image/PacMan_Only (2).png'),
    pygame.image.load('image/PacMan_Only (3).png'),
    pygame.image.load('image/PacMan_Only (3).png'),
    pygame.image.load('image/PacMan_Only (3).png'),  
    pygame.image.load('image/PacMan_Only (4).png'),
    pygame.image.load('image/PacMan_Only (4).png'),
    pygame.image.load('image/PacMan_Only (4).png'),
    pygame.image.load('image/PacMan_Only (5).png'),
    pygame.image.load('image/PacMan_Only (5).png'),
    pygame.image.load('image/PacMan_Only (5).png'),
    pygame.image.load('image/PacMan_Only (6).png'),
    pygame.image.load('image/PacMan_Only (6).png'),
    pygame.image.load('image/PacMan_Only (6).png'),
    pygame.image.load('image/PacMan_Only (7).png'),
    pygame.image.load('image/PacMan_Only (7).png'),
    pygame.image.load('image/PacMan_Only (7).png'),
    pygame.image.load('image/PacMan_Only (8).png'),
    pygame.image.load('image/PacMan_Only (8).png'),
    pygame.image.load('image/PacMan_Only (8).png'),
    pygame.image.load('image/PacMan_Only (9).png'),
    pygame.image.load('image/PacMan_Only (9).png'),
    pygame.image.load('image/PacMan_Only (9).png')]):
        self.x = pl_x
        self.y = pl_y
        self.health = h
        self.speed = sp
        self.coin = coins
        self.sprites = sprite_game
        self.name = name
        self.surname = surname
    def rect(self):
        return self.sprites[0].get_rect(topleft=(self.x, self.y))