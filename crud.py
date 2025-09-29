from sqlalchemy.orm import Session
import models, schemas

# Create a new patient
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# Get all patients
def get_patients(db: Session):
    return db.query(models.Patient).all()

# Create a new appointment
def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# Get all appointments
def get_appointments(db: Session):
    return db.query(models.Appointment).all()