import pygame
import random,sys
from random import randrange
import math
from pygame.locals import*
#----------------- GLOBAL VARIABLES ---------
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE =(0,0,255)
GREEN = (0 , 255 , 0)
MAX_STARS  = 250
STAR_SPEED = 2
screen_width = 400
screen_height = 400
stone_height = 10
stone_width = 10
Hammer_width = 30
Hammer_height = 20
p_width = 20
p_height = 20

#----------------- class,function ---------

#----------------- BACK GROUND ------------
def init_stars(screen):
  global stars
  stars = []
  for i in range(MAX_STARS):
    star = [randrange(0,screen_width - 1),randrange(0,screen_height - 1)]
    stars.append(star)
 
def move_and_draw_stars(screen):
  global stars
  for star in stars:
    star[0] += STAR_SPEED
    if star[0] >= screen_width:
      star[0] = 0
      star[1] = randrange(0,400)
 
    screen.set_at(star,(255,255,255))
#--------------- BACK GROUND END ------------

#--------------- PLAYER DEFINE --------------

class Player(pygame.sprite.Sprite):

    change_y = 0
    change_x = 0
    def __init__(self,color,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([p_width , p_height])
        self.image.fill(color)
        #self.image = pygame.image.load('boy.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x +=self.change_x
        self.rect.y += self.change_y
        self.gravity()
    def gravity(self):
        if self.change_y == 0:
            
            self.change_y =1
        else:
            self.change_y +=0.35
            
        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_height - self.rect.height
    def force(self):
        self.change_y =-6
    def change_pos(self,x):
        self.change_x = x
    def hit_change(self,x):
        self.rect.x += x

#--------------- STONE ----------------------
class Stone(pygame.sprite.Sprite):
    x_change = 0
    y_change = 0
    def __init__(self, color, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([stone_width, stone_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.y +=self.y_change
#------------------------- STONE END ----------------------

#------------------------- HAMMER -------------------------

class Hammer(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Hammer_width, Hammer_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -=3
        if self.rect.x < 0:
            self.rect.x = screen_width
            self.rect.y = randrange(110,400)
#------------------------- HAMMER END ---------------------

#------------------------- BULLET -------------------------

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([random.randint(4,20), random.randint(4,20)])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y -= 3
#------------------------- BULLET END ---------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])    
    pygame.display.set_caption("Run")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    all_sprite_list = pygame.sprite.Group()
    stone_list =  pygame.sprite.Group()
    stone1_list =  pygame.sprite.Group()
    player_list = pygame.sprite.Group()
    hammer_list =  pygame.sprite.Group()
    bullet_list =  pygame.sprite.Group()
    top = 0
    top_1 = 10
    value_list = [128,256,512]
    color_list = [BLUE]
    for column in range(0,100):
        for row in range(0,randrange(3,10)):
            stone = Stone(random.choice(color_list),top, row * (stone_height + 2) + 1)
            stone_list.add(stone)
            all_sprite_list.add(stone)
        top += stone_width + 2

    hammer_x_pos = 500
    for row in range(0,3):
        hammer = Hammer(RED,hammer_x_pos ,randrange(20,400))
        hammer_x_pos +=randrange(100,200)
        hammer_list.add(hammer)
        all_sprite_list.add(hammer)
    player = Player(GREEN,30,350)
    player_list.add(player)
    all_sprite_list.add(player)
    init_stars(screen)
    while True:
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_UP:
                    player.force()
                if event.key == pygame.K_RIGHT:
                    player.change_pos(4)
                if event.key == pygame.K_LEFT:
                    player.change_pos(-4)
                
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_RIGHT:
                    player.change_pos(0)

                if event.key == pygame.K_LEFT:
                    player.change_pos(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.load("soot.wav")
                pygame.mixer.music.play()
                bullet = Bullet()
                bullet_list.add(bullet)
                all_sprite_list.add(bullet)
                bullet.rect.x = (player.rect.x + p_width/2)
                bullet.rect.y = player.rect.y
                     
        screen.fill((0,0,0))
##        message = 'score: %d' % score
##        text = font.render(message, 1, GREEN)
##        screen.blit(text, (300, 100))
        hit = pygame.sprite.spritecollide(player,hammer_list,False)
        if hit :
            player.hit_change(-50)
        for block in hit:
            if player.change_y > 0:
                player.rect.bottom = block.rect.top
                if player.rect.bottom == block.rect.top:
                    player.change_x = -3
            elif player.change_y < 0:
                player.rect.top = block.rect.bottom
        for b in bullet_list:
            hit_stone = pygame.sprite.spritecollide(b,stone_list,False)
            for s in hit_stone:
              s.y_change +=0.5
              all_sprite_list.remove(b)
        for h in hammer_list :
            hammer_hit_bullet = pygame.sprite.spritecollide(h,bullet_list,True)
        for rs in stone1_list:
            blue_stone = pygame.sprite.spritecollide(rs,stone_list,True)
            all_sprite_list.remove(blue_stone)
        for rs in stone1_list:
            rs.update()
        move_and_draw_stars(screen)
        clock.tick(70)
        all_sprite_list.draw(screen)
        all_sprite_list.update()
        pygame.display.flip()
 
if __name__ == "__main__":
  main()
