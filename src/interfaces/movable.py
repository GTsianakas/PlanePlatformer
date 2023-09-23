import sys
sys.path.append('..')

from abc import ABC, abstractmethod
from physics_vectors import Velocity

class Movable(ABC):
    @abstractmethod
    def move(self,x:int, y:int) -> None:
        pass

    @abstractmethod
    def get_velocity(self) -> Velocity:
        pass
