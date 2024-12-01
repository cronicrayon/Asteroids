import pygame
from constants import *

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop()

def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0 # Delta time
    while True:
        dt = timer.tick(60) / 1000
        # code to get the close window button working
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        pygame.Surface.fill(screen, (0,0,0)) # black background on render window
        pygame.display.flip() # updates render window
if __name__ == "__main__":
    main()
