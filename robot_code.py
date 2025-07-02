import time
import math
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

sim.startSimulation()
time.sleep(1)

left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')
robot = sim.getObject('/PioneerP3DX')

floor_handle = sim.getObject('/Floor')
sim.scaleObject(floor_handle, 15.0, 20.0, 1.0)

# تنظیمات موتور
max_velocity = 2.0
wheel_distance = 0.2
sim.setJointMaxForce(left_motor, 100)
sim.setJointMaxForce(right_motor, 100)

def move_linear(duration, velocity):
    sim.setJointTargetVelocity(left_motor, velocity)
    sim.setJointTargetVelocity(right_motor, velocity)
    time.sleep(duration)
    sim.setJointTargetVelocity(left_motor, 0)
    sim.setJointTargetVelocity(right_motor, 0)

def rotate_precise(degree):
    rad = math.radians(degree)
    rotation_time = abs(rad * wheel_distance / 2) / max_velocity
    direction = 1 if degree > 0 else -1
    sim.setJointTargetVelocity(left_motor, direction * max_velocity)
    sim.setJointTargetVelocity(right_motor, -direction * max_velocity)
    time.sleep(rotation_time)
    sim.setJointTargetVelocity(left_motor, 0)
    sim.setJointTargetVelocity(right_motor, 0)

def rotate_to_angle(target_angle_rad):
    orientation = sim.getObjectOrientation(robot, -1)[2]
    error = (target_angle_rad - orientation + math.pi) % (2 * math.pi) - math.pi
    direction = 1 if error > 0 else -1
    rotation_time = abs(error) / max_velocity
    sim.setJointTargetVelocity(left_motor, -direction * max_velocity)
    sim.setJointTargetVelocity(right_motor, direction * max_velocity)
    time.sleep(rotation_time)
    sim.setJointTargetVelocity(left_motor, 0)
    sim.setJointTargetVelocity(right_motor, 0)

def circular_movement_counterClockWise(radius=1.0, linear_speed=0.2, duration=10, robot_name='/PioneerP3DX'):
    wheel_base = 0.33
    v_left = linear_speed * (radius + wheel_base / 2) / radius
    v_right = linear_speed * (radius - wheel_base / 2) / radius
    sim.setJointTargetVelocity(left_motor, v_left)
    sim.setJointTargetVelocity(right_motor, v_right)
    time.sleep(duration)
    sim.setJointTargetVelocity(left_motor, 0)
    sim.setJointTargetVelocity(right_motor, 0)

try:
    print("Moving A → B")
    move_linear(duration=7, velocity=max_velocity)

    print("Moving B → D")
    rotate_precise(135)
    time.sleep(0.75)
    move_linear(duration=12, velocity=max_velocity)

    print("Moving D → F")
    rotate_precise(-135)
    time.sleep(0.75)
    move_linear(duration=7, velocity=max_velocity)

    print("Moving F → G")
    rotate_precise(135)
    move_linear(duration=3, velocity=max_velocity)

    print("Moving G → I")
    rotate_precise(-75)
    move_linear(duration=8, velocity=max_velocity)

    print("Moving I → J")
    circular_movement_counterClockWise(radius=1, linear_speed=4, duration=33.5)
    time.sleep(0.5)

    print("Moving I → N")
    move_linear(duration=8, velocity=max_velocity)

    print("Moving N → A")
    rotate_to_angle(0.0)
    move_linear(duration=20, velocity=max_velocity)

    print("Moving A → C")
    rotate_precise(135)
    move_linear(duration=7, velocity=max_velocity)

    print("Moving C → D")
    rotate_precise(45)
    move_linear(duration=7, velocity=max_velocity)

finally:
    sim.stopSimulation()
    print("Simulation stopped.")