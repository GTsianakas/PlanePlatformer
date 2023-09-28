import math

from physics_vectors import Vector2D, PhysicsObject, convert_coords_to_vector

class Physics():

    def __init__(self, dt = 1):
        self.dt = dt


    def apply_gravity(self, pobject: PhysicsObject, g: float = 3.2) -> None:
        pobject.speed.y = pobject.speed.y - g

    def apply_drag(self, pobject: PhysicsObject, coef: float = 0.02) -> None:
        pobject.speed = pobject.speed * (1-coef) * self.dt
        

    def apply_lift(self, pobject: PhysicsObject, coef: float = 1.2, K = 10) -> None:
        (angle, magnitude) = convert_coords_to_vector(pobject.speed)
        pobject.speed.x += 0.5 * coef * K * magnitude**2 * math.sin(angle)
