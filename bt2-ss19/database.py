from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Thay đổi thông tin chuỗi kết nối MySQL cho phù hợp với máy của bạn
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/clinic_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
