import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Wall Street Bets', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class OptionsMenu(Menu):

    def __init__(self, game, agents, steps):
        Menu.__init__(self, game)
        self.state = 0

        mid_h_offset = 20
        for x in agents:
            x.append(self.mid_w)
            x.append(self.mid_h + mid_h_offset)
            mid_h_offset+=20

        self.stepx, self.stepy = self.mid_w, self.mid_h + mid_h_offset
        self.states = agents
        self.states.append(['steps',steps, self.stepx, self.stepy])
        self.cursor_rect.midtop = (self.states[0][2] + self.offset, self.states[0][3])

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            for x in self.states:
                self.game.draw_text(str(x[0]) + " - " + str(x[1]), 15, x[2], x[3])
            #self.game.draw_text("Number of Steps - " + str(self.steps), 15, self.stepx, self.stepy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):

        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.game.UP_KEY:
                if self.state > 0:
                    self.state -=1
                else:
                    self.state = len(self.states) - 1
            elif self.game.DOWN_KEY:
                if self.state < len(self.states) - 1:
                    self.state +=1
                else:
                    self.state = 0

            self.cursor_rect.midtop = (self.states[self.state][2] + self.offset, self.states[self.state][3])


        elif self.game.RIGHT_KEY:
           self.states[self.state][1] +=1
        elif self.game.LEFT_KEY:
            if self.states[self.state][1] > 0:
                self.states[self.state][1] -= 1


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Carolina, João, Sebastião', 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
