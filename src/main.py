import pygame
import configparser

from plane import Plane

p = Plane()

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
                
        screen.fill("blue")
        update()
        
        render(screen)

        pygame.display.flip()
        clock.tick(int(config['GAME']['MAX_FPS']))
    
    pygame.quit()


def update() -> None:
    p.move()
    
def render(screen: pygame.Surface) -> None:
    rotated_image, image_rect = p.draw(screen)
    screen.blit(rotated_image, image_rect)

if __name__ == "__main__":
    main()


