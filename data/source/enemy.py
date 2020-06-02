import pygame, random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, posX, posY, enemyWidth, enemyHeight):
        super().__init__()
        spriteChoice = random.randint(1, 2)
        if spriteChoice == 1:
            self.image = pygame.image.load("data/textures/asteroid_col.png").convert_alpha()
        if spriteChoice == 2:
            self.image = pygame.image.load("data/textures/asteroid_broke.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.enemyWidth = enemyWidth
        self.enemyHeight = enemyHeight
        self.vel = 2

    def update(self, displayHeight):
        self.rect.y += self.vel
        if self.rect.y > displayHeight:
            self.kill()

    def checkCollision(self, group1, playerGroup, kill1, kill2):
        pygame.sprite.groupcollide(group1, playerGroup, kill1, kill2)

        if len(playerGroup) == 0:
            player.gameOver()

# finish
class Alien(Asteroid):
    def __init__(self, posX, posY, enemyWidth, enemyHeight):
        super().__init__(posX, posY, enemyWidth, enemyHeight)
        vel = 3

    def update(self, playerPosX):
        self.rect.y += self.vel 

# finish
class AlienProjectile(Asteroid):
    def __init__(self, posX, posY, bulletWidth, bulletHeight):
        super().__init__(posX, posY, bulletWidth, bulletHeight)
        vel = 7

    def update(self, displayHeight):
        self.rect.y += self.vel
        if self.rect.y > displayHeight:
            self.kill()