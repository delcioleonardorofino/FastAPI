from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    completed = Column(Boolean, server_default="FALSE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True, nullable=False, 
                        nullable=text('now()')))

