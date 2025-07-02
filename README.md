# python-coppeliasim-robot


# 🚀 Features
Linear Motion: Move forward/backward with adjustable speed and duration.

Precise Rotation: Rotate the robot by a specific angle (in degrees).

Angle-based Rotation: Rotate to a target angle (in radians) using orientation feedback.

Circular Motion: Perform counter-clockwise circular movement with adjustable radius and speed.

Path Following: Executes a predefined sequence of movements (A → B → D → F → G → I → J → N → A → C → D).

# ⚙️ Requirements
CoppeliaSim (V-REP)

Python 3.x

numpy

coppeliasim_zmqremoteapi_client (Included in CoppeliaSim's remote API examples)


# 🔄 Movement Functions
Function	Description
move_linear(duration, velocity)                    Moves straight for duration (seconds) at velocity.

rotate_precise(degree)	                           Rotates the robot by degree (positive = counter-clockwise).

rotate_to_angle(target_angle_rad)	                 Rotates to a specific angle (in radians).

circular_movement_counterClockWise()	             Moves the robot in a circular path (counter-clockwise).


# 📜 Predefined Path
The robot follows this sequence:

A → B: Linear movement.

B → D: 135° rotation + linear movement.

D → F: -135° rotation + linear movement.

F → G: 135° rotation + linear movement.

G → I: -75° rotation + linear movement.

I → J: Circular motion (counter-clockwise).

I → N: Linear movement (skipping J).

N → A: Rotate to 0° + linear movement.

A → C: 135° rotation + linear movement.

C → D: 45° rotation + linear movement.

# 🛑 Stopping the Simulation
The simulation stops automatically after completing the path (sim.stopSimulation()).

# 📌 Notes
Adjust max_velocity and wheel_distance in the script for different robot models.

Ensure the ZMQ Remote API is enabled in CoppeliaSim (Tools → ZMQ Remote API).



# 💡 Tip
For customization, modify the movement sequence in the try block.

# 🎯 Goal
This project demonstrates basic robot path planning in CoppeliaSim using Python.

 Happy simulating! 🤖 🚀


