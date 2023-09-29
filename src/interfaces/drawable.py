from abc import ABC, abstractmethod

import pygame

class Drawable(ABC):
    @abstractmethod
    def draw(self, screen: pygame.Surface) -> tuple:
        pass
    
