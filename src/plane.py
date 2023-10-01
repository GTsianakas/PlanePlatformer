import pygame
import math

from interfaces import drawable, movable, controllable
from physics_vectors import Vector2D, PhysicsObject
from physics import Physics

class Plane(drawable.Drawable, movable.Movable, controllable.Control):

    def __init__(self, position: Vector2D = Vector2D(100,500), 
                 physical_entity: PhysicsObject = PhysicsObject(),
                 physics_world: Physics = Physics(), 
                 thrust=0.001, turn_rate=50):
                 
        self.position = position
        self.physical_entity = physical_entity
        self.physics_world = physics_world

        self.thrust = thrust
        self.turn_rate = turn_rate
        self.angle = 0

        self.fire_rate = 10
        self.max_thrust = 0.1

    def move(self) -> None:
        self.physical_entity.add_force(self.thrust, -self.angle, self.physics_world.dt)

        self.physics_world.apply_gravity(self.physical_entity)
        self.physics_world.apply_drag(self.physical_entity)
        self.physics_world.apply_lift(self.physical_entity,self.angle)

        self.physical_entity.speed += self.physical_entity.acceleration
        self.position += self.physical_entity.speed

        self.control()
        print(f'thrust:{self.thrust}\tpos:{self.position}')

    def draw(self, screen: pygame.Surface) -> tuple:
        plane_img = pygame.image.load("../assets/plane.png")
        scaled_image = pygame.transform.scale(plane_img, (40, 20))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        image_rect = rotated_image.get_rect()
        image_rect.center = (self.position.x, self.position.y)
        return (rotated_image, image_rect)

    def control(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.thrust < self.max_thrust:
            self.thrust += self.max_thrust/100
        if keys[pygame.K_s] and self.thrust > 0:
            self.thrust -= self.max_thrust/100
        if keys[pygame.K_a]:
            temp_angle: float = self.angle + self.turn_rate * self.physics_world.dt
            if (temp_angle > 360):
                self.angle = temp_angle - 360
            else:
                self.angle = temp_angle
        if keys[pygame.K_d]:
            temp_angle: float = self.angle - self.turn_rate * self.physics_world.dt
            if (temp_angle < 0):
                self.angle = temp_angle + 360
            else:
                self.angle = temp_angle



