from interfaces import drawable, movable
from physics_vectors import Vector2D, PhysicsObject
from physics import Physics

class Plane(drawable.Drawable, movable.Movable):

    def __init__(self, position: Vector2D = Vector2D(0,0), 
                 physical_entity: PhysicsObject = PhysicsObject(),
                 physics_world: Physics = Physics(), 
                 lift: float=5, thrust=10, turn_rate=10):
        self.position = position
        self.physical_entity = physical_entity
        self.physics_world = physics_world

        self.thrust = thrust
        self.turn_rate = turn_rate
        self.angle = 90

        self.fire_rate = 10
        self.max_power = 100

    def move(self) -> None:
        #need to check direction
        #angle_change = self.turn_rate * dt
        self.physical_entity.add_force(self.thrust, self.angle, self.physics_world.dt)

        self.physics_world.apply_gravity(self.physical_entity)
        self.physics_world.apply_drag(self.physical_entity)
        self.physics_world.apply_lift(self.physical_entity)

        self.position += self.physical_entity.speed

    def draw(self):
        pass
    

a = Plane()


#print(a.physical_entity)
a.move()
a.move()

# print(a.physical_entity)
# a.move()
# print(a.physical_entity)
# a.move()
# print(a.physical_entity)
# a.move()
# print(a.physical_entity)
# a.move()
# print(a.physical_entity)
# a.move()
# print(a.physical_entity)

