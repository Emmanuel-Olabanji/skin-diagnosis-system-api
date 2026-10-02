from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        if not ObjectId.is_valid(str(value)):
            raise ValueError("Invalid ObjectId")
        return str(value)


class DoctorModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    name: str
    email: str
    specialty: str = "General"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PatientModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    patient_number: str
    name: str
    age: Optional[int] = None
    diagnosis_history: list[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CaseModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    patient_id: str
    doctor_id: str
    title: str
    notes: str = ""
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ApiKeyModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    doctor_id: str
    api_key: str
    expires_at: Optional[datetime] = None
    is_active: bool = True
