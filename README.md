<img width="838" height="680" alt="image" src="https://github.com/user-attachments/assets/05256b40-5de4-4787-ae16-04d08410c834" /># 🌤️ NeuralSky: AI-Powered Weather Recognition System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![HTML/CSS](https://img.shields.io/badge/HTML5_&_CSS3-E34F26?style=for-the-badge&logo=html5&logoColor=white)

A lightweight, end-to-end weather classification web application built with a custom-trained **MobileNetV2** Convolutional Neural Network, a **FastAPI** backend, and a modern, responsive frontend.

---

## 🚀 The Project
NeuralSky takes a single image of the sky or scenery and instantly classifies the weather condition into one of four categories: **Cloudy, Rain, Shine, or Sunrise**. 

Instead of relying on massive, heavy models, this project utilizes transfer learning via **MobileNetV2** to achieve high accuracy while keeping the model file incredibly small (~14 MB), allowing for lightning-fast inference times on the FastAPI backend.

### ✨ Key Features
* **Real-Time Inference:** Upload an image and get predictions in milliseconds.
* **Lightweight Architecture:** Optimized MobileNetV2 model tailored for edge/web deployment.
* **Modern UI:** A clean, glass-morphism inspired frontend interface.

---

## 🧠 Model Architecture & Performance

The core vision engine was trained on Kaggle using a T4 GPU. By freezing the base layers of MobileNetV2 (pretrained on ImageNet) and attaching a custom 128-node dense head with dropout, the model quickly learned to map complex visual features to meteorological conditions.

* **Base Model:** MobileNetV2
* **Parameters:** ~2.4 Million Total (164K Trainable)
* **Validation Accuracy:** **91%** (Achieved in just 5 Epochs)
* **Real-World Confidence:** Consistently hits **99%+** confidence on test images.

### Training Metrics (Accuracy & Loss)
<img width="1665" height="784" alt="Screenshot 2026-05-31 203545" src="https://github.com/user-attachments/assets/43d9093c-1f50-4078-935b-209ddbf843e3" />
<img width="601" height="326" alt="Screenshot 2026-05-31 203601" src="https://github.com/user-attachments/assets/c8e80b8b-1fb0-418a-a2d9-8e920bac6679" />
<img width="838" height="680" alt="Screenshot 2026-05-31 204351" src="https://github.com/user-attachments/assets/422ec726-13bb-4438-9119-bc7026db4efa" />

---

## 📸 Application Gallery

### 1. The Interface
<img width="630" height="758" alt="image" src="https://github.com/user-attachments/assets/a82363fb-ff97-4239-adc8-79ad68ba582a" />


### 2. High-Confidence Predictions
<img width="607" height="681" alt="image" src="https://github.com/user-attachments/assets/7e1d2dca-d527-4b27-84f6-ba34ec07936a" />


---

## 🛠️ Tech Stack
* **Deep Learning:** TensorFlow, Keras, MobileNetV2
* **Backend API:** FastAPI, Uvicorn, Python, Pillow, NumPy
* **Frontend:** HTML5, CSS3 (Modern Flexbox/Grid), Vanilla JavaScript

---

## 💻 How to Run Locally

If you want to test the model yourself, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/ShwetaPatil2005/NeuralSky-AI-Powered-Weather-Recognition-System.git](https://github.com/ShwetaPatil2005/NeuralSky-AI-Powered-Weather-Recognition-System.git)
cd NeuralSky-AI-Powered-Weather-Recognition-System

**2. Install Dependencies**

Bash
pip install fastapi uvicorn python-multipart tensorflow pillow numpy
3. Start the FastAPI Server

Bash
uvicorn main:app --reload
4. Launch the Frontend
Simply double-click the index.html file to open it in your browser and start classifying images!
