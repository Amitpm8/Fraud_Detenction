# Real-Time Financial Fraud Detection System

## Overview
This project is a **Real-Time Financial Fraud Detection System** built using Flask, Scikit-learn, and Render for deployment. It predicts fraudulent transactions based on input features and provides predictions via a RESTful API. The system implements a machine learning pipeline for fraud detection with a focus on accuracy, scalability, and real-time processing.

---

## Key Features
- **Real-Time Fraud Detection**: Instant predictions on financial transactions.
- **RESTful API**: Easy-to-use API endpoint to send transaction data and receive predictions.
- **Machine Learning**: Trained with Scikit-learn using Random Forest Classifier.
- **Deployed on Render**: Live and accessible API endpoint.
- **Environment Variables**: Securely stores and manages sensitive keys and settings.

---

## Achievements
1. Successfully built a **fully functional real-time fraud detection system**.
2. Deployed the project on Render with zero downtime.
3. Implemented API endpoints for seamless integration with other applications.
4. Demonstrated proficiency in:
   - Flask for building web services.
   - Machine learning model deployment.
   - Render as a hosting platform.
   - API testing using Postman.
5. Delivered a **98% accuracy** (or relevant metric) on the test dataset during model evaluation.
6. Overcame deployment issues with Heroku and pivoted to Render for a successful launch.

---

## Installation and Setup
### Clone the Repository
```bash
git clone https://github.com/your-username/Real-Time-Financial-Fraud-Detection.git
cd Real-Time-Financial-Fraud-Detection
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run Locally
```bash
flask run
```
- The application will be live at `http://127.0.0.1:5000/`.

---

## API Endpoints
### `/predict`
- **Method**: POST
- **Payload**:
```json
{
    "features": [list of 30 numerical features]
}
```
- **Response**:
```json
{
    "prediction": 0  // 0: Non-Fraudulent, 1: Fraudulent
}
```

### Example cURL Command:
```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "features": [-1.06453826, 0.17348925, -1.66156107, -0.08842163, -0.97871495, -1.05156262, 0.76252377, -0.4238806, 0.18760014, 0.81897078, -0.51890784, -0.08589134, 0.98021151, 0.07724801, -0.22729521, -0.14948917, -2.44552216, 0.14947692, 2.09104549, 0.53135806, 0.65641244, -0.29057759, -1.29878001, -0.84364067, -1.91034348, 0.59701544, -1.54833298, 0.10156733, 0.30912807, 1.7262552]
}' \
https://fraud-detection-app-665h.onrender.com/predict
```

---

## Deployment on Render
### Steps to Deploy:
1. **Create a New Web Service**:
   - Log in to Render.
   - Select "New" > "Web Service".
2. **Connect GitHub Repository**:
   - Link the GitHub repository to Render.
3. **Set Up Build Command**:
   - Use: `pip install -r requirements.txt`
4. **Set Start Command**:
   - Use: `gunicorn app:app`
5. **Set Environment Variables**:
   - Add any required environment variables.
6. **Deploy and Test**:
   - Test the app using the live URL.

---

## File Structure
```
.
├── app.py                 # Main Flask application
├── model.pkl              # Trained ML model
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
```

---

## Tools & Technologies Used
- **Python**: Programming language.
- **Flask**: Web framework.
- **Scikit-learn**: Machine learning library.
- **Gunicorn**: WSGI server for deployment.
- **Render**: Cloud platform for deployment.
- **Postman**: API testing tool.

---

## Future Enhancements
1. Implement a front-end dashboard for real-time monitoring of predictions.
2. Add support for multiple machine learning models.
3. Integrate a database (e.g., MongoDB, PostgreSQL) for transaction logs.
4. Enhance the API to handle batch predictions.

---

## Author
- **Amit**
- Connect on [LinkedIn](www.linkedin.com/in/amit-p-m)

---


## Acknowledgments
- Special thanks to the OpenAI community for guidance.
- Inspired by real-world challenges in financial fraud detection.

---

## Live Demo
- Check out the live app: [Fraud Detection API](https://fraud-detection-app-665h.onrender.com)
