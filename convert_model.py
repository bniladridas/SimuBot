import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2

# Load MobileNetV2 (pre-trained on ImageNet)
model = MobileNetV2(weights='imagenet')

# Save the model as .h5
model.save('models/object_detector.h5')
print("Model saved as object_detector.h5")