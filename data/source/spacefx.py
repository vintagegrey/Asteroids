import pygame, random

class SpaceFX(pygame.sprite.Sprite):
    def __init__(self, posX, posY, fxWidth, fxHeight):
        super().__init__()
        spriteChoice = random.randint(1, 3)
        if spriteChoice == 1:
            self.image = pygame.image.load("data/textures/star_c_big.png").convert_alpha()
        if spriteChoice == 2:
            self.image = pygame.image.load("data/textures/star_b_big.png").convert_alpha()
        if spriteChoice == 3:
            self.image = pygame.image.load("data/textures/star_y_big.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.fxWidth = fxWidth
        self.fxHeight = fxHeight
        self.vel = 2

    def update(self, displayHeight):
        if self.vel > 0:
            self.rect.y += self.vel
        if self.rect.y > displayHeight:
            self.kill()