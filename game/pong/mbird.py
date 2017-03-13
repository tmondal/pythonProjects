
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
            
            self.change_y =8
        else:
            self.change_y +=.45
            
        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_height - self.rect.height
        

    def force(self):

        self.change_y =-8

    def change_pos(self,x):
        self.change_x = x
        self.rect.x +=self.change_x
    

class wall :
    score = 0
    def __init__(self,color,x,y,height):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.rect = pygame.Rect(int(self.x),int(self.y),60,self.height)
        
    def update(self):
        self.rect.x -= 3
        if(self.rect.x < -60) :
            self.rect.x = screen_width
            self.score = self.score + 1
        message = 'score: %d' % self.score
        text = font.render(message, 1, GREEN)
        screen.blit(text, (400, 10))

            
def collide(player,wall):

    if player.rect.colliderect(wall.rect):
        text_1=font.render("Touch", True, GREEN)
        screen.blit(text_1, [200, 200])
        pygame.quit()
        sys.exit()
       
        
#-------------------------------- pygame initilize----------------------------
pygame.init()
screen_width = 500
screen_height = 500
step = 200
screen = pygame.display.set_mode([screen_width, screen_height])


wall_list = []
top_wall = []
player = Block(RED ,100,100, 25)
wall_pos = (screen_width)       
block_height = random.randint(100,200)        
Wall = wall(BLUE,wall_pos,0,block_height)
Wall_bott = wall(BLUE,wall_pos,block_height + 200,screen_height)
wall_list.append(Wall)
wall_list.append(Wall_bott)

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
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
        clock.tick(100)
        pygame.display.flip()
pygame.quit()     
