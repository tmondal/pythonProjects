import pygame
import random,sys
from random import randrange
import math
from pygame.locals import*

##----------------- COLOR DEFINING -------------------

BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
RED = (255 , 0 , 0)
BLUE =(0,0,255)
GREEN = (0 , 255 , 0)

##----------------- CLASS AND FUNCTION ---------------

class Player:
    def __init__(self, (x, y), size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.thickness = 0
        self.angle = 0
        self.speed = 0

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size, self.thickness)
    

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
       
#------------------------ WALL DEFINE ---------------------
    

class wall(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

#------------------------- BULLET -------------------------

class Bullet(pygame.sprite.Sprite):
    def __init__(self, (x, y), size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.thickness = 0
        self.angle = 0
        self.speed = 0

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size, self.thickness)
    
#------------------------- BULLET END ---------------------


def move(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    tangent = math.atan2(dy, dx)
    angle = 0.5 * math.pi + tangent

    angle1 = 2*tangent - p1.angle
    (p1.angle) = (angle1)
        
    p1.x -= 0.3*math.sin(angle)
    p1.y += 0.3*math.cos(angle)
        

def move_bullet(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    tangent = math.atan2(dy, dx)
    angle = 0.5 * math.pi + tangent
        
    p2.x += 10*math.sin(angle)
    p2.y -= 10*math.cos(angle)
def bullet_target_collide(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)
    if dist < (p1.size + p2.size):
        bullet_list.remove(p2)
def bullet_player_collide(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    
    if dist < (p1.size + p2.size):
        p1.x = randrange(-100,650)
        p1.y = randrange(-100,650)
def player_collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    
    if dist < (p1.size + p2.size):
        p1.x = randrange(-100,650)
        p1.y = randrange(-100,650)

##        pos = pygame.mouse.get_pos()
##        text=font.render("Short", True, GREEN)
##        screen.blit(text, [pos[0], pos[1]])
##        

##---------------------- GAME INITIATE ----------------------------
pygame.init()

screen_width = 600
screen_height = 600
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode([screen_width, screen_height],0,32)
#background = pygame.image.load("fground.jpg").convert()
clock = pygame.time.Clock()

##---------------------- PLAYER POSITIONING ------------------------

all_player =[]
for p in range(10):
    player = Player((randrange(-10,610),randrange(-100,610)),10,BLUE)
    all_player.append(player)   
##--------------------- BALL DEFINE --------------------------------
player_ball = Player((300,300),10,RED)

##--------------------- WALL POSITIONING ---------------------------
wall_list = pygame.sprite.Group()
bullet_list = []

wall_left = wall(0,0,3,screen_height)
wall_bottom =wall(0,screen_height - 3,screen_width,3)
wall_right = wall(screen_width - 3,0,3,screen_height)
wall_up = wall(0,0,screen_width,3)

wall_list.add(wall_left)
wall_list.add(wall_bottom)
wall_list.add(wall_right)
wall_list.add(wall_up)

##--------------------- MAIN GAME LOOP -----------------------------
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    ball_move(player_ball,oppo_player)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #pygame.mixer.music.load("soot.wav")
                #pygame.mixer.music.play()
                bullet = Bullet((player_ball.x,player_ball.y - 2),2,RED)
                bullet_list.append(bullet)
            
        screen.fill(BLACK)
        #screen.blit(background,(0,0))
        clock.tick(60)
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        target = Player((pos[0],pos[1]),10,GREEN)
        target.display()
        for player in all_player:
            move(player,player_ball)
            
        for b in bullet_list:
            move_bullet(target,b)
            bullet_target_collide(target,b)
        for b in bullet_list:
            for p in all_player:
                bullet_player_collide(p,b)
            
        for player in all_player:
            player_collide(player,player_ball)
            
        for p in all_player:
            p.display()
        player_ball.display()

        wall_list.draw(screen)

        for bullet in bullet_list:
            bullet.display()
        pygame.display.flip()
                
    pygame.quit()
if __name__ == "__main__":
  main()
