from pydantic import BaseModel


class PatientCreate(BaseModel):
    patient_number: str
    name: str
    age: int | None = None
