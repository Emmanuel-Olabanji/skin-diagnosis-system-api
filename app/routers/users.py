from fastapi import APIRouter, HTTPException, status

from app.config.config import DOCTORS_DB_COLLECTION, PATIENTS_DB_COLLECTION
from app.config.db_init import mongo_db
from app.schema.authentication import DoctorCreate, DoctorLogin, PatientCreate
from app.utils.authentication import hash_password, verify_password
from app.middleware.authentication import create_access_token

router = APIRouter(prefix="", tags=["users"])


@router.post("/register-doctor")
def register_doctor(payload: DoctorCreate):
    doctors = mongo_db[DOCTORS_DB_COLLECTION]
    if doctors.find_one({"email": str(payload.email)}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Doctor already exists")

    doctor_record = {
        "name": payload.name,
        "email": str(payload.email),
        "password": hash_password(payload.password),
        "specialty": payload.specialty,
    }
    result = doctors.insert_one(doctor_record)
    return {"id": str(result.inserted_id), "message": "Doctor registered successfully"}


@router.post("/login")
def doctor_login(payload: DoctorLogin):
    doctors = mongo_db[DOCTORS_DB_COLLECTION]
    doctor = doctors.find_one({"email": str(payload.email)})
    if not doctor or not verify_password(payload.password, doctor.get("password", "")):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token({"doctor_id": str(doctor.get("_id")), "email": doctor["email"]})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register-patient")
def register_patient(payload: PatientCreate):
    patients = mongo_db[PATIENTS_DB_COLLECTION]
    if patients.find_one({"patient_number": payload.patient_number}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Patient already exists")

    patient_record = {
        "patient_number": payload.patient_number,
        "name": payload.name,
        "age": payload.age,
        "diagnosis_history": [],
    }
    result = patients.insert_one(patient_record)
    return {"id": str(result.inserted_id), "message": "Patient registered successfully"}


@router.get("/doctors")
def get_doctors():
    doctors = mongo_db[DOCTORS_DB_COLLECTION]
    return list(doctors.find({}, {"password": 0}))


@router.get("/patients/{patient_number}")
def get_patient(patient_number: str):
    patients = mongo_db[PATIENTS_DB_COLLECTION]
    patient = patients.find_one({"patient_number": patient_number})
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return patient
