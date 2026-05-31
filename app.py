from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

# Allow our simple HTML frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Load the model we just trained
print("Loading Model...")
model = tf.keras.models.load_model("weather_model.h5")
classes = ['Cloudy', 'Rain', 'Shine', 'Sunrise']
print("Model Loaded Successfully!")

# 2. Define the prediction endpoint
@app.post("/predict")
async def predict_weather(file: UploadFile = File(...)):
    # Read the uploaded image
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    
    # Resize and scale exactly like we did in Kaggle
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0) # Add batch dimension
    
    # Make the prediction
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions)
    confidence = float(np.max(predictions)) * 100
    
    # Return the result to the frontend
    return {
        "prediction": classes[class_idx],
        "confidence": f"{confidence:.2f}%"
    }