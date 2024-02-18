from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config import settings
import enum

Base = declarative_base()

class AlertStatus(enum.Enum):
    CREATED = "created"
    DELETED = "deleted"
    TRIGGERED = "triggered"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    alerts = relationship("Alert", back_populates="owner")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price_target = Column(Float)
    currency = Column(String, default="BTC")
    status = Column(Enum(AlertStatus), default=AlertStatus.CREATED)
    owner = relationship("User", back_populates="alerts")

# db connection
engine = create_engine(settings.database_url)
Base.metadata.create_all(bind=engine)
