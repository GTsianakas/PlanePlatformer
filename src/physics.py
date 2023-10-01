import math

from physics_vectors import Vector2D, PhysicsObject, convert_coords_to_vector, rotate_vector, normalize_vector

class Physics():

    def __init__(self, dt = 0.01):
        self.dt = dt

    def apply_gravity(self, pobject: PhysicsObject, g: float = 0.005) -> None:
        #pobject.speed.y = pobject.speed.y + g * self.dt
        #pobject.speed.y += pobject.speed.y * self.dt + (g * 0.5 * self.dt * self.dt)
        pobject.acceleration.y += g
        


    def apply_drag(self, pobject: PhysicsObject, coef: float = 0.002) -> None:
        #pobject.speed -= pobject.speed * pobject.speed * coef * self.dt
        (angle, magnitude) = convert_coords_to_vector(pobject.speed)

        drag_force = -coef * magnitude
        drag_acceleration = drag_force / pobject.mass

        magnitude_root = math.sqrt(magnitude) + 0.00001
        drag_accel_x = drag_acceleration * (pobject.speed.x / magnitude_root)
        drag_accel_y = drag_acceleration * (pobject.speed.y / magnitude_root)

        pobject.acceleration.x += drag_accel_x
        pobject.acceleration.y += drag_accel_y


        

    def apply_lift(self, pobject: PhysicsObject, angle:float, coef:float = 0.001, K:float = 0.5, S:float = 0.0) -> None:

        _, magnitude = convert_coords_to_vector(pobject.speed)
        
        #speed_angle = math.atan2(pobject.speed.y, pobject.speed.x)

        lift_force = 0.5 * coef * K * magnitude**2 * (math.sin(angle) + S)

        lift_accel_x = lift_force * math.cos(angle - math.pi/2) / pobject.mass
        lift_accel_y = lift_force * math.sin(angle - math.pi/2) / pobject.mass
        #print(f"{lift_accel_x}\t{lift_accel_y}")

        pobject.acceleration.x += lift_accel_x
        pobject.acceleration.y += lift_accel_y
        
        # lift_force: float = 0.5 * coef * K * magnitude**2 * (math.sin(angle) + 0.1) * self.dt
        # norm_vector: Vector2D = normalize_vector(pobject.speed,lift_force)
        # rotated_vector: Vector2D = rotate_vector(norm_vector,angle)

        # pobject.speed = norm_vector * lift_force

