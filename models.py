from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


from database import Base


class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True)
    link = Column(String)
