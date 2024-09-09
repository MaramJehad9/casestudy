import os
import docker
import joblib

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# Connect to Docker daemon
client = docker.from_env()

# Pull the Docker image (in this case, Python 3.10)
image = client.images.pull('python:3.10')

# Extract features from the Docker image
def extract_features(image):
    # Example of feature extraction (e.g., layers, base image, etc.)
    layers = len(image.history())
    base_image = image.attrs['Config']['Image']
    # Add more features based on vulnerabilities in dependencies or base image
    return [layers, base_image]

# Get features from the Docker image
features = extract_features(image)

# Use the Random Forest model to classify the image
prediction = model.predict([features])

# Output the classification result
if prediction == 'Secure':
    print('Secure')
else:
    # Notify the team if the image is insecure
    print("Image flagged as insecure. Please update the dependencies or use a secure version.")

