from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self,x:int, y:int) -> None:
        pass
