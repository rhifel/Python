import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
running = True
font_style = pygame.font.Font('fonts/Pixeltype.ttf', 50)

sky_image = pygame.image.load('graphics/Sky.png').convert()
ground_image = pygame.image.load('graphics/ground.png').convert()

text_style = font_style.render("The Running Game", False, 'Purple')

snail_image = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_pos_x = 700 # snail initial position
# tried putting here the snail_rect but the looping stop need to put it below

player_image = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_image.get_rect(midbottom = (100,300)) # use rectangle to have more control of the image

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(sky_image,(0,0))
    screen.blit(ground_image,(0,300))
    screen.blit(text_style,(280,20))
    
    snail_pos_x -= 4
    if snail_pos_x < -100: snail_pos_x = 800 #looping the snail
    snail_rect = snail_image.get_rect(midbottom = (snail_pos_x,300)) # snail_rect needs to be here
    screen.blit(snail_image,snail_rect)

    screen.blit(player_image,player_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()