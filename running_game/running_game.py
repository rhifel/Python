import pygame
from sys import exit
from time import sleep
from random import randint

# Display Score
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_txt = font_style.render(f"Score: {current_time:01}", False, "#E999DC")
    score_rect = score_txt.get_rect(center = (400, 50))
    screen.blit(score_txt, score_rect)
    return current_time

# Added new obstacles
def obstacle_movement(obstacle_list):
    
    for obstacle_item in obstacle_list:
        obstacle_item.x -= 5
        
        if obstacle_item.bottom == 300:  screen.blit(snail_img,obstacle_item)
        else:   screen.blit(fly_img,obstacle_item)
        
    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
    
    # if obstacle_list:
    #     print(f"current item:", obstacle_list[0])
    # else:
    #     print("No Obstacle")
    return obstacle_list
    
# New Collision Mechanics
def collisions(player, obstacles):
    for obstacles_rect in obstacles:
        if player.colliderect(obstacles_rect):  return False
    
    return True

# initialize pygame
pygame.init()

# Display 
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

# initialize clock
clock = pygame.time.Clock()

start_time = 0
score = 0
game_active = False
player_grav = 0

# Font Style
font_style = pygame.font.Font('fonts/Pixeltype.ttf', 50) 

# Background Images
sky_img = pygame.image.load('graphics/Sky.png').convert()
ground_img = pygame.image.load('graphics/ground.png').convert()

# Output Text
quit_txt = font_style.render("Press Q to Quit", False, "#085C5C")
quit_rect = quit_txt.get_rect(center = (400, 350))

over_txt = font_style.render("Press Space to Play", False, "#085C5C")
over_rect = over_txt.get_rect(center = (400, 50))

# Obstacles
# Snails
snail_img = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_rect = snail_img.get_rect(midbottom = (700, 300))

# Flies
fly_img = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

# Obstacle List
obstacle_rect_list = []

# Player Variables
player_img = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_img.get_rect(midbottom = (100, 300)) # use rectangle to have more control of the image

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
# player_jump_rect = player_stand.get_rect(center = (100, 280))

# Obstacle Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300: # click and use mouse cursor to make the player jump
                    player_grav = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_grav = -20
                    
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit() 
            if event.type == obstacle_timer:
                if randint(0,2):    obstacle_rect_list.append(snail_img.get_rect(midbottom = (randint(900, 1100), 300)))
                else:   obstacle_rect_list.append(fly_img.get_rect(midbottom = (randint(900, 1100), 210)))
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                sleep(1)
                game_active = True
                # snail_rect.left = 800
                start_time = pygame.time.get_ticks()
                
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()            
                
    if game_active:      
        # Background Position        
        screen.blit(sky_img,(0, 0))
        screen.blit(ground_img,(0, 300)) 
        
        # Output Text Frame
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 0 , 5,)
        # screen.blit(score_txt,score_rect)
        score = display_score()
        
        # Snail Loop and Positon
        # snail_rect.x -= 5
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_img,snail_rect)

        # Player Position
        player_grav += 1
        player_rect.y += player_grav
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_img,player_rect)
        
        # if player_grav == -20:
        #     screen.blit(player_jump,player_jump_rect)
        
        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        # Collisions
        # if snail_rect.colliderect(player_rect):
        #     game_active = False
        # New mechanics
        game_active = collisions(player_rect,obstacle_rect_list)
            
    else:
        # Intro Screen Display
        screen.fill("#83B99A")
         
        score_txt = font_style.render(f"Your Score: {score}", False, "#085C5C")
        score_txt_rect = score_txt.get_rect(center = (400, 350))
        
        screen.blit(player_stand, player_stand_rect)
        
        obstacle_rect_list.clear()
        player_rect.midbottom = (100, 300)
        
        if score == 0:
            screen.blit(over_txt,over_rect)
            screen.blit(quit_txt,quit_rect)
        # Intro Screen after collision
        else: screen.blit(score_txt,score_txt_rect)

        
    pygame.display.update()
    clock.tick(60)

