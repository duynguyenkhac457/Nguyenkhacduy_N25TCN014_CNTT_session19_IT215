from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Clinic(Base):
    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True, index=True)
    clinic_name = Column(String(255), nullable=False)
    specialty = Column(String(255), nullable=False)

    # Relationship 1-N với Doctor
    doctors = relationship("Doctor", back_populates="clinic")


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    doctor_code = Column(String(50), unique=True, nullable=False)
    salary = Column(Float, nullable=False)
    clinic_id = Column(Integer, ForeignKey("clinics.id"))

    # Relationship N-1 với Clinic
    clinic = relationship("Clinic", back_populates="doctors")
    
    # Relationship 1-1 với License (Bắt buộc uselist=False)
    license = relationship("License", back_populates="doctor", uselist=False)


class License(Base):
    __tablename__ = "licenses"

    id = Column(Integer, primary_key=True, index=True)
    license_number = Column(String(100), unique=True, nullable=False)
    issue_by = Column(String(255), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), unique=True, nullable=False)

    # Relationship 1-1 với Doctor
    doctor = relationship("Doctor", back_populates="license")
