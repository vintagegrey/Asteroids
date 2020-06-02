import pygame

class MainMenu(object):
    def __init__(self, displayHeight, displayWidth):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.title = pygame.image.load("data/textures/title.png")

    def intro(self):
        # fuckkk