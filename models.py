from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from database import Base

class Patient(Base):
    __tablename__ = "Patients"
    patient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    date_of_birth = Column(Date)

class Appointment(Base):
    __tablename__ = "Appointments"
    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("Patients.patient_id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("Doctors.doctor_id"), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    reason = Column(String)