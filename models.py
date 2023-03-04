from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

class Post(Base):
    __tablename__='posts'
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    title = Column(String)
    content = Column(String,nullable=False)
    published = Column(Boolean,default=True,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")
