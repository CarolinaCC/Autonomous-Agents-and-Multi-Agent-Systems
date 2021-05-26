from gui.game import Game
import matplotlib as plt

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
