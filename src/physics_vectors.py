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
        if isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)
        else:
            raise TypeError("Invalid multiplication")

    def __isub__(self, other):
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
            return self
        else:
            raise TypeError("Invalid -=")

    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise TypeError("Invalid +=")

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
        self.acceleration.x = force * math.cos(radians) / self.mass
        self.acceleration.y = force * math.sin(radians) / self.mass

    def __str__(self):
        return f"PhysicsObject(acc={self.acceleration}, speed={self.speed}, mass={self.mass})"



def convert_coords_to_vector(coords: Vector2D) -> tuple[float,float]:
    if coords.x == 0 and coords.y == 0:
        return (0, 0)
    angle = math.atan2(coords.y, coords.x)
    magnitude = math.sqrt(coords.x ** 2 + coords.y ** 2)

    return (angle, magnitude)


def rotate_vector(vector: Vector2D, angle_degrees: float) -> Vector2D:
    angle_radians = math.radians(angle_degrees)
    x_new = vector.x * math.cos(angle_radians) - vector.y * math.sin(angle_radians)
    y_new = vector.x * math.sin(angle_radians) + vector.y * math.cos(angle_degrees)

    return Vector2D(x_new, y_new)


def normalize_vector(vector: Vector2D, magnitude: float) -> Vector2D:
    if magnitude > 0:
        return Vector2D(vector.x / magnitude, vector.y / magnitude)
    else:
        return Vector2D(0, 0)
