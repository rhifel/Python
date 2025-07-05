import pygame
from sys import exit
from time import sleep
from random import randint, choice
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # For PyInstaller temp path
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(resource_path("graphics/Player/player_walk_1.png")).convert_alpha()
        player_walk_2 = pygame.image.load(resource_path("graphics/Player/player_walk_2.png")).convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(resource_path('graphics/Player/jump.png')).convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.grav = 0
        
        self.jump_sound = pygame.mixer.Sound(resource_path('audio/jump.mp3'))
        self.jump_sound.set_volume(0.5)
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.grav = -20
            self.jump_sound.play()
            
        # mouse = pygame.mouse.get_pressed()
        # mouse_pos = pygame.mouse.get_pos()
        # if any(mouse):
        #     if self.rect.collidepoint(mouse_pos) and self.rect.bottom >= 300:
        #         self.grav = -20

    def apply_grav(self):
        self.grav += 1
        self.rect.y += self.grav
        if self.rect.bottom >= 300: 
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
                
    def update(self):
        self.player_input()
        self.apply_grav()
        self.animation_state()

# Obstacle Class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            fly_img_1 = pygame.image.load(resource_path("graphics/Fly/Fly1.png")).convert_alpha()
            fly_img_2 = pygame.image.load(resource_path("graphics/Fly/Fly2.png")).convert_alpha()
            self.frames = [fly_img_1, fly_img_2]
            y_pos = 210
            
        else:
            snail_img_1 = pygame.image.load(resource_path("graphics/snail/snail1.png")).convert_alpha()
            snail_img_2 = pygame.image.load(resource_path("graphics/snail/snail2.png")).convert_alpha()
            self.frames = [snail_img_1, snail_img_2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100),y_pos))
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        
    def update(self):
        self.animation_state()
        self.rect.x -= 5
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        
# Display Score
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_txt = font_style.render(f"Score: {current_time:01}", False, "#E999DC")
    score_rect = score_txt.get_rect(center=(400, 50))
    screen.blit(score_txt, score_rect)
    return current_time


def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True

# initialize pygame
pygame.init()

# Display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

# initialize clock
clock = pygame.time.Clock()

start_time = 0
score = 0
game_active = False
player_grav = 0

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Font Style
font_style = pygame.font.Font(resource_path("fonts/Pixeltype.ttf"), 50)

# Background Images
sky_img = pygame.image.load(resource_path("graphics/Sky.png")).convert()
ground_img = pygame.image.load(resource_path("graphics/ground.png")).convert()

# Background Music
bg_music = pygame.mixer.Sound(resource_path('audio/music.wav'))
bg_music.set_volume(0.4)
bg_music.play(loops= -1)

# Intro screen Player Image and Output Text
quit_txt = font_style.render("Press Q to Quit", False, "#085C5C")
quit_rect = quit_txt.get_rect(center=(400, 350))

over_txt = font_style.render("Press Space to Play", False, "#085C5C")
over_rect = over_txt.get_rect(center=(400, 50))

player_stand = pygame.image.load(resource_path("graphics/Player/player_stand.png")).convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Obstacle Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1800)


1
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q: 
                    pygame.quit()
                    exit()
                    
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','snail','fly','snail'])))
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    sleep(1)
                    game_active = True
                    start_time = pygame.time.get_ticks()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()

    if game_active:
        # Background Position
        screen.blit(sky_img, (0, 0))
        screen.blit(ground_img, (0, 300))

        # Output Text Frame
        score = display_score()

        # Player Position
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Collisions
        game_active = collisions_sprite()
        
    else:
        # Intro Screen Display
        screen.fill("#83B99A")

        score_txt = font_style.render(f"Your Score: {score}", False, "#085C5C")
        score_txt_rect = score_txt.get_rect(center=(400, 100))

        screen.blit(player_stand, player_stand_rect)

        if score == 0:
            screen.blit(over_txt, over_rect)
            screen.blit(quit_txt, quit_rect)
        # Intro Screen after collision
        else:   screen.blit(score_txt, score_txt_rect)

    pygame.display.update()
    clock.tick(60)
