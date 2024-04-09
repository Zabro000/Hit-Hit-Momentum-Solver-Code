#STEAM30 - Momentum 2 block collision
#CS20- Template
#NAME: Reinhardt

import pygame
import time
import random



#Screen size and frames per second
WIDTH = 1500
HEIGHT = 400
FPS = 60

big = 200
small = 100

sig_digs = 4 # what to round the new random mass and velocity to so the screen is not too messy

#variables for colours used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COPPER = (72, 45, 20)

#initialise pygame and create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penny Lab Simulation")
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

def velocity_finder_simple(collider_velocity, collider_mass, other_velocity, other_mass):
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

def momentum_math_simple(mass, velocity):
    return mass * velocity


#simple kinetic energy math function for 1D objects
def kinetic_energy_math_simple(net_velocity, mass):
    return (1/2) * mass * (net_velocity**2)


#uses amount of momentum to sort
def bubble_sort(item_list):
    item_list_length = len(item_list)

    for index in range(item_list_length):

        for object_ in range(0, item_list_length - index - 1):
            
            if abs(item_list[object_].momentum) > abs(item_list[object_ + 1].momentum):
                item_list[object_], item_list[object_ + 1] = item_list[object_ + 1], item_list[object_]
    


    return item_list


            

 
#Blocks that collide
class Block(pygame.sprite.Sprite):
   
    #Block Initialize
    def __init__(self, side, blk_size, mass, v, name = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((blk_size,blk_size))
        self.rect = self.image.get_rect()
        self.rect.center = [WIDTH/2, HEIGHT/2]
        self.vel=v
        self.speedx = v
        self.mass=mass
        self.size = blk_size
        self.float_position_x = 0
        self.text_color = BLACK
        self.kinetic_energy = 0 
        self.body_color = BLUE

       
        if side=="left":
            self.float_position_x = 50
        elif side == "c_left":
            self.float_position_x = 250
        elif side=="right":
            self.float_position_x = WIDTH - self.size - 50
        elif side == "c_right":
            self.float_position_x = WIDTH - self.size - 250
        elif side == "middle":
            self.float_position_x = (WIDTH - self.size)/2
        else:
            print("DIRECTION ERROR")
            raise TypeError

        if name is None:
            self.name = "general block"
        else:
            self.name = name

        


        self.rect.x = self.float_position_x

    
    @property
    def momentum(self):
        return self.mass * self.speedx
    
  
    #Keys, speed, direction for Left Block
    def update(self):
        
        #Auto run
        #if  self.vel!=0 and self.speedx == self.vel:
        self.float_position_x += self.speedx
        self.rect.x = round(self.float_position_x)
        #print("Self rect x plus speed: ", self.rect.x)
        self.kinetic_energy = kinetic_energy_math_simple(self.speedx, self.mass)
    

        # sign of the speed direction is important for the code to determine which way the block will bounce away on a collision
        if self.speedx > 0:
            self.speedx_sign = 1
        elif self.speedx < 0:
            self.speedx_sign = -1
        else:
            self.speedx_sign = 2

        
class Button(pygame.sprite.Sprite):


    def __init__(self, display_text, color, position_x, position_y) -> None:
        self.button_width = 200
        self.button_height = 100
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.button_width,self.button_height))
        self.rect = self.image.get_rect()
        self.rect.center = [position_x, position_y]
        self.display_text = display_text
        self.color = color
        self.x_position = position_x
        self.y_position = position_y 
        self.image.fill(color)

        

     
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





            
all_buttons = pygame.sprite.Group()
Random_B = Button("Random Collision", GREEN, WIDTH/2 - 150, HEIGHT/2 - 30)
Default_B = Button("Defualt Collision", BLUE, WIDTH/2 + 150, HEIGHT/2 - 30)
Rear_End_B = Button("Rear End Collision", RED, WIDTH/2, HEIGHT/2 + 100)

all_buttons.add(Random_B)
all_buttons.add(Default_B)
all_buttons.add(Rear_End_B)

show_ttl_screen()

# Defining the states for the different buttons
random_selection = False
rear_end_selection = False 
defualt_selection = False

#Settings so the user can choose if they want a random collision or 
#/////////////////////////////////////////////////////////////////////////////////////////////////////
screen.fill(WHITE)
draw_txt(screen, "Settings for blocks:", 40, BLACK, WIDTH/2, 10)

pygame.display.flip()

running = True

