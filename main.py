#STEAM30 - Momentum 2 block collision
#CS20- Template
#NAME: Reinhardt

import pygame
import time

#Screen size and frames per second
WIDTH = 1300
HEIGHT = 400
FPS = 30

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
font_name = pygame.font.match_font('calibri')

#Draw Text - Allows you to easily draw vars on screen at some x.,y
def draw_txt(surf, text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def momentum_math_simple(collider_velocity, collider_mass, other_velocity, other_mass):
    #starting math
    collider_momentum_inital = collider_velocity * collider_mass
    other_momentum_inital = other_velocity * other_mass
    momentum_inital = other_momentum_inital + collider_momentum_inital
    
    #what the collider final velocity should be (this is important for the physics but can be different or random)
    collider_velocity_final = 0
    print("collider_velocity_final, ", collider_velocity_final)

    #equation for the velocity final of the other object
    other_velocity_final = (collider_mass*(collider_velocity - collider_velocity_final) + other_momentum_inital)/other_mass

    print("other_velocity_final", other_velocity_final)
    print("collider_velocity_final, ", collider_velocity_final)

    #momentum final
    momentum_final = other_velocity_final*other_mass + collider_velocity_final*collider_mass

    if momentum_final == momentum_inital:
        print("Momentum is conserved!, ", momentum_final, momentum_inital)

    return collider_velocity_final, other_velocity_final, momentum_inital

 
#Blocks that collide
class Block(pygame.sprite.Sprite):
   
    #Block Initialize
    def __init__(self, side, blk_size, mass, v):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((blk_size,blk_size))
        self.rect = self.image.get_rect()
        self.rect.center = [WIDTH/2, HEIGHT/2]
        self.vel=v
        self.speedx = v
        self.mass=mass
        self.size = blk_size
       
        if side=="left":
            self.multiply=1
            self.image.fill(RED)
            self.rect.x = 50
        elif side=="right":
            self.multiply=-1
            self.image.fill(BLUE)
            self.rect.x = WIDTH - self.size - 50
        elif side == "middle":
            self.multiply = 1
            self.image.fill(GREEN)
            self.rect.x = (WIDTH - self.size)/2
        else:
            print("DIRECTION ERROR")
        
    #Keys, speed, direction for Left Block
    def update(self):
        
        #Auto run
        #if  self.vel!=0 and self.speedx == self.vel:
        self.rect.x += self.speedx * self.multiply
        


     
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
LEFT = Block("left",200,20,5)
RIGHT = Block("right",100,10,0)
MIDDLE = Block("middle", 200,10,-1)



all_sprites.add(LEFT)
all_sprites.add(RIGHT)
all_sprites.add(MIDDLE)

#extra variables
hit_count = 0
wall_hits = 0

#game loop
game_start = True
running = True

show_ttl_screen()

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

    
    #First colision of the left and middle block
   
    first_hit = pygame.sprite.collide_rect(LEFT, MIDDLE)


    if first_hit:
        leftspeed, middlespeed, momentum = momentum_math_simple(LEFT.vel, LEFT.mass, MIDDLE.vel, MIDDLE.mass)

        LEFT.speedx = leftspeed
        MIDDLE.speedx = middlespeed
        LEFT.rect.centerx += -10
        MIDDLE.rect.centerx += 10
        MIDDLE.image.fill(RED)


        print(LEFT.speedx)

        
        hit_count+=1
        #RIGHT.rect.left+=(RIGHT.vel+1)
         
        #LEFT.rect.right-=(LEFT.vel+1)

    #update
    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    
    draw_txt(screen, str(hit_count), 28, BLACK, (WIDTH/2), 10)
    draw_txt(screen, str(wall_hits), 18, BLACK, (WIDTH/2), 26)
    draw_txt(screen, str(LEFT.vel), 18, RED, (WIDTH/4), 26)
    draw_txt(screen, str(RIGHT.vel), 18, BLUE, 3*(WIDTH/4), 26)

    #flips display after drawing everything
    pygame.display.flip()

pygame.quit()
