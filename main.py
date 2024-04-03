#STEAM30 - Momentum 2 block collision
#CS20- Template
#NAME: Reinhardt

import pygame
import time

#Screen size and frames per second
WIDTH = 1200
HEIGHT = 400
FPS = 60

#variables for colours used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#initialise pygame and create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2Block Momentum")
clock = pygame.time.Clock()
    
#font for text used
font_name = pygame.font.match_font('arial')

#Draw Text - Allows you to easily draw vars on screen at some x.,y
def draw_txt(surf, text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
 
#Blocks that collide
class Block(pygame.sprite.Sprite):
    #Block Initialize
    def __init__(self,side,blk_size, mass, v):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((blk_size,blk_size))
        self.rect = self.image.get_rect()
        self.rect.bottom = 3*(HEIGHT / 4)
        self.vel=v
        self.speedx = v
        self.mass=mass
        if side=="left":
            self.multiply=1
            self.image.fill(RED)
            self.rect.x = 50
        elif side=="right":
            self.multiply=-1
            self.image.fill(BLUE)
            self.rect.x = 500
        else:
            print("DIRECTION ERROR")
        
    #Keys, speed, direction for Left Block
    def update(self):
        
        #Auto run
        if  self.vel!=0 and self.speedx == self.vel:
            self.rect.x += self.speedx * self.multiply
        
        #Keyboard run
        else:
            #Temperary movement keys (A/D)
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_a]:
                self.speedx = -10
            if keystate[pygame.K_d]:
                self.speedx = 10
        self.rect.x += self.speedx * self.multiply


#Wall
class Wall(pygame.sprite.Sprite):
    #Wall Initialize
    def __init__(self,loc,blk_size):
        pygame.sprite.Sprite.__init__(self)
        self.thick=25
        if loc=="left":
            self.image = pygame.Surface((self.thick,blk_size))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = (self.thick/2)-5
            self.rect.centery = HEIGHT/2
            
        elif loc=="right":
            self.image = pygame.Surface((self.thick,blk_size))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = (WIDTH-(self.thick/2))+5
            self.rect.centery = HEIGHT/2
        
        elif loc=="bottom":
            self.image = pygame.Surface((blk_size,self.thick))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.top = (3*(HEIGHT / 4))+1
        
        else:
            print("WALL BUILD ERROR")
     
#title screen, shows controls, gives option to start game
def show_ttl_screen():
    screen.fill(WHITE)
    #text for the title screen
    draw_txt(screen, "Momentum Block Solver!", 40, BLACK, WIDTH / 2, 10)
    
    #flips display after drawing
    pygame.display.flip()
    waiting = True
    while waiting:
        #keep running at correct speed
        clock.tick(FPS)
        for event in pygame.event.get():
            #close window
            if event.type == pygame.QUIT:
                pygame.quit()
                #starts game if a key is pressed
            if event.type == pygame.KEYUP:
                waiting = False
           
#sprites used
all_sprites = pygame.sprite.Group()
LEFT = Block("left",50,5,0)
RIGHT = Block("right",100,10,1)
Other = Block("right", 200,10,12)

L_Wall= Wall("left",HEIGHT)
B_Wall= Wall("bottom",WIDTH)
R_Wall=Wall("right",HEIGHT)
RR_Wall = Wall("right",HEIGHT)

all_sprites.add(LEFT)
all_sprites.add(RIGHT)
all_sprites.add(L_Wall)
all_sprites.add(B_Wall)
all_sprites.add(R_Wall)
all_sprites.add(RR_Wall)
all_sprites.add(Other)

#extra variables
hit_count = 0
wall_hits = 0

#game loop
game_start = True
running = True


while running:
        #title screen, will be the first thing to be displayed when game is run
#     if game_start:
#         show_ttl_screen()
#         game_start = False    
        
    #keep loop running at correct speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #close window
        if event.type == pygame.QUIT:
            running = False
            
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
            print("LEFT right edge: ", LEFT.rect.right)
            print("LEFT speedx: ", LEFT.speedx)
            print("LEFT multply: ", LEFT.multiply)
            print("RIGHT left edge: ", RIGHT.rect.left)
            print("RIGHT speedx: ", RIGHT.speedx)
            print("RIGHT multply: ", RIGHT.multiply)

    
    #Collision between 2 blocks
    b_hit = pygame.sprite.collide_rect(LEFT, RIGHT)
    if b_hit:
        hit_count+=1
        LEFT.speedx=0
        LEFT.rect.right-=(LEFT.vel+1)
        if LEFT.multiply!=RIGHT.multiply:
            RIGHT.multiply*=-1
        LEFT.multiply*=-1
        LEFT.speedx=LEFT.vel
        
        RIGHT.speedx=0
        RIGHT.rect.left+=(RIGHT.vel+1)
        RIGHT.speedx=RIGHT.vel
        
    #Collision between block and Wall   
    w_hit_L = pygame.sprite.collide_rect(LEFT, L_Wall)
    if w_hit_L:
        wall_hits+=1
        LEFT.rect.right+=2
        LEFT.multiply*=-1


        
    w_hit_R = pygame.sprite.collide_rect(RIGHT, R_Wall)
    if w_hit_R:
        wall_hits+=1
        RIGHT.rect.right+=2
        RIGHT.multiply*=-1
    

    #update
    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    
    draw_txt(screen, str(hit_count), 18, BLACK, (WIDTH/2), 10)
    draw_txt(screen, str(wall_hits), 18, BLACK, (WIDTH/2), 26)
    draw_txt(screen, str(LEFT.vel), 18, RED, (WIDTH/4), 26)
    draw_txt(screen, str(RIGHT.vel), 18, BLUE, 3*(WIDTH/4), 26)

    #flips display after drawing everything
    pygame.display.flip()

pygame.quit()
