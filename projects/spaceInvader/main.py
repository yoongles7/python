# space invaders using pygame. I made this game following a tutorial from freecodecamp youtube channel https://github.com/attreyabhatt/Space-Invaders-Pygame


import os
import warnings


os.environ['PYGAME_DETECT_AVX2'] = '0'
warnings.filterwarnings("ignore", message="pkg_resources is deprecated")
warnings.filterwarnings("ignore", message="Your system is avx2 capable")   # warning supresion


import pygame
import random
import math
from pygame import mixer


# Initialize the pygame
pygame.init()
clock = pygame.time.Clock()


# Create the screen
screen = pygame.display.set_mode((800, 600))


# Background
background = pygame.image.load('background.png')


# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)


# Title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.8)
    enemyY_change.append(40)


# Bullet


# Ready - you can't see the bullet on the screen
# Fire the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

fontX = 10
fontY = 10


# Game over font
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))
    
    
def player(x, y):
    screen.blit(playerImg, (x, y))

    
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
is_running = True

while is_running:
    screen.fill((0, 0, 0))
    
    # Background Image
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.8
            elif event.key == pygame.K_RIGHT:
                playerX_change = 1.8
            
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
        # Close with Escape key or Q key
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                is_running = False    

    # Player movement
    playerX += playerX_change     
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
        
    # Enemy movement
    for i in range(num_of_enemies):
        
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.8
            enemyY[i] += enemyY_change[i]
        
         # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            
        enemy(enemyX[i], enemyY[i], i)
           
    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    player(playerX, playerY)
    show_score(fontX, fontY)
    
    pygame.display.update()
    
    clock.tick(120)  # limits FPS to 60

    
pygame.quit()