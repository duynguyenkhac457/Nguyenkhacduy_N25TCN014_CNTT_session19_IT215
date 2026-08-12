from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from database import Base
from models import Warehouse, Package, Waybill
import schemas

def create_warehouse(db: Session, warehouse : schemas.WarehouseCreate):
    new_warehouse = Warehouse(**warehouse.model_dump())
    try: 
        db.add(new_warehouse)
        db.commit()
        db.refresh(new_warehouse)
        return new_warehouse
    except SQLAlchemyError : 
        db.rollback()
        raise HTTPException(status_code=500, detail="lỗi khi kết nối với database")
 
def get_warehouse(db: Session, warehouse_id :int ):
    warehouse = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404,detail="không tìm thấy nhà kho")
    return warehouse


