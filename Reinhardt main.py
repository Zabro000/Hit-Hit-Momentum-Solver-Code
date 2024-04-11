#STEAM30 - Momentum 2 block collision
#CS20- Template
#NAME: Reinhardt

import pygame
import time
import random
import math


#Screen size and frames per second
WIDTH = 1500
HEIGHT = 400
FPS = 60

big = 200
small = 100

sig_digs = 4 # what to round the new random mass and velocity to so the screen is not too messy

penny_img = "Reinhardt penny.jpeg"

#variables for colours used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COPPER = (196, 98, 16)

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


def momentum_math_simple(mass, velocity):
    return mass * velocity


#simple kinetic energy math function for 1D objects
def kinetic_energy_math_simple(net_velocity, mass):
    return (1/2) * mass * (net_velocity**2)


# Does the math for collisions
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

# Does the math for collisions
def velocity_finder_simple_3(collider_velocity, collider_mass, other_velocity, other_mass):
    #Initalizing all the varibles needed in the math loop
    collider_inital_kinetic = kinetic_energy_math_simple(collider_velocity, collider_mass)
    other_inital_kinetic = kinetic_energy_math_simple(other_velocity, other_mass)
    total_inital_kinetic = other_inital_kinetic + collider_inital_kinetic

    print("inital kinetic energy of the two objects")
    
    collider_final_kinetic = 0
    other_final_kinetic = 0 
    total_final_kinetic = 0 

    collider_final_kinetic = collider_final_kinetic + other_final_kinetic

    inital_collider_momentum = collider.momentum 
    collider_velocity_final = 0
    other_velocity_final = 0

    # collision cannot generate energy and must cause more collisions:
    while total_inital_kinetic > total_final_kinetic and other_velocity_final < collider_velocity_final: 

        #This is what I saw when doing the penny lab, that the colliding object would transfer all of its mommentum
        if collider_mass <= other_mass:
            collider_velocity_final = collider_velocity * round(random.uniform(0.0, 0.3), 4)
            print("less than")
        # Larger objects tend to keep lots of their momentum in collisons with smaller objects
        else:
            collider_velocity_final = collider_velocity * round(random.uniform(0.4, 0.7), 4)



        #starting math
        collider_momentum_inital = collider_velocity * collider_mass
        other_momentum_inital = other_velocity * other_mass
        momentum_inital = other_momentum_inital + collider_momentum_inital


        #equation for the velocity final of the other object
        other_velocity_final = (collider_mass*(collider_velocity - collider_velocity_final) + other_momentum_inital)/other_mass

    
    
        #what the collider final velocity should be (this is important for the physics but can be different or random)
        print("collider_velocity_final, ", collider_velocity_final)

        print("other_velocity_final", other_velocity_final)
        print("collider_velocity_final, ", collider_velocity_final)

        momentum_final = other_velocity_final*other_mass + collider_velocity_final*collider_mass

        if momentum_final == momentum_inital:
            print("Momentum is conserved!, ", momentum_final, momentum_inital)


        total_final_kinetic = kinetic_energy_math_simple(collider_velocity_final, collider_mass) + kinetic_energy_math_simple(other_velocity_final, other_mass)

        print("MATH IS DONE")

    return collider_velocity_final, other_velocity_final, momentum_inital


def velocity_finder_simple_2(collider_velocity, collider_mass, other_velocity, other_mass):
    collider_velocity_final = 0 
    collider_inital_kinetic = kinetic_energy_math_simple(collider_velocity, collider_mass)

    other_inital_kinetic = kinetic_energy_math_simple(other_velocity, other_mass)

    total_inital_kinetic_energy = other_inital_kinetic + collider_inital_kinetic

    other_velocity_final = ((0.5 *total_inital_kinetic_energy)/other_mass)**0.5

    collider_momentum_inital = collider_velocity * collider_mass
    other_momentum_inital = other_velocity * other_mass
    momentum_inital = other_momentum_inital + collider_momentum_inital

    return collider_velocity_final, other_velocity_final, momentum_inital


    



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


