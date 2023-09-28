import math

from dataclasses import dataclass

@dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, other):
        if isinstance(other, (Vector2D)):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Invalid addition")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError("Invalid multiplication")

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __radd__(self, other):
        self + other

    def __rmul__(self, other):
        self * other


class PhysicsObject:

    def __init__(self, acceleration: Vector2D = Vector2D(0,0),
                speed: Vector2D = Vector2D(0,0), mass: float = 1):
        self.acceleration = acceleration
        self.speed = speed
        self.mass = mass

    def add_force(self, force: float, angle: float, dt: float = 1) -> None:
        radians = math.radians(angle)

        self.acceleration.x = force * math.cos(radians) / self.mass #* dt
        self.acceleration.y = force * math.sin(radians) / self.mass #* dt

        self.speed += self.acceleration * dt

    def __str__(self):
        return f"PhysicsObject(acc={self.acceleration}, speed={self.speed}, mass={self.mass})"



def convert_coords_to_vector(coords: Vector2D) -> tuple:
    angle = math.atan2(coords.y, coords.x)
    magnitude = math.sqrt(coords.x**2 + coords.y**2)
    
    return (angle, magnitude)