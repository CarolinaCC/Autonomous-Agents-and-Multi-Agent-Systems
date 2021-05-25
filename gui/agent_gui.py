import pygame


class Agent_gui:
    hovered = False

    def __init__(self, text, pos, display, font, number):
        self.text = text
        self.pos = pos
        self.display = display
        self.font = font
        self.number = number
        self.player_avatar = pygame.image.load("gui/assets/players/" + str(self.number) + ".png")
        self.offset_x = - 10
        self.offset_y = 60
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        self.display.blit(self.player_avatar, self.pos)
        rect = pygame.Surface((self.rend.get_width(), self.rend.get_height()), pygame.SRCALPHA, 32)
        rect.fill((23, 100, 255, 150))
        self.display.blit(rect, (self.pos[0] + self.offset_x, self.pos[1] + self.offset_y))
        self.display.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return 252, 119, 3
        else:
            return 255, 255, 255

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = (self.pos[0] + self.offset_x, self.pos[1] + self.offset_y)
