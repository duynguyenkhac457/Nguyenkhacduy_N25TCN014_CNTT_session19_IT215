from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import schemas, services

# Tự động tạo bảng nếu chưa có (phục vụ test)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hệ thống Quản lý Phòng Khám")

@app.post("/clinics", response_model=schemas.ClinicDetailResponse, status_code=status.HTTP_201_CREATED)
def create_clinic_endpoint(clinic_in: schemas.ClinicCreate, db: Session = Depends(get_db)):
    return services.create_clinic(db, clinic_in)

@app.get("/clinics/{clinic_id}", response_model=schemas.ClinicDetailResponse, status_code=status.HTTP_200_OK)
def get_clinic_endpoint(clinic_id: int, db: Session = Depends(get_db)):
    return services.get_clinic_detail(db, clinic_id)

@app.patch("/doctors/{doctor_id}", response_model=schemas.DoctorBaseSchema, status_code=status.HTTP_200_OK)
def update_doctor_endpoint(doctor_id: int, doctor_in: schemas.DoctorUpdate, db: Session = Depends(get_db)):
    return services.update_doctor(db, doctor_id, doctor_in)

@app.delete("/licenses/{license_id}", status_code=status.HTTP_200_OK)
def delete_license_endpoint(license_id: int, db: Session = Depends(get_db)):
    return services.delete_license(db, license_id)
