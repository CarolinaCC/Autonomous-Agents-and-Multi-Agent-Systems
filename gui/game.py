import pygame

from gui.agent_gui import *
from gui.menu import *
from game_manager import *
import matplotlib.pyplot as plt
import numpy as np

class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.F_KEY = False, False, False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        # self.font_name = '8-BIT WONDER.TTF'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE, self.GREEN, self.RED = (0, 0, 0), (255, 255, 255), (3, 252, 40), (252, 3, 3)
        self.main_menu = MainMenu(self)

        self.agents = [['random_agents', 1], ['simple_react_agents', 1], ['careful_react_agents', 1], ['rl_agent', 1]]
        self.modes = ["DEFAULT", "INFLATION", "RECESSION"]
        self.steps = 500
        self.options = OptionsMenu(self, self.agents, self.steps, self.modes)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.setup = True
        self.array_agents_gui = []
        self.game_manager = 0
        self.bg = pygame.image.load("gui/assets/background-game.png")

        self.x_breaking, self.y_breaking = -100, 580
        self.players_pos_array = [[230, 320], [360, 320], [500, 320], [155, 400], [560, 400], [230, 490], [360, 490],
                                  [500, 490]]

        self.show_plot = False
        self.c_game_over = 0

    def game_loop(self):
        while self.playing:
            if self.setup:
                self.game_manager = GameManager(self.options.states[0][1], self.options.states[1][1],
                                                self.options.states[2][1], self.options.states[3][1],
                                                self.options.states[-2][1],
                                                self.modes[self.options.states[-1][1]])
                self.setup = False

                c = 0
                for x in self.game_manager.agents_array:
                    self.array_agents_gui.append(
                        Agent_gui(x.type, (self.players_pos_array[c][0], self.players_pos_array[c][1]), self.display,
                                  pygame.font.Font(self.font_name, 20), c))
                    c += 1

            self.check_events()

            if self.ESCAPE_KEY:
                self.playing = False
                pygame.quit()
                exit()

            if self.RIGHT_KEY:
                self.game_manager.step(1)

            if self.UP_KEY:
                self.game_manager.step(1000)

            if self.F_KEY:
                self.game_manager.step(self.options.states[-2][1])

            self.display.fill(self.BLACK)
            self.display.blit(self.bg, (0, 0))

            for x in range(len(self.array_agents_gui)):
                if self.array_agents_gui[x].rect.collidepoint(pygame.mouse.get_pos()):
                    self.array_agents_gui[x].hovered = True

                    self.draw_text('CASH AVAILABLE - ' + f'{self.game_manager.agents_array[x].get_cash_value():.2f}',
                                   15, 55, 70, self.WHITE)
                    self.draw_text('VALUE - ' + f'{self.game_manager.agents_array[x].get_value():.2f}', 15, 55, 90,
                                   self.WHITE)
                    self.draw_text('STOCKS VALUE - ' + f'{self.game_manager.agents_array[x].get_stock_value():.2f}', 15,
                                   55, 110, self.WHITE)

                    self.display.blit(self.array_agents_gui[x].player_avatar, (290, 50))
                    self.draw_text(self.game_manager.agents_array[x].type, 15, 290, 115, self.WHITE)

                    cx = 0
                    cy = 0
                    for y in self.game_manager.agents_array[x].get_stocks_owned():
                        self.draw_text(self.game_manager.central_bank.get_stock(y).name + ' - ' +
                                       f'{self.game_manager.agents_array[x].get_stocks_owned_by_id_price(y):.2f}' + '€',
                                       12, 55 + cx, 130 + cy, self.WHITE)
                        cy += 20
                        if cy > 100:
                            cy = 0
                            cx += 120


                else:
                    self.array_agents_gui[x].hovered = False
                self.array_agents_gui[x].draw()

            has_ended = ''


            if self.game_manager.has_ended():
                has_ended += ' - GAME IS OVER'
                if self.c_game_over == 0:
                    self.show_plot = True
                else:
                    self.show_plot = False
                self.c_game_over += 1

            self.draw_text(
                'Current Step - ' + str(self.game_manager.current_step) + '/' + str(
                    self.game_manager.steps_num) + has_ended, 18, 55,
                35, self.BLACK)
            self.draw_text('Stocks', 15, 470, 6, self.WHITE)
            self.draw_text('Price', 15, 547, 6, self.WHITE)
            self.draw_text('Variation', 15, 608, 6, self.WHITE)

            c = 31

            for stock in self.game_manager.central_bank.stocks:
                self.draw_text(stock.name, 12, 470, c, self.WHITE)
                self.draw_text(f'{stock.price:.2f}' + ' €', 12, 553, c, self.WHITE)
                if stock.get_percentage_variation() >= 0:
                    color_chart = self.GREEN
                else:
                    color_chart = self.RED
                self.draw_text(f'{stock.get_percentage_variation():.2f}' + ' %', 12, 620, c, color_chart)
                c += 25

            self.draw_text('Breaking News - ' + self.game_manager.get_current_event(), 15, self.x_breaking,
                           self.y_breaking, self.WHITE)
            self.x_breaking += 2
            if self.x_breaking > self.DISPLAY_W:
                self.x_breaking = - 200
            self.draw_text('Mode - ' + self.game_manager.game_mode, 15, 320, 440, self.WHITE)

            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

            if (self.show_plot):
                ## PLOT DOS PREÇOS DO MERCADO
                plt.figure(1)
                for stock in self.game_manager.stocks:
                    x = np.arange(len(stock.price_history))
                    y = stock.price_history
                    plt.plot(x, y, label=stock.name)

                plt.title("Stock Price per Step")
                plt.xlabel("steps")
                plt.ylabel("price €")
                plt.legend()

                #

                plt.figure(2)
                ## PLOT AGENT CASH BY STEP
                for agent in self.game_manager.agents_array:
                    x = np.arange(len(agent.cash_history))
                    y = agent.cash_history
                    plt.plot(x, y, label=agent.type)

                plt.title("Agent Cash per Step")
                plt.xlabel("steps")
                plt.ylabel("Cash €")
                plt.legend()

                plt.figure(3)
                ## PLOT AGENT Invested BY SETP
                for agent in self.game_manager.agents_array:
                    x = np.arange(len(agent.stock_history))
                    y = agent.stock_history
                    plt.plot(x, y, label=agent.type)

                plt.title("Agent Invested Money per Step")
                plt.xlabel("steps")
                plt.ylabel("€")
                plt.legend()

                plt.figure(4)
                ## PLOT AGENT Cash + Stock BY STEP
                for agent in self.game_manager.agents_array:
                    l = len(agent.value_history)
                    x = np.arange(l)
                    y = agent.value_history
                    plt.plot(x, y, label=agent.type)

                plt.title("Agent Cash + Stock per Step")
                plt.xlabel("steps")
                plt.ylabel("value €")
                plt.legend()
                #
                plt.show()
                self.show_plot = False

        # print results to file for analysis
        # self.game_manager.print_results()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_f:
                    self.F_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.F_KEY = False, False, False, False, False, False, False, False

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.display.blit(text_surface, text_rect)