while running:
    clock.tick(FPS)

    mouse_location = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                pygame.quit()

        # Checks if there was a mouse click and it was over this button
        if event.type == pygame.MOUSEBUTTONDOWN:
            """   print(Random_B.rect.left)
            print(mouse_location[0])
            print(mouse_location[1])
            print(Random_B.rect.top)
            print('\n') """
                
            if Random_B.rect.left <= mouse_location[0] <= Random_B.rect.left + Random_B.button_width and Random_B.rect.top <= mouse_location[1] <= Random_B.rect.bottom:
                print("button was pressed")
                random_selection = True
                running = False

            if Default_B.rect.left <= mouse_location[0] <= Default_B.rect.left + Default_B.button_width and Default_B.rect.top <= mouse_location[1] <= Default_B.rect.bottom:
                print("A button was pressed")
                defualt_selection = True
                running = False

            if Rear_End_B.rect.left <= mouse_location[0] <= Rear_End_B.rect.left + Default_B.button_width and Rear_End_B.rect.top <= mouse_location[1] <= Rear_End_B.rect.bottom:
                print("A button was pressed")
                rear_end_selection = True
                running = False

        all_buttons.update()
        all_buttons.draw(screen)

        # shows the display text of the button
        draw_txt(screen,str(Random_B.display_text), 20, BLACK, Random_B.x_position, Random_B.y_position - 10)
        draw_txt(screen, str(Default_B.display_text), 20, BLACK, Default_B.x_position, Default_B.y_position - 10)
        draw_txt(screen, str(Rear_End_B.display_text), 20, WHITE, Rear_End_B.x_position, Rear_End_B.y_position -10)
        pygame.display.flip()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#sprites used



all_sprites = pygame.sprite.Group()
LEFT = Block("left",200, 600, 5,"left block")  
RIGHT = Block("right",100,100, -1)
MIDDLE = Block("middle",200,20, 0.1, "middle block")

all_sprites.add(LEFT)
all_sprites.add(RIGHT)
all_sprites.add(MIDDLE)


# assigns random mass and velocity to all objects
sig_digs = 4 # what to round the new random mass and velocity to so the screen is not too messy

if random_selection == True:
    for objects in all_sprites:
        new_velocity = round(random.uniform(-3.5, 3.5), sig_digs)
        new_mass = round(random.uniform(0.1, 500), sig_digs)
        objects.speedx  = new_velocity
        objects.mass = new_mass

elif rear_end_selection == True:
     LEFT.mass = 40
     LEFT.speedx = 3
     MIDDLE.mass = 20
     MIDDLE.speedx = 1
     RIGHT.mass = 10
     RIGHT.speedx = 0

elif defualt_selection == True:
     penny_mass = 0.00235
     LEFT.side = "c_left"
     RIGHT.side = "c_right"
     for objects in all_sprites:
         objects.mass = penny_mass
         objects.body_color = COPPER
         objects.speedx = 0
    
     LEFT.speedx = 1.5
else: 
      
      raise "E"

     


      """     penny_mass = 0.00235 
      for objects in all_sprites:
        objects.mass = penny_mass
        objects.speedx = 0
        objects.body_color = COPPER 
        objects.blk_size = 75 """



#extra variables
hit_count = 0


#game loop
game_start = True
running = True

