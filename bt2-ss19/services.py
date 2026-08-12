from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schemas

def create_clinic(db: Session, clinic_in: schemas.ClinicCreate):
    try:
        # Giải nén dữ liệu bằng toán tử **
        new_clinic = models.Clinic(**clinic_in.model_dump())
        db.add(new_clinic)
        db.commit()
        db.refresh(new_clinic)
        return new_clinic
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Lỗi hệ thống khi tạo phòng khám")

def get_clinic_detail(db: Session, clinic_id: int):
    clinic = db.query(models.Clinic).filter(models.Clinic.id == clinic_id).first()
    if not clinic:
        raise HTTPException(status_code=404, detail="Không tìm thấy phòng khám")
    return clinic

def update_doctor(db: Session, doctor_id: int, doctor_in: schemas.DoctorUpdate):
    doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Không tìm thấy bác sĩ")
    
    try:
        # Lấy các trường thực tế được gửi lên
        update_data = doctor_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(doctor, key, value)
        
        db.commit()
        db.refresh(doctor)
        return doctor
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Lỗi hệ thống khi cập nhật bác sĩ")

def delete_license(db: Session, license_id: int):
    license_obj = db.query(models.License).filter(models.License.id == license_id).first()
    if not license_obj:
        raise HTTPException(status_code=404, detail="Không tìm thấy chứng chỉ")
    
    try:
        db.delete(license_obj)
        db.commit()
        return {"message": "Xóa chứng chỉ hành nghề thành công"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Lỗi hệ thống khi xóa chứng chỉ")
