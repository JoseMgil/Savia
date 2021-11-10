# Pygame development 1
# Star the basic game set up 
# Set up the display

import pygame
from GameClass import Game



SCREEN_WIDHT = 800 
SCREEN_HEIGHT = 800 
SCREN_TITLE = 'Savia GAME'
       
# We need to Init the pygame library 
pygame.init()

new_game = Game(SCREN_TITLE, SCREEN_WIDHT, SCREEN_HEIGHT)
new_game.run_game()


pygame.quit()
quit()
