import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from time import sleep as slp

from colors import *
from pygame_config import *

def init_game():
    pygame.init()
    pygame.display.set_caption("El Initials") # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

def draw_line(window,coord1,coord2):
    pygame.draw.line(window, THAYER_GREEN, coord1,coord2, 50)

# Draw Function to update graphics
def draw(window):
    
    window.fill(WHITE)

    #T
    draw_line(window,[10,50], [390,50])
    draw_line(window,[200,50], [200,780])

    #Y
    draw_line(window, [600,780], [600,400])
    draw_line(window, [420,30], [600,400])
    draw_line(window, [750,30], [600,400])

    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    return True

def main(): # MAIN FUNCTION
    window = init_game()
    clock = pygame.time.Clock()

    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: # QUIT
        #         run = False
        #         break
        
        draw(window) # UPDATES SCREEN


    pygame.quit()
    quit()

if __name__ == "__main__": 
    main()

