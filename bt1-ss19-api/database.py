from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/logicstics_db" 

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal() # Mở một phiên làm việc mới
    try:
        yield db        # Tạm dừng hàm, giao 'db' cho API sử dụng
    finally:
        db.close()   

class Base(DeclarativeBase):
    pass
