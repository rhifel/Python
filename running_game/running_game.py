import pygame
import sys

# initialize pygame
pygame.init()

# Display 
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

# initialize clock
clock = pygame.time.Clock()

# Games States
game_active = True

# Font Style
font_style = pygame.font.Font('fonts/Pixeltype.ttf', 50) 

# Background Images
sky_img = pygame.image.load('graphics/Sky.png').convert()
ground_img = pygame.image.load('graphics/ground.png').convert()

# Output Text
score_txt = font_style.render("Score: ", False, "#E999DC")
score_rect = score_txt.get_rect(center = (400, 50))

# Snail 
snail_img = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_img.get_rect(midbottom = (700, 300))

# Player
player_img = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_img.get_rect(midbottom = (100, 300)) # use rectangle to have more control of the image
player_grav = 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_grav = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_grav = -20
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                
    if game_active:      
        # Background Position        
        screen.blit(sky_img,(0, 0))
        screen.blit(ground_img,(0, 300)) 
        
        # Output Text Frame
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 0 , 5,)
        screen.blit(score_txt,score_rect)
        
        # Snail Loop and Positon
        snail_rect.x -= 5
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_img,snail_rect)

        # Player Keys and Position
        player_grav += 1
        player_rect.y += player_grav
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_img,player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('#000000')
        #game_over = pygame.image.load('graphics/game_over.png').convert_alpha()
        #screen.blit(game_over,(0, 0))
        
    pygame.display.update()
    clock.tick(60)

