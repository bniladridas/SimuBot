import pybullet as p
import os

def setup_simulation():
    # Connect to the physics server
    physicsClient = p.connect(p.GUI)  # Use p.DIRECT for non-graphical version
    p.setGravity(0, 0, -10)

    # Load a plane and a robot (e.g., a simple cube)
    plane_urdf_path = "assets/plane.urdf"
    robot_urdf_path = "assets/r2d2.urdf"
    
    if not os.path.exists(plane_urdf_path):
        raise FileNotFoundError(f"URDF file not found: {plane_urdf_path}")
    if not os.path.exists(robot_urdf_path):
        raise FileNotFoundError(f"URDF file not found: {robot_urdf_path}")
    
    try:
        planeId = p.loadURDF(plane_urdf_path)
    except p.error as e:
        print(f"Error loading URDF file: {e}")
        raise

    cubeStartPos = [0, 0, 1]
    cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
    
    try:
        robotId = p.loadURDF(robot_urdf_path, cubeStartPos, cubeStartOrientation)
    except p.error as e:
        print(f"Error loading URDF file: {e}")
        raise

    return physicsClient, planeId, robotId

def run_simulation(physicsClient):
    # Simulation loop
    for _ in range(1000):
        p.stepSimulation()
    p.disconnect()