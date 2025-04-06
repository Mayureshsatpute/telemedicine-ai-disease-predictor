# 🏥 Telemedicine Connect - Web Application

A comprehensive AI-powered telemedicine platform tailored for underserved communities. This web app enables users to book video consultations, access local health resources, and get AI-based symptom diagnoses — all with a simple and user-friendly interface.

---

## 🌐 Live Features

### ✅ User Authentication
- 🔐 **Register/Login** functionality
- Backend connection to Flask API for secure authentication
- Session-less access to dashboard upon successful login

### 📋 AI Symptom Diagnosis
- Users input symptoms
- Sent to backend Flask AI model
- Returns real-time diagnosis result (`/predict` endpoint)

### 📅 Teleconsultation Booking System
- Input: Name, date, specialty
- Generates appointment history using `localStorage`
- Opens video call in new tab via [Jitsi Meet](https://meet.jit.si/)
- Appointment history with rejoin links

### 📍 Local Health Resources
- Select city and view nearby hospitals, pharmacies, wellness centers
- Pre-filled hospital lists for:
  - Jalgaon
  - Nashik
  - Pune
  - Aurangabad
  - Dhule

### 📊 Dashboard Sections
- AI Diagnosis section
- Medication tracker (static placeholder)
- Appointment history
- Local health resources directory
- Responsive navigation with toggle between login and signup

---

## 🛠️ Tech Stack

### Frontend:
- **HTML, CSS, JavaScript**
- Responsive design and dynamic DOM manipulation
- LocalStorage for storing appointments

### Backend:
- **Flask (Python)**
  - `/login`: User authentication
  - `/register`: User signup
  - `/predict`: AI-based diagnosis using symptom input

### AI Integration:
- Connected to ML model hosted via Flask for symptom-to-disease prediction
- Includes heart disease predictor and common illness predictor

---

## 📁 Project Structure

```
├── index.html                 # Main frontend file
├── static/
│   └── style.css             # Custom styles (if separated)
├── backend/
│   └── app.py                # Flask backend routes
│   └── models/
│       └── heart_disease_model.pkl
│       └── illness_model.pkl
├── templates/                # Flask templates if applicable
│   └── dashboard.html
```

---

## 🚀 How to Run the Project

### 🔧 Backend (Flask):
1. Navigate to the `backend/` directory.
2. Install required packages:
   ```bash
   pip install flask scikit-learn
   ```
3. Start the Flask server:
   ```bash
   python app.py
   ```
   Flask will run at `http://localhost:5000`.

### 🌐 Frontend:
1. Open `index.html` in any modern browser.
2. Ensure the backend is running locally for authentication and diagnosis.
3. Interact with features:
   - Register/Login
   - Book appointments
   - Diagnose symptoms
   - View health resource directory

---

## 📌 Future Improvements

- ✅ Replace localStorage with database-backed history (e.g., MySQL)
- ✅ Add real-time chat with doctor
- ✅ Integrate Marathi/other regional languages toggle
- ✅ Add medication reminder system
- ✅ User profile with past consultation analytics

---
## 👨‍💻 Developed By

**Mayuresh Satpute**  
**Aakanksha Naiknaware**  
<<<<<<< HEAD
`© 2025 Telemedicine Connect. All rights reserved.`
=======
`© 2025 Telemedicine Connect. All rights reserved.`
>>>>>>> f09892294afd512fd477525b582b418e45a2b3f6
