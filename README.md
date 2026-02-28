# Emotion Detector – Final Project 

This project is part of the "AI-Based Web Application Development" course.  
The goal is to build an Emotion Detection web application using the Watson NLP (Embedded AI) library and deploy it using Flask.

---

## 📌 Project Tasks Completed

### **Task 1 — Clone the Project Repository**
- Repository created and project folder structure prepared.

### **Task 2 — Emotion Detection Application**
- Implemented `emotion_detector()` in `EmotionDetection/emotion_detection.py`
- Sends text to Watson NLP "Emotion Predict" model  
- Returns raw response or `None` values for invalid input

### **Task 3 — Output Formatting**
- The result is converted from JSON text → Python dictionary
- Only key values extracted:  
  - emotion  
  - anger  
  - disgust  
  - fear  
  - joy  
  - sadness  

### **Task 4 — Packaged as EmotionDetection Package**
Folder structure:# emotion-detector-project

### **Task 5 — Unit Testing**
- Added `test_emotion_detection.py`
- Includes 3 unit tests:
  - Positive emotion
  - Negative emotion
  - Neutral emotion

### **Task 6 — Flask Web Deployment**
- Implemented Flask app in `server.py`
- Endpoint `/emotionDetector` connects frontend to backend
- Successfully deployed on **http://localhost:5000**

### **Task 7 — Error Handling**
- Handles:
  - Blank input  
  - Invalid text (gibberish)  
  - API failures  
- Returns `Invalid input! Try again.`

### **Task 8 — Static Code Analysis**
- Pylint executed on server.py
- Score improved based on suggestions

---

## 💻 How to Run This Project

### **1. Install dependencies**
```bash
python3.11 -m pip install requests flask pylint
