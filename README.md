# python-coppeliasim-robot


# 🚀 Features
- Linear Motion: Move forward/backward with adjustable speed and duration.

- Precise Rotation: Rotate the robot by a specific angle (in degrees).

- Angle-based Rotation: Rotate to a target angle (in radians) using orientation feedback.

- Circular Motion: Perform counter-clockwise circular movement with adjustable radius and speed.

- Path Following: Executes a predefined sequence of movements (A → B → D → F → G → I → J → N → A → C → D).

# ⚙️ Requirements
- CoppeliaSim (V-REP)

- Python 3.x

- numpy

- coppeliasim_zmqremoteapi_client (Included in CoppeliaSim's remote API examples)


# 🔄 Movement Functions

- move_linear(duration, velocity)                    Moves straight for duration (seconds) at velocity.

- rotate_precise(degree)	                           Rotates the robot by degree (positive = counter-clockwise).

- rotate_to_angle(target_angle_rad)	                 Rotates to a specific angle (in radians).

- circular_movement_counterClockWise()	             Moves the robot in a circular path (counter-clockwise).

## 📽 Demo

![demo](demo.gif)



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


