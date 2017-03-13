# making first game

import pygame
import random,sys
from pygame.locals import*

#define some colors

BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE =(192,192,192)
GREEN = (0 , 255 , 0)

# class,function write here


    
class Block :

    change_y = 0
    change_x = 0
    def __init__(self,color,x,y,height):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        pygame.draw.rect(screen,self.color,(int(self.x),int(self.y),30,self.height))

    def update(self):
        self.y += self.change_y
        self.gravity()
        
    def gravity(self):
        if self.change_y == 0:
            
            self.change_y =1
        else:
            self.change_y +=0.35
            
        if self.y >= screen_height - self.height and self.change_y >= 0:
            self.change_y = 0
            self.y = screen_height - self.height
        

    def force(self):

        self.change_y =-6

    def change_pos(self,x):
        self.change_x = x
        self.x +=self.change_x
    

class wall :

    def __init__(self,color,x,y,height):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        
    def display(self):
        pygame.draw.rect(screen,self.color,(int(self.x),int(self.y),30,self.height))
        
    def update(self):
        self.x -= 2
        if self.x < -25 :
            self.x = screen_width

# initialize pygame
pygame.init()
screen_width = 1200
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


wall_list = []
player = Block(RED ,100,100, 25)

for x in range(0,1200,300):
        block_height = random.randint(100,300)
        Wall = wall(BLUE,x,0,block_height)
        Wall_bott = wall(BLUE,x,block_height + 100,screen_height)
        wall_list.append(Wall)
        wall_list.append(Wall_bott)

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# infinite loop untill user clicks cross
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
                
           
        
       
    screen.fill(BLUE)
    blocks_hit_list = pygame.sprite.spritecollide(player,wall_list,False)
    for blocks in blocks_hit_list :
        text=font.render("Touch", True, GREEN)
        screen.blit(text, [200, 300])
##        score +=1
##  
##        if score == 360:
##            text_1=font.render("Two Touch Left", True, GREEN)
##            screen.blit(text_1, [400, 300])
##            
##        if score == 380:
##            text_2=font.render("Be Careful  ONE LEFT", True, GREEN)
##            screen.blit(text_2, [600, 300])
##        if score == 400 :
##            pygame.quit()
##            sys.exit()


    
    player.update()
    all_block_list.draw(screen)
    for wall in wall_list:
        wall.display()
    
    wall_list.update()
    clock.tick(70)
    
    pygame.display.flip()
    
        
pygame.quit()
