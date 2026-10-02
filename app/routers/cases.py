from fastapi import APIRouter, HTTPException, status

from app.config.config import CASES_DB_COLLECTION, DOCTORS_DB_COLLECTION, PATIENTS_DB_COLLECTION
from app.config.db_init import mongo_db
from app.schema.case import CaseCreate
from app.middleware.authentication import get_current_user

router = APIRouter(prefix="", tags=["cases"])


@router.post("/new_case")
def create_case(payload: CaseCreate):
    cases = mongo_db[CASES_DB_COLLECTION]
    patients = mongo_db[PATIENTS_DB_COLLECTION]
    doctors = mongo_db[DOCTORS_DB_COLLECTION]

    if not patients.find_one({"_id": payload.patient_id}):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    if not doctors.find_one({"_id": payload.patient_id}):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")

    case_record = {
        "patient_id": payload.patient_id,
        "doctor_id": payload.patient_id,
        "title": payload.title,
        "notes": payload.notes,
        "status": payload.status,
    }
    result = cases.insert_one(case_record)
    return {"id": str(result.inserted_id), "message": "Case created successfully"}


@router.get("/get_cases")
def get_cases_for_doctor(current_user: dict = {}) -> list:
    cases = mongo_db[CASES_DB_COLLECTION]
    return list(cases.find({"doctor_id": current_user.get("doctor_id", "")}))


@router.get("/cases/{case_id}")
def get_case_by_id(case_id: str):
    cases = mongo_db[CASES_DB_COLLECTION]
    case = cases.find_one({"_id": case_id})
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
    return case


@router.get("/cases/patient/{patient_id}")
def get_cases_for_patient(patient_id: str):
    cases = mongo_db[CASES_DB_COLLECTION]
    return list(cases.find({"patient_id": patient_id}))
