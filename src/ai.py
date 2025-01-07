from tensorflow.keras.models import load_model
import numpy as np
import cv2

# Load the model
model = load_model('../models/object_detector.h5')

# Preprocess an image
def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # Resize to match model input size
    image = image / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Extract features from an image
def extract_features(image_path):
    image = cv2.imread(image_path)  # Load the image
    if image is None:
        raise FileNotFoundError(f"Image file '{image_path}' not found.")
    processed_image = preprocess_image(image)
    features = model.predict(processed_image)
    return features

# Example usage
if __name__ == "__main__":
    image_path = "../img/hello.jpg"  # Ensure this path is correct
    features = extract_features(image_path)
    print("Extracted features:", features)