import pygame

class DebugMenu(object):
    def __init__(self, font, fpsClock, player, foregroundColor):
        self.font = font
        self.fpsClock = fpsClock
        self.player = player
        self.foregroundColor = foregroundColor

    def fpsCounter(self):
        fps = str(int(self.fpsClock.get_fps()))
        fpsText = self.font.render(fps + " FPS", 1, self.foregroundColor, pygame.Color("Black"))
        return fpsText

    def currentPos(self):
        posText = self.font.render("X: " + str(self.player.rect.x) + ", Y: " + str(self.player.rect.y), 1, self.foregroundColor, pygame.Color("Black"))
        return posText

    def entityAmount(self, enemyList, fxList, projectileList):
        text = self.font.render("Enemies: " + str(len(enemyList)) + " - Projectiles: " + str(len(projectileList)), 1, self.foregroundColor, pygame.Color("Black"))
        return text