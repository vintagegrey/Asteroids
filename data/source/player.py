import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY, playerWidth, playerHeight):
        super().__init__()
        self.image = pygame.image.load("data/textures/player_col.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.playerWidth = playerWidth
        self.playerHeight = playerHeight
        self.vel = 2 

        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False

    def update(self, displayWidth, displayHeight):
        if self.moveRight and self.rect.x < displayWidth - self.playerWidth - self.vel:
            self.rect.x += self.vel
        if self.moveLeft and self.rect.x > self.vel:
            self.rect.x -= self.vel
        if self.moveUp and self.rect.y > self.vel:
            self.rect.y -= self.vel
        if self.moveDown and self.rect.y < displayHeight - self.playerHeight - self.vel:
            self.rect.y += self.vel

class PlayerProjectile(pygame.sprite.Sprite):
    def __init__(self, posX, posY, bulletWidth, bulletHeight, player):
        super().__init__()
        self.image = pygame.image.load("data/textures/player_bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.bulletWidth = bulletWidth
        self.bulletHeight = bulletHeight
        self.vel = 7

    def update(self):
        self.rect.y -= self.vel
        if self.rect.y < 0:
            self.kill()

    def checkCollision(self, group1, enemyGroup, kill1, kill2):
        pygame.sprite.groupcollide(group1, enemyGroup, kill1, kill2)