import cv2
import numpy as np

def preprocess_image(image):
    """
    Preprocess an image for the model.
    """
    image = cv2.resize(image, (224, 224))  # Resize to match model input size
    image = image / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image