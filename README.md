# ML Project

![Python](https://img.shields.io/badge/Python-3.8-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.4-orange)
![PyBullet](https://img.shields.io/badge/PyBullet-3.0-green)

This project uses machine learning for object detection and simulates a robot using PyBullet.

## Installation

Follow these steps to set up the project:

```bash
# Clone the repository
git clone https://github.com/bniladridas/SimuBot.git

# Navigate to the project directory
cd SimuBot

# Install dependencies
pip install -r requirements.txt
```

## Usage

Instructions on how to use the project:

```bash
# Run the simulation
python src/main.py
```

## Project Structure

- `src/`: Contains the source code for the simulation and AI components.
  - `simulation.py`: Sets up and runs the simulation.
  - `ai.py`: Contains the AI model and feature extraction code.
  - `utils.py`: Utility functions for image preprocessing.
  - `main.py`: Main entry point for running the simulation and AI tasks.
- `assets/`: Contains URDF files for the robot and plane.
- `models/`: Contains the pre-trained AI models.
- `img/`: Contains sample images for testing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ML Workflow

### Control Flow Diagram

This diagram illustrates the control flow of the ML component for object detection:

```mermaid
flowchart TD
    A[Start] --> B[Load Image]
    B --> C{Preprocess Image?}
    C -->|Yes| D[Resize Image]
    D --> E[Normalize Image]
    E --> F[Add Batch Dimension]
    F --> G[Feature Extraction]
    G --> H[Model Prediction]
    H --> I[Output Features]
    I --> J[End]
    C -->|No| G
```

### Model and Algorithm Diagram

Here's an overview of the model architecture and algorithms used:

```mermaid
classDiagram
    class Model {
        +MobileNetV2 model
        +load_model(model_path: str)
        +predict(input_data: Tensor)
    }

    class ImageProcessing {
        +preprocess_image(image: np.array)
        +extract_features(image_path: str)
    }

    class Simulation {
        +setup_simulation()
        +run_simulation(physicsClient)
    }

    Model -- ImageProcessing : Uses
    ImageProcessing -- Simulation : Provides features for
```

### Explanation

- **Model**: The project leverages a pre-trained MobileNetV2 for object detection, loaded using TensorFlow's Keras API.
- **Image Processing**: Images are preprocessed (resized, normalized) before being fed into the model for feature extraction.
- **Simulation**: The extracted features could guide actions within the PyBullet simulation environment, simulating real-world scenarios where object detection informs robot behavior.