# Project Documentation

## 1. Project Overview

### Project Description

The Skin Diagnosis API integrates an AI-powered machine learning model for skin condition analysis. The default ML-API used in this project is linked to the Skin Diagnosis ML service; however, the system is flexible and can be configured to use another ML API if needed.

This project is a Python-based application designed to facilitate the diagnosis and management of skin conditions using AI-powered image analysis. It provides an API for handling patient cases, doctor management, and secure authentication. Built with FastAPI and MongoDB, it ensures scalability, security, and efficient data storage.

## 2. Installation & Setup

### Prerequisites

- Python 3.x
- pip
- MongoDB database access

### Installation Steps

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <project-folder>
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Copy `.env.example` to `.env` and update values.

## 3. Configuration

The application uses environment variables for configuration. Key settings include:

```ini
MONGO_USERNAME=your_username
MONGO_PASSWORD=your_password
MONGO_CLUSTER=cluster.mongodb.net
DB_NAME=Skin_Cancer_Diagnosis
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
PORT=8000
```

## 4. API Endpoints

### Case Management Endpoints

- `POST /new_case`
- `GET /cases/{case_id}`
- `GET /get_cases`
- `GET /cases/patient/{patient_id}`

### User Management Endpoints

- `POST /register-doctor`
- `POST /login`
- `POST /register-patient`
- `GET /doctors`
- `GET /patients/{patient_number}`

## 5. Usage Instructions

Run the application:

```sh
python -m uvicorn app.main:app --reload
```

Access the API via the configured endpoints.

## 6. Running Tests

```sh
pytest
```

## 7. Project Structure

```text
app/
  config/
  db/
  external_services/
  middleware/
  models/
  routers/
  schema/
  utils/
  main.py
``` 

## 8. License

This project is licensed under the MIT License.
