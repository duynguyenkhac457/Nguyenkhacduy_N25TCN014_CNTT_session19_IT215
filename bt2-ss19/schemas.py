from pydantic import BaseModel, ConfigDict
from typing import List, Optional

# --- CLINIC SCHEMAS ---
class ClinicCreate(BaseModel):
    clinic_name: str
    specialty: str

class DoctorBaseSchema(BaseModel):
    id: int
    doctor_code: str
    salary: float
    clinic_id: Optional[int] = None
    
    model_config = ConfigDict(from_attributes=True)

class ClinicDetailResponse(BaseModel):
    id: int
    clinic_name: str
    specialty: str
    doctors: List[DoctorBaseSchema] = [] # Lồng ghép danh sách Bác sĩ

    model_config = ConfigDict(from_attributes=True)


# --- DOCTOR SCHEMAS ---
class DoctorUpdate(BaseModel):
    doctor_code: Optional[str] = None
    salary: Optional[float] = None
    clinic_id: Optional[int] = None


# --- LICENSE SCHEMAS ---
class LicenseResponse(BaseModel):
    id: int
    license_number: str
    issue_by: str
    doctor_id: int

    model_config = ConfigDict(from_attributes=True)
