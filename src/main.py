import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.insert(0, '/Users/niladridas/Documents/Sim')

import suppress_warnings  # This will apply the warning filter

from .simulation import setup_simulation, run_simulation
from .ai import extract_features
import cv2

if __name__ == "__main__":
    # Run simulation
    physicsClient, planeId, robotId = setup_simulation()
    run_simulation(physicsClient)

    # Example: Extract features from an image
    image_path = "img/hello.jpg"  # Replace with your image path
    features = extract_features(image_path)
    print("Extracted features:", features)