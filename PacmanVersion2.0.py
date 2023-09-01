import pygame
import time
import sqlite3
import random
db = sqlite3.connect('server13.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS user(
    name TEXT,
    surname TEXT,
    cash BIGINT
)""")
db.commit()
# db.close()
fill_lose = True
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((860,700))
pygame.display.set_caption("Pacman Version 2.0")
icon = pygame.image.load('image/pacman.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('image/lnC4o.png').convert()
i = 0 

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
    pygame.image.load('image/PacMan_Only (5).png')]):
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
        


enemy = []
i_enemy = 0
x_enemy = 640
coin = [Obj(100, 100,[
    pygame.image.load('image/coin.png')
])]

write_name = Obj(240, 170, [
    pygame.image.load('image/li.png'),
    pygame.image.load('image/li.png')
])
write_sur = Obj(240, 310, [
    pygame.image.load('image/li.png'),
    pygame.image.load('image/li.png')
])
enemy_count = 0


anim_count = 0
bg_sound = pygame.mixer.Sound('music/1-track-1.mp3')
bg_sound.play()
lose_sound = pygame.mixer.Sound('music/2-track-2.mp3')
coin_sound = pygame.mixer.Sound('music/sfx-2.mp3')

need_input_name = False
need_input_sur = False
input_text_name = ''
input_text_sur = ''

gameplay = False
gamestart = True
running = True
sql_play = True

myfont = pygame.font.Font('fonts/ofont.ru_Ostrovsky.ttf', 20)
text_font = myfont.render('ТЫ ПРОИГРАЛ',False, 'White')
text_lose = myfont.render('Играть заново',False, 'White')
text_start = myfont.render('Играть!',False, 'White')
text_lose_rect = text_lose.get_rect(topleft=(340, 250))

def print_text(message,x,y, font_color, font_size, font_type = 'fonts/ofont.ru_Ostrovsky.ttf' ):
    font_types = pygame.font.Font(font_type,font_size)
    text = font_types.render(message, True, font_color)
    screen.blit(text, (x,y))




while running:

    if gameplay:
        fill_lose = True
        screen.fill('Black')
        sql_play = True
        screen.blit(player.sprites[anim_count], (player.x, player.y))
        l_enemy = len(enemy)

        for f in range(1,l_enemy):
            screen.blit(enemy[f].sprites[enemy_count], (enemy[f].x, enemy[f].y))
            en_rect = enemy[f].rect()
            enemy[f].walk_enemy()
            # if enemy[f].y < 619 and enemy[f].i == 0:
            #     if enemy[f].y == 618:
            #         enemy[f].i = 1
            #     enemy[f].y += enemy[f].speed
            # elif enemy[f].y > 17 and enemy[f].i == 1: 
            #     if enemy[f].y == 18:
            #         enemy[f].i= 0
            #     enemy[f].y -= enemy[f].speed
            # else:
            #     enemy[f].x= 640
            #     enemy[f].y =18
        screen.blit(coin[0].sprites[0], (coin[0].x, coin[0].y))
        player_rect = player.rect()
        coin_rect = coin[0].rect()
        if player_rect.colliderect(coin_rect):
            coin_sound.play()
            rx = random.randint(18,600)
            ry = random.randint(18,600)
            coin.pop()
            i +=30
            enemy.append(Enemy(x_enemy - i,18, 100,5,100))
            coin.append(Obj(rx, ry,[
            pygame.image.load('image/coin.png')
            ]))
            player.coin += 1
        l_enemy = len(enemy)
        for f in range(1,l_enemy):
            en_rect = enemy[f].rect()
            if player_rect.colliderect(en_rect):
                lose_sound.play()
                player.health -= enemy[f].damage
                time.sleep(1)
                gameplay = False
                continue



    


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 12:
            player.x -= player.speed
            if anim_count != 5 and anim_count<6:
                anim_count +=1
            else:
                anim_count = 0
        elif keys[pygame.K_RIGHT] and player.x < 838:
            player.x += player.speed
            if anim_count != 5 and anim_count<6:
                anim_count +=1
            else:
                anim_count = 0
        elif keys[pygame.K_DOWN] and player.y < 688:
            player.y += player.speed
            if anim_count != 11 and anim_count >= 6 :
                anim_count +=1
            else:
                anim_count = 6
        elif keys[pygame.K_UP] and player.y > 12:
            player.y -= player.speed
            if anim_count != 5:
                anim_count +=1
            else:
                anim_count = 0
    elif gamestart:
        screen.fill('Black')
        
        screen.blit(text_start,(340, 410))
        text_start_rect = text_start.get_rect(topleft=(340, 410))

        screen.blit(write_name.sprites[0], (write_name.x, write_name.y))
        screen.blit(write_name.sprites[0], (write_sur.x, write_sur.y))
        write_rect1 = write_name.rect()
        write_rect2 = write_sur.rect()
        print_text('Введите имя:', write_name.x, write_name.y - 40, ('White'),20)
        print_text(input_text_name, write_name.x + 20 , write_name.y + 25,('Red'),20)
        print_text('Введите фамилию:', write_sur.x, write_sur.y - 40, ('White'),20)
        print_text(input_text_sur, write_sur.x + 20 , write_sur.y + 30,('Black'), 20)
        mouse = pygame.mouse.get_pos()
        if text_start_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            gamestart = False

            enemy.append(Enemy(x_enemy,18, 100,10,100))
            
            player = Person( 13, 13, 100, 15, 0, input_text_name, input_text_sur)
            
            need_input_name = False
            need_input_sur = False
            input_text_name = ''
            input_text_sur = ''
        if write_rect1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            need_input_name = True
            need_input_sur = False
        if write_rect2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            need_input_name = False
            need_input_sur = True


    else:
        if fill_lose:
            screen.fill('Black')
            fill_lose =False
        # screen.blit(text_font, (350, 180))
        screen.blit(text_lose, text_lose_rect)

        print_text('Тор 5 игроков!', 310, 330,('Red'),30)
        print_text('(Имя, фамилия, очки)', 320, 360,('Red'),15)


        if sql_play:
            k = 400
            k2 = 340
            sql.execute(f"INSERT INTO user VALUES(?,?,?)", (player.name,player.surname, player.coin))
            db.commit()
            sql.execute("SELECT * FROM user")
            result = sql.fetchall()
            coins_result = []
            max_result = 0
            max_result_index = 0
            
            for j in result:
                coins_result.append(j[2])
            coins_result_len = len(coins_result) 
            coins_result.sort()
            print(result)
            count_top = 0
            count_top_fin = 5
            if count_top_fin > coins_result_len:
                count_top_fin = coins_result_len
            for a in range(coins_result_len - 1, 0, -1):
                for j in result:
                    if j[2] == coins_result[a] and count_top < count_top_fin:
                        k += 30
                        text1 = '  '.join(map(str, j))  
                        print_text(text1, k2, k,('White'), 20)
                        count_top +=1
            k = 430
            k2 = 340
        sql_play = False
        mouse = pygame.mouse.get_pos()
        if text_lose_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gamestart = True
            player.x = 13
            player.y = 13
            coin[0].x = 400
            coin[0].y = 400
            player.health=100
            enemy.clear()
            i = 0

        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            db.close()
            pygame.quit()
        if event.type== pygame.KEYDOWN:
            if need_input_name and event.key == pygame.K_BACKSPACE:
                input_text_name = input_text_name[:-1]
            elif need_input_sur and event.key == pygame.K_BACKSPACE:
                input_text_sur = input_text_sur[:-1]
            else:
                if need_input_name and len(input_text_name) < 15:
                    input_text_name += event.unicode
                elif need_input_sur and len(input_text_sur) < 15:
                    input_text_sur += event.unicode
                else:
                    pass
        
    clock.tick(20)
