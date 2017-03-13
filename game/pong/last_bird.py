# making first game

import pygame
import random,sys
import math
from pygame.locals import*

#---------------defining some colors--------------------------------------

BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE =(0,0,255)
GREEN = (0 , 255 , 0)

# --------------class,function written here-------------------------------


    
class Block :

    change_y = 0
    change_x = 0
    def __init__(self,color,x,y,height):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.rect = pygame.Rect(int(self.x),int(self.y),30,self.height)

    def update(self):
        self.rect.y += self.change_y
        self.gravity()
        
    def gravity(self):
        if self.change_y == 0:
            
            self.change_y =2
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
    

class wall :

    def __init__(self,color,x,y,height):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.rect = pygame.Rect(int(self.x),int(self.y),30,self.height)
        
    def update(self):
        self.rect.x -= 2
        if self.rect.x < -25 :
            self.rect.x = screen_width

            
def collide(player,wall):
    
    if player.rect.colliderect(wall.rect):
        text_1=font.render("Touch", True, GREEN)
        screen.blit(text_1, [400, 300])
    else:
	   if player.rect.right > wall.rect.right :
	       score +=1 
	       message = 'score: %d' % score
	       text = font.render(message, 1, GREEN)
	       screen.blit(text, (500, 200))
        
#-------------------------------- pygame initilize----------------------------
pygame.init()
screen_width = 1200
screen_height = 400
step = 300
screen = pygame.display.set_mode([screen_width, screen_height])


wall_list = []
player = Block(RED ,100,100, 25)

for x in range(0,screen_width,step):
        block_height = random.randint(100,300)
        Wall = wall(BLUE,x,0,block_height)
        Wall_bott = wall(BLUE,x,block_height + 100,screen_height)
        wall_list.append(Wall)
        wall_list.append(Wall_bott)

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


#---------------------- infinite loop untill user clicks cross------------------
def main():
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
                     
           
        screen.fill(BLACK)
        

        for wall in wall_list:
            collide(player,wall)
        for wall in wall_list:
            pygame.draw.rect(screen,(0,0,255),wall.rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        player.update()
        for wall in wall_list:
            wall.update()
        clock.tick(70)
        pygame.display.flip()
       
    pygame.quit()
if __name__ == "__main__":
  main()