#Screen outputs




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
            print("RIGHT left edge: ", RIGHT.rect.left)
            print("RIGHT speedx: ", RIGHT.speedx)
            print("MIDDLE EDGE: ", MIDDLE.rect.right)
            print("Middle speedx: ", MIDDLE.speedx)

    
    #First colision of the left and middle block
   
    first_hit = pygame.sprite.collide_rect(LEFT, MIDDLE)


    if first_hit:
         
        # Statements to handle head on collisions vs collisions where one object pushes another
        if LEFT.speedx_sign == MIDDLE.speedx_sign:
            collider = LEFT
            projectile = MIDDLE
        else:

            first_hit_objs = [LEFT, MIDDLE]
            first_hit_objs = bubble_sort(first_hit_objs)
            collider = first_hit_objs[-1]
            projectile = first_hit_objs[-2]
            print("velocity of fastest", first_hit_objs[-1].name)
            print("should stop:", first_hit_objs[-1].name)


        collider_space_sign = -1 * collider.speedx_sign
        projectile_space_sign = -1 * projectile.speedx_sign

        collider.float_position_x += 30 * collider_space_sign
        projectile.float_position_x += 10 * projectile_space_sign

        collider.speedx, projectile.speedx, momentum = velocity_finder_simple(collider.speedx, collider.mass, projectile.speedx, projectile.mass)

        collider_space_sign = -1 * collider.speedx_sign
        projectile_space_sign = -1 * projectile.speedx_sign

        collider.float_position_x += 30 * collider_space_sign
        projectile.float_position_x += 10 * projectile_space_sign

        hit_count+=1

    
    second_hit = pygame.sprite.collide_rect(RIGHT, MIDDLE)

    if second_hit:

        # Statements to handle head on collisions vs collisions where one object pushes another
        if RIGHT.speedx_sign == MIDDLE.speedx_sign:
            collider = RIGHT
            projectile = MIDDLE
        else:

            first_hit_objs = [RIGHT, MIDDLE]
            first_hit_objs = bubble_sort(first_hit_objs)
            collider = first_hit_objs[-1]
            projectile = first_hit_objs[-2]
            print("velocity of fastest", first_hit_objs[-1].name)
            print("should stop:", first_hit_objs[-1].name)

        collider_space_sign = -1 * collider.speedx_sign
        projectile_space_sign = -1 * projectile.speedx_sign

        collider.float_position_x += 30 * collider_space_sign
        projectile.float_position_x += 10 * projectile_space_sign

        collider.speedx , projectile.speedx, momentum = velocity_finder_simple(collider.speedx, collider.mass, projectile.speedx, projectile.mass)

        
        hit_count+=1

     
    #Changing the color of the text based if a sprite is moving or not
    for sprite in all_sprites:
        if sprite.speedx != 0:
            sprite.text_color = RED 
            sprite.image.fill(RED)
        else:
            sprite.text_color = BLACK
            sprite.image.fill(sprite.body_color)
    
    total_kinetic_energy = LEFT.kinetic_energy + MIDDLE.kinetic_energy + RIGHT.kinetic_energy
    total_momentum = LEFT.momentum + MIDDLE.momentum + RIGHT.momentum
    round_total_momentum = round(total_momentum, sig_digs)
    round_total_kinetic_energy = round(total_kinetic_energy, sig_digs)

    #update
    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    draw_txt(screen, f"Block 1 speed {str(round(LEFT.speedx, sig_digs))} and mass {str(round(LEFT.mass,sig_digs))}", 18, LEFT.text_color, (200), 20)

    draw_txt(screen, f"Block 1 kinetic energy {str(round(LEFT.kinetic_energy, sig_digs))}", 18, LEFT.text_color, (200), 40)

    draw_txt(screen, f"Block 2 speed {str(round(MIDDLE.speedx, sig_digs))} and mass {str(round(MIDDLE.mass, sig_digs))}", 18, MIDDLE.text_color, (WIDTH/2), 20)

    draw_txt(screen, f"Block 2 kinetic energy {str(round(MIDDLE.kinetic_energy, sig_digs))}", 18, MIDDLE.text_color, (WIDTH/2), 40)

    draw_txt(screen, f"Block 3 speed {str(round(RIGHT.speedx, sig_digs))}  and mass {str(round(MIDDLE.mass, sig_digs))}", 18, RIGHT.text_color, (WIDTH-200), 20)

    draw_txt(screen, f"Block 3 kinetic energy {str(round(RIGHT.kinetic_energy, sig_digs))}", 18, RIGHT.text_color, (WIDTH-200), 40)

    
    draw_txt(screen, f"The total kinetic energy of the system is {str(round_total_kinetic_energy)}.", 20, RED, (WIDTH/2), (HEIGHT-20))

    draw_txt(screen, f"The total momentum of the system is {str(round_total_momentum)}.", 20, RED, (WIDTH/2), (HEIGHT-40))

    draw_txt(screen, f"The number of collisions is {str(hit_count)}.", 20, RED, (WIDTH/2), (HEIGHT-60))


    
 

    """ draw_txt(screen, str(hit_count), 28, BLACK, (WIDTH/2), 10)
    draw_txt(screen, str(wall_hits), 18, BLACK, (WIDTH/2), 26)
    draw_txt(screen, str(LEFT.vel), 18, RED, (WIDTH/4), 26)
    draw_txt(screen, str(RIGHT.vel), 18, BLUE, 3*(WIDTH/4), 26) """

    #flips display after drawing everything
    pygame.display.flip()

pygame.quit()
