import pygame, sys, random
from data.source.player import Player, PlayerProjectile
from data.source.enemy import Asteroid, Alien, AlienProjectile
from data.source.spacefx import SpaceFX
from data.source.debugmenu import DebugMenu
pygame.init() 

pygame.display.set_caption("Asteroids!")

D_WIDTH = 500
D_HEIGHT = 500
DISPLAY = pygame.display.set_mode((D_WIDTH, D_HEIGHT))

ICON = pygame.image.load("data/textures/player_col.png").convert_alpha()
pygame.display.set_icon(ICON)

FPS = 144
FPSCLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("2Credits", 32)

BACKGROUND = (0, 0, 0) # Darkest color
FOREGROUND = (255, 255, 255) # Brightest color

MAXENEMIES = 15 # Max value is around 220 before the loop has trouble keeping up
MAXFX = 50 # Max value is around 130 ^^^

showDebug = True

def redrawFrame():
    DISPLAY.fill(BACKGROUND)
    fx_list.draw(DISPLAY)
    fx_list.update(D_HEIGHT)

    player_list.draw(DISPLAY)
    player_list.update(D_WIDTH, D_HEIGHT)

    projectiles_list.draw(DISPLAY)
    projectiles_list.update()
    playerprojectile.checkCollision(projectiles_list, enemy_list, True, True)

    enemy_list.draw(DISPLAY)
    enemy_list.update(D_HEIGHT)
    enemy.checkCollision(enemy_list, player_list, True, False)
    
    if showDebug == True:
        DISPLAY.blit(FONT.render("bruhnk mobile", 1, FOREGROUND, pygame.Color("Black")), (10, 0))
        DISPLAY.blit(debug.entityAmount(enemy_list, fx_list, projectiles_list), (10, 25))
        DISPLAY.blit(debug.fpsCounter(), (10, 50))
        DISPLAY.blit(debug.currentPos(), (10, 75))

    pygame.display.update()

# Sprite groups 
enemy_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
fx_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
projectiles_list = pygame.sprite.Group()

# Making player 
player = Player(D_WIDTH / 2, 440, 32, 32)
playerprojectile = PlayerProjectile(100, 100, 32, 32, player)
# Making debug menu
debug = DebugMenu(FONT, FPSCLOCK, player, (255, 255, 255))

player_list.add(player)
all_sprites.add(player)

while True:
    # Ew this is gross
    # Player movement btw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moveRight = True
            if event.key == pygame.K_LEFT:
                player.moveLeft = True
            if event.key == pygame.K_UP:
                player.moveUp = True
            if event.key == pygame.K_DOWN:
                player.moveDown = True
            if event.key == pygame.K_v:
                showDebug ^= True
            if event.key == pygame.K_x:
                playerprojectile = PlayerProjectile(player.rect.x, player.rect.y - 20, 32, 32, player)
                projectiles_list.add(playerprojectile)
                all_sprites.add(playerprojectile)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moveRight = False
            if event.key == pygame.K_LEFT:
                player.moveLeft = False
            if event.key == pygame.K_UP:
                player.moveUp = False
            if event.key == pygame.K_DOWN:
                player.moveDown = False

    # Add enemies 
    if len(enemy_list) != MAXENEMIES:
        enemy = Asteroid(random.randint(2, D_WIDTH), random.randint(-150, 2), 32, 32)
        enemy_list.add(enemy)
        all_sprites.add(enemy)

    # Add background fx
    if len(fx_list) != MAXFX:
        fx = SpaceFX(random.randint(2, D_WIDTH), random.randint(-250, 2), 32, 32)
        fx_list.add(fx)
        all_sprites.add(fx)

    # the destruction code
    # for i in range(MAXENEMIES):
    #     enemy = Asteroid(random.randint(2, D_WIDTH), random.randint(-150, 2), 32, 32)
    #     enemy_list.add(enemy)

    redrawFrame()
    FPSCLOCK.tick(FPS)