from pydantic import BaseModel, EmailStr


class DoctorCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    specialty: str = "General"


class DoctorLogin(BaseModel):
    email: EmailStr
    password: str


class PatientCreate(BaseModel):
    patient_number: str
    name: str
    age: int | None = None


class CaseCreate(BaseModel):
    patient_id: str
    title: str
    notes: str = ""
    status: str = "pending"
