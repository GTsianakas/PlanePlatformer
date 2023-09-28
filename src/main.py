import pygame
import configparser

def main() -> None:
    config = configparser.ConfigParser()
    config.read('../settings.ini')
    pygame.init()
    
    screen = pygame.display.set_mode((int(config['GAME']['WIDTH']),
                                      int(config['GAME']['HEIGHT']))
                                     )
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("purple")
        update()
        
        render()

        pygame.display.flip()
        clock.tick(int(config['GAME']['MAX_FPS']))
    
    pygame.quit()


def update() -> None:
    pass
    
def render() -> None:
    pass

if __name__ == "__main__":
    main()