# Buttons for options
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
    draw_txt(screen, "Penny Lab Simulation!!!", 40, BLACK, WIDTH / 2, 10)
    draw_txt(screen, "Press any key to continue.", 25, RED, WIDTH / 2, 50)
    draw_txt(screen,"This simulates the collisions between three objects, or pennies placed beside each other, like the picture below. One of the colliding objects will always have its final velocity set to 0m/s to reflect the penny collision in real life.", 15, BLACK, WIDTH/2, 80)
    
    
    # Loads in the image of the simulation 
    penny_image = pygame.image.load(penny_img)
    penny_image_rect_x = round(penny_image.get_width())
    penny_image_rect_y = round(penny_image.get_height())
    new_penny_image_x = round(penny_image_rect_x/4)
    new_penny_image_y = round(penny_image_rect_y/4)


    penny_image = pygame.transform.scale(penny_image, (round(penny_image_rect_x/4), round(penny_image_rect_y/4)))

    screen.blit(penny_image, (WIDTH/2 - new_penny_image_x/2 ,100))


    
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





#initalize all buttons       
all_buttons = pygame.sprite.Group()
Random_B = Button("Random Collision", BLUE, WIDTH/2 - 150, HEIGHT/2 - 30)
Default_B = Button("Penny Collision", COPPER, WIDTH/2 + 150, HEIGHT/2 - 30)
Rear_End_B = Button("Rear End Collision", RED, WIDTH/2, HEIGHT/2 + 100)

all_buttons.add(Random_B)
all_buttons.add(Default_B)
all_buttons.add(Rear_End_B)

show_ttl_screen()

# Defining the states for the different buttons
random_selection = False
rear_end_selection = False 
defualt_selection = False

#SETTINGS GAME LOOP:
#/////////////////////////////////////////////////////////////////////////////////////////////////////
screen.fill(WHITE)
draw_txt(screen, "Collision Options:", 40, BLACK, WIDTH/2, 10)

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
        draw_txt(screen,str(Random_B.display_text), 20, WHITE, Random_B.x_position, Random_B.y_position - 10)
        draw_txt(screen, str(Default_B.display_text), 20, WHITE, Default_B.x_position, Default_B.y_position - 10)
        draw_txt(screen, str(Rear_End_B.display_text), 20, WHITE, Rear_End_B.x_position, Rear_End_B.y_position -10)
        pygame.display.flip()
#DONE SETTINGS GAME LOOP
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#sprites used
all_sprites = pygame.sprite.Group()
LEFT = Block("left",200, 600, 5,"left block")  
RIGHT = Block("right",100,100, -1)
MIDDLE = Block("middle",200,20, 0.1, "middle block")

all_sprites.add(LEFT)
all_sprites.add(RIGHT)
all_sprites.add(MIDDLE)


#Code for which button the user picked 

if random_selection == True:
    for objects in all_sprites:
        new_velocity = round(random.uniform(-3.5, 3.5), sig_digs)
        new_mass = round(random.uniform(0.1, 500), sig_digs)
        objects.speedx  = new_velocity
        objects.mass = new_mass
        
        
        # quick fix because the right and the middle block would end up with the same random properties somehow    
    RIGHT.mass = round(random.uniform(0.1, 520), sig_digs)
    RIGHT.speedx = round(random.uniform(-3.5, 3.6), sig_digs)

elif rear_end_selection == True:
     LEFT.mass = 40
     LEFT.speedx = 3
     MIDDLE.mass = 21
     MIDDLE.speedx = 2
     RIGHT.mass = 22
     RIGHT.speedx = 0.1

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
      print("Button or selection malfunctioned!")
      raise NameError

#extra variables
hit_count = 0


#game loop
game_start = True
running = True



