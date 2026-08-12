from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Base
from database import engine, get_db
from schemas import WarehouseDetailResponse, WarehouseCreate
import service

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/warehouses", response_model=WarehouseDetailResponse, status_code=201)
def create_warehouse_api(warehouse :WarehouseCreate, db : Session = Depends(get_db) ):
    return service.create_warehouse(warehouse=warehouse, db=db)

@app.get("/warehouses/{warehouse_id}")
def get_warehouse_api(warehouse_id : int, db : Session = Depends(get_db)):
    return service.get_warehouse(db=db,warehouse_id=warehouse_id)
