import pygame
import random,sys
import math
from pygame.locals import*

#----------------- COLOR DEFINING ---------------------

BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE =(0,0,255)
GREEN = (0 , 255 , 0)

#----------------- CLASS AND FUNCTION ---------------

class Player:
    change_x = 0
    change_y = 0
    def __init__(self, (x, y),color):
        self.x = x
        self.y = y
        self.color = color
        self.thickness = 0
        self.angle = 0
        self.speed = 0

    def display(self):
        pygame.draw.rect(screen,self.color,(int(self.x),int(self.y),20,20))
    def update(self):
        self.x += self.change_x
        self.y += self.change_y
    def change_pos(self,x,y):
        self.x += x
        self.y += y
class Line:
    def __init__(self,color,(x,y),width,height):
        self.color = color
        self.x= x
        self.y = y
        self.width = width
        self.height = height
    def display(self):
       pygame.draw.rect(screen,self.color,(int(self.x),int(self.y),self.width,self.height))
        
class Oposit_player:

    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255,0,0)
        self.thickness = 0
        self.angle = 0
        self.speed = 0
    
    def display_user(self):
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size, self.thickness)
#----------------------- Functions ------------------------------       
def main_oppo_move(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    tangent = math.atan2(dy, dx)
    angle = 0.5 * math.pi + tangent

    angle1 = 2*tangent - p1.angle
    (p1.angle) = (angle1)
        
    p1.x -= 0.2*math.sin(angle)
    p1.y += 0.2*math.cos(angle)

def Distance(p,b):
    dx = p.x - b.x
    dy = p.y - b.y
    s = dx*dx + dy*dy
    distance = math.sqrt(s)
    return distance
    

##class wall(pygame.sprite.Sprite):
##
##    def __init__(self,x,y,width,height):
##
##        pygame.sprite.Sprite.__init__(self)
##
##        self.image = pygame.Surface([width,height])
##        self.image.fill(GREEN)
##
##        self.rect = self.image.get_rect()
##
##        self.rect.x = x
##        self.rect.y = y

pygame.init()

screen_width = 1200
screen_height = 600
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode([screen_width, screen_height],0,32)
background = pygame.image.load("fground.jpg").convert()
clock = pygame.time.Clock()
#---------------------- LINE DRAWING -----------------------------
all_line =[]
line_1 = Line( WHITE,(40 , 20),1 , screen_height - 40)
line_2 = Line( WHITE,((screen_width / 2) , 20),1 , screen_height - 40)
line_3 = Line( WHITE,(screen_width - 40 , 20),1 , screen_height - 40)
line_4 = Line( WHITE,(40 , 20) , screen_width - 80 ,2)
line_5 = Line( WHITE,(40 , screen_height - 20) , screen_width - 80 ,2)
               
all_line.append(line_1)
all_line.append(line_2)
all_line.append(line_3)
all_line.append(line_4)
all_line.append(line_5)
               
#---------------------- PLAYER POSITIONING -----------------------
relative = screen_height / 2
x_d = screen_width / 4
y_d = relative / 2
all_player =[]
all_opposit_player =[]
player_1 = Player((20,relative),WHITE)
player_2 = Player((x_d,y_d),BLUE)
player_3 = Player((1.5*x_d,relative),BLUE)
player_4 = Player((x_d,relative + y_d),BLUE)

ball = Player((screen_width / 2, relative),BLACK)

all_player.append(player_1)
all_player.append(player_2)
all_player.append(player_3)
all_player.append(player_4)

opposit_1 = Player((screen_width - 40,relative),WHITE)
opposit_2 = Player((screen_width - x_d,y_d),BLUE)
opposit_3 = Player((screen_width - 1.5*x_d,relative),BLUE)
opposit_4 = Player((screen_width - x_d,relative + y_d),BLUE)

all_opposit_player.append(opposit_1)
all_opposit_player.append(opposit_2)
all_opposit_player.append(opposit_3)
all_opposit_player.append(opposit_4)
#--------------------- PLAYER SELECTION ---------------------------

#--------------------- MAIN GAME LOOP -----------------------------
def main():
   
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
##            elif event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_s:
##                    ball_move(player_ball,oppo_player)
            elif event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_UP:
                    player.change_pos(0,-8)
                if event.key == pygame.K_DOWN:
                    player.change_pos(0,8)
                if event.key == pygame.K_RIGHT:
                    player.change_pos(8,0)
                if event.key == pygame.K_LEFT:
                    player.change_pos(-8,0)
##            elif event.type == pygame.KEYUP:
##                if event.key == pygame.K_UP:
##                    player.change_pos(0,0)
##                if event.key == pygame.K_DOWN:
##                    player.change_pos(0,0)
##                if event.key == pygame.K_RIGHT:
##                    player.change_pos(0,0)
##                if event.key == pygame.K_LEFT:
##                    player.change_pos(0,0)
        
        screen.blit(background,(0,0))
        for player in all_player:
            player.display()
#-------------------- Player selection----------------------------
        dist = []    
        for p in all_player:
            d = Distance(p,ball)
            dist.append(d)
            min_dist = min(dist)
            i = dist.index(min_dist)
        player = all_player[i]
#------------------- Opposit player selection --------------------
        distance = []    
        for p in all_opposit_player:
            d1 = Distance(p,ball)
            distance.append(d1)
            min_dist = min(distance)
            i = distance.index(min_dist)
        opposit_player = all_opposit_player[i]
        main_oppo_move(opposit_player,ball)
        
        for p in all_opposit_player:
            p.display()
        for line in all_line:
            line.display()
        ball.display()
        player.update()
        clock.tick(60)
        pygame.display.flip()
                
    pygame.quit()
if __name__ == "__main__":
  main()
