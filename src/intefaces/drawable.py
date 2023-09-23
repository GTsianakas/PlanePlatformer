from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self,x:int, y:int) -> None:
        pass
    