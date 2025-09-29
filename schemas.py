from pydantic import BaseModel
from datetime import date, datetime

# Patient Schemas
class PatientCreate(BaseModel):
    name: str
    email: str
    phone: str
    date_of_birth: date

class PatientOut(PatientCreate):
    patient_id: int

    class Config:
        orm_mode = True

# Appointment Schemas
class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    reason: str

class AppointmentOut(AppointmentCreate):
    appointment_id: int

    class Config:
        orm_mode = True