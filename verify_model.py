from tensorflow.keras.models import load_model

# Load the saved model
loaded_model = load_model('models/object_detector.h5')

# Print model summary
loaded_model.summary()