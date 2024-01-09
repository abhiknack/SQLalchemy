from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.orm import sessionmaker,DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = "Mess"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    gender:Mapped[str] 
    age:Mapped[int]

    def __repre__(self):
        return f"{self.id} {self.name} {self.gender} {self.age} "

engine = create_engine("postgresql://mess_bgz8_user:QghoHtgB4IJpPkaqYu3tPC9tTib7a35o@dpg-cmejskacn0vc73bpcrkg-a/mess_bgz8")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(1234,"Abhijeet Kujur","M",29)
session.add(p1)
session.commit()