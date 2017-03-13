import pygame
import random,sys
import math
from pygame.locals import*

##----------------- COLOR DEFINING ---------------------

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
       

    

class wall(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y



def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        tangent = math.atan2(dy, dx)
        angle = 0.5 * math.pi + tangent
        angle1 = 2*tangent - p1.angle
        (p1.angle) = (angle1)
        p1.x += 12*math.sin(angle)
        p1.y -= 12*math.cos(angle)

def ball_move(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    tangent = math.atan2(dy, dx)
    angle = 0.5 * math.pi + tangent
    
    p1.x += 200*math.sin(angle)
    p1.y -= 200*math.cos(angle)

def isregion(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    if dist < 150:
        tangent = math.atan2(dy, dx)
        angle = 0.5 * math.pi + tangent

        angle1 = 2*tangent - p1.angle
        
        (p1.angle) = (angle1)
        
        p1.x -= 0.7*math.sin(angle)
        p1.y += 0.7*math.cos(angle)
        
    else:
        
        outregion(p1,p2)

def outregion(p1,p2):
    if p1 == all_player[5]:
        dx = 375 - p1.x
        dy = 200 - p1.y
    elif p1 == all_player[4]:
        dx = 225 - p1.x
        dy = 200 - p1.y
    elif p1 == all_player[3]:
        dx = 450 - p1.x
        dy = 100 - p1.y
    elif p1 == all_player[2]:
        dx = 300 - p1.x
        dy = 100 - p1.y
    elif p1 == all_player[1]:
        dx = 150 - p1.x
        dy = 100 - p1.y
    elif p1 == all_player[0]:
        dx = 300 - p1.x
        dy = 20 - p1.y
    
    dist = math.hypot(dx, dy)
    
    tangent = math.atan2(dy, dx)
    angle = 0.5 * math.pi + tangent

    angle1 = 2*tangent - p1.angle
    
    (p1.angle) = (angle1)
    
    p1.x += 2*math.sin(angle)
    p1.y -= 2*math.cos(angle)

    
        
def player_collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    
    if dist < (p1.size + p2.size):
        
        if p1 == all_player[5]:
            p1.x = 375
            p1.y = 200
        elif p1 == all_player[4]:
            p1.x = 225
            p1.y = 200
        elif p1 == all_player[3]:
            p1.x = 450
            p1.y = 100
        elif p1 == all_player[2]:
            p1.x = 300
            p1.y = 100
        elif p1 == all_player[1]:
            p1.x = 150
            p1.y = 100
        elif p1 == all_player[0]:
            p1.x = 300
            p1.y = 20

        pos = pygame.mouse.get_pos()
        text=font.render("Short", True, GREEN)
        screen.blit(text, [pos[0], pos[1]])
        p2.x = random.randint(300,500)
        p2.y = random.randint(500,550)

##def wall_collide(w1,p1):

    

    
        
##---------------------- GAME INITIATE ----------------------------
pygame.init()

screen_width = 600
screen_height = 600
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode([screen_width, screen_height],0,32)
background = pygame.image.load("fground.jpg").convert()
clock = pygame.time.Clock()

##---------------------- PLAYER POSITIONING -----------------------
relative = 300
x_d = 75
y_d = 100
all_player =[]
player = Player((relative,20),10,WHITE)
player_1 = Player((relative - 2*x_d,y_d),10,BLUE)
player_2 = Player((relative,y_d),10,(0,0,255))
player_3 = Player((relative + 2*x_d,y_d),10,BLUE)
player_4 = Player((relative - x_d,2*y_d),10,BLUE)
player_5 = Player((relative + x_d,2*y_d),10,BLUE)
player_ball = Player((relative + x_d,500),10,BLACK)

all_player.append(player)
all_player.append(player_1)
all_player.append(player_2)
all_player.append(player_3)
all_player.append(player_4)
all_player.append(player_5)

##--------------------- WALL POSITIONING ---------------------------
wall_list = pygame.sprite.Group()

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
            
        
        screen.blit(background,(0,0))
        clock.tick(60)
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        oppo_player = Oposit_player((pos[0],pos[1]),15)
        collide(player_ball,oppo_player)
        for player in all_player:
            isregion(player,player_ball)
            
        for player in all_player:
            player_collide(player,player_ball)

    ##    for wall in wall_list:
    ##        wall_collide(wall,player_ball)
            
        for player in all_player:
            player.display()
        player_ball.display()

        wall_list.draw(screen)
        oppo_player.display_user()
        pygame.display.flip()
                
    pygame.quit()
if __name__ == "__main__":
  main()
