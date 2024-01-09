from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "Mess"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"{self.id} {self.name} {self.gender} {self.age}"

engine = create_engine("postgresql://mess_bgz8_user:QghoHtgB4IJpPkaqYu3tPC9tTib7a35o@dpg-cmejskacn0vc73bpcrkg-a/mess_bgz8")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(id=1234, name="Abhijeet Kujur", gender="M", age=29)
session.add(p1)
session.commit()
