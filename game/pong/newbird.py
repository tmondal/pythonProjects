# making first game

import pygame
import random,sys
from random import randrange
from pygame.locals import*

#defining colors and variables

BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE =(0,0,200)
GREEN = (0 , 255 , 0)
MAX_STARS  = 250
STAR_SPEED = 2
screen_width = 1200
screen_height = 400

# class,function written here


def init_stars(screen):
  global stars
  stars = []
  for i in range(MAX_STARS):
    star = [randrange(0,screen_width - 1),randrange(0,screen_height - 1)]
    stars.append(star)
 
def move_and_draw_stars(screen):
  global stars
  for star in stars:
##    star[0] += STAR_SPEED
##    if star[0] >= screen_width:
##      star[0] = 0
##      star[1] = randrange(0,400)
 
    screen.set_at(star,(255,255,255))
    
class Block(pygame.sprite.Sprite):

    change_y = 0
    change_x = 0
    def __init__(self,color,width,height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width , height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 200

    def update(self):
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
        self.rect.x +=self.change_x
    

class wall(pygame.sprite.Sprite):
    #score = 0
    def __init__(self,x,y,width,height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill((102,51,0))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.w = width
    def update(self):
        self.rect.x -= 2

        if (self.rect.x + self.w) < 0 :
            self.rect.x = screen_width
            self.height = randrange(80,300)
            #self.score = self.score + 1
            
# This is another list of all sprites including player

all_block_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

player = Block(RED , 25 , 25)
all_block_list.add(player)

def main():
    pygame.init()
    scoer = 0
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Flying Bird")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    for x in range(600,1800,300):
        block_height = random.randint(80,300)
        Wall = wall(x,0,45,block_height)
        Wall_bott = wall(x,block_height + 100,45,screen_height)
        wall_list.add(Wall)
        wall_list.add(Wall_bott)
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
                    player.change_pos(8)
                if event.key == pygame.K_LEFT:
                    player.change_pos(-8)
        
                   
        screen.fill(BLUE)
        blocks_hit_list = pygame.sprite.spritecollide(player,wall_list,False)
        for block in blocks_hit_list :
            text=font.render("Touch", True, GREEN)
            screen.blit(text, [200, 300])
        
        
        player.update()
        all_block_list.draw(screen)
        wall_list.draw(screen)
        wall_list.update()
        for wa in wall_list:
          if ((wa.rect.x + wa.w) < 0) :
            score = score + 1
        message = 'score: %d' % score
        text = font.render(message, 1, GREEN)
        screen.blit(text, (500, 200))
        move_and_draw_stars(screen)
        clock.tick(70)
        pygame.display.flip()
 
if __name__ == "__main__":
  main()
