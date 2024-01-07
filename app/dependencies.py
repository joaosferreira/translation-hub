from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABSE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()