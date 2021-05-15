import pygame


class Agent_gui:

    hovered = False

    def __init__(self, text, pos, display, font):
        self.text = text
        self.pos = pos
        self.display = display
        self.font = font
        self.set_rect()
        self.draw()


    def draw(self):
        self.set_rend()
        self.display.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos