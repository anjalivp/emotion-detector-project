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
