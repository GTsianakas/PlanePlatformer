import math

from physics_vectors import Vector2D, PhysicsObject, convert_coords_to_vector

class Physics():

    def __init__(self, dt = 0.01):
        self.dt = dt

    def apply_gravity(self, pobject: PhysicsObject, g: float = 0.1) -> None:
        pobject.speed.y = pobject.speed.y + g * self.dt

    def apply_drag(self, pobject: PhysicsObject, coef: float = 0.0002) -> None:
        pobject.speed = pobject.speed * (1-coef)

    def apply_lift(self, pobject: PhysicsObject, coef: float = 0.8, K = 1) -> None:
        (angle, magnitude) = convert_coords_to_vector(pobject.speed)
        pobject.speed.y -= 0.5 * coef * K * magnitude**2 * (math.sin(angle) + 0.1) * self.dt
