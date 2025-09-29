from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, crud, schemas

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Patient endpoints
@app.post("/patients/", response_model=schemas.PatientOut)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.get("/patients/", response_model=list[schemas.PatientOut])
def read_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)

# Appointment endpoints
@app.post("/appointments/", response_model=schemas.AppointmentOut)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db, appointment)

@app.get("/appointments/", response_model=list[schemas.AppointmentOut])
def read_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)