#Main Game Loop
#////////////////////////////////////////////////////////////////
while running:
    #keep loop running at correct speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #close window
        if event.type == pygame.QUIT:
            running = False
   
    
    #Code for collisions between the LEFT and MIDDLE block
    first_hit = pygame.sprite.collide_rect(LEFT, MIDDLE)


    if first_hit:
        # Statements to handle head on collisions vs collisions where one object pushes another
        if LEFT.speedx_sign == MIDDLE.speedx_sign and LEFT.speedx_sign == 1:
            collider = LEFT
            projectile = MIDDLE
        #Extra logic to handle all permutations of rear end collisions
        elif LEFT.speedx_sign == MIDDLE.speedx_sign and LEFT == -1:
            collider = MIDDLE
            projectile = LEFT
        else:
            first_hit_objs = [LEFT, MIDDLE]
            first_hit_objs = bubble_sort(first_hit_objs)
            collider = first_hit_objs[-1]
            projectile = first_hit_objs[-2]
            print("velocity of fastest", first_hit_objs[-1].name)
            print("should stop:", first_hit_objs[-1].name)


        #Moves blocks away from each other so they dont get stuck

        collider.speedx, projectile.speedx, momentum = velocity_finder_simple_3(collider.speedx, collider.mass, projectile.speedx, projectile.mass)

        collider_space_sign = -1 * collider.speedx_sign
        projectile_space_sign = -1 * projectile.speedx_sign

        collider.float_position_x += 30 * collider_space_sign
        projectile.float_position_x += 10 * projectile_space_sign

        hit_count+=1

    
    #Code for collisions between the RIGHT and MIDDLE block 
    second_hit = pygame.sprite.collide_rect(RIGHT, MIDDLE)

    if second_hit:

        # Statements to handle head on collisions vs collisions where one object pushes another
        if RIGHT.speedx_sign == MIDDLE.speedx_sign and RIGHT.speedx == -1:
            collider = RIGHT
            projectile = MIDDLE
        #Extra logic to handle all permutations of rear end collisions
        elif RIGHT.speedx_sign == MIDDLE.speedx_sign and RIGHT.speedx == 1:
            collider = MIDDLE
            projectile = RIGHT
        else:
            first_hit_objs = [RIGHT, MIDDLE]
            first_hit_objs = bubble_sort(first_hit_objs)
            collider = first_hit_objs[-1]
            projectile = first_hit_objs[-2]
            print("velocity of fastest", first_hit_objs[-1].name)
            print("should stop:", first_hit_objs[-1].name)

        collider.speedx , projectile.speedx, momentum = velocity_finder_simple_3(collider.speedx, collider.mass, projectile.speedx, projectile.mass)

        collider_space_sign = -1 * collider.speedx_sign
        projectile_space_sign = -1 * projectile.speedx_sign

        collider.float_position_x += 30 * collider_space_sign
        projectile.float_position_x += 10 * projectile_space_sign

        
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
    
    # All text on screen 
    draw_txt(screen, f"Block 1 speed: {str(round(LEFT.speedx, sig_digs))}m/s and mass: {str(round(LEFT.mass,sig_digs))}kg", 18, LEFT.text_color, (200), 20)

    draw_txt(screen, f"Block 1 kinetic energy: {str(round(LEFT.kinetic_energy, sig_digs))}J", 18, LEFT.text_color, (200), 40)

    draw_txt(screen, f"Block 2 speed: {str(round(MIDDLE.speedx, sig_digs))}m/s and mass: {str(round(MIDDLE.mass, sig_digs))}kg", 18, MIDDLE.text_color, (WIDTH/2), 20)

    draw_txt(screen, f"Block 2 kinetic energy: {str(round(MIDDLE.kinetic_energy, sig_digs))}J", 18, MIDDLE.text_color, (WIDTH/2), 40)

    draw_txt(screen, f"Block 3 speed: {str(round(RIGHT.speedx, sig_digs))}m/s and mass {str(round(RIGHT.mass, sig_digs))}kg", 18, RIGHT.text_color, (WIDTH-200), 20)

    draw_txt(screen, f"Block 3 kinetic energy: {str(round(RIGHT.kinetic_energy, sig_digs))}J", 18, RIGHT.text_color, (WIDTH-200), 40)

    
    draw_txt(screen, f"The total kinetic energy of the system is {str(round_total_kinetic_energy)}J.", 20, RED, (WIDTH/2), (HEIGHT-20))

    draw_txt(screen, f"The total momentum of the system is {str(round_total_momentum)}Ns.", 20, RED, (WIDTH/2), (HEIGHT-40))

    draw_txt(screen, f"The number of collisions = {str(hit_count)}.", 20, RED, (WIDTH/2), (HEIGHT-60))

    #flips display after drawing everything
    pygame.display.flip()

pygame.quit()
