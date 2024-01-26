from typing import List
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import JSON, ForeignKey

class Base(DeclarativeBase):
    pass

class Day(Base):
    __tablename__ = 'Day'
    day_id: Mapped[int] = mapped_column(primary_key=True)
    day_name: Mapped[str] = mapped_column(nullable=False,unique=True)
    day:Mapped['Dish'] = relationship(back_populates='day')
    def __repr__(self):
        return f"{self.day_id} {self.day_name}"

class MealType(Base):
    __tablename__ = 'MealType'
    meal_type_id: Mapped[int] = mapped_column(primary_key=True)
    meal_type_name: Mapped[str] = mapped_column(nullable=False,unique=True)
    mealtype:Mapped['Dish'] = relationship(back_populates='mealtype')

    def __repr__(self):
        return f"{self.meal_type_id} {self.meal_type_name}"

class Dish(Base):
    __tablename__ = 'Dish'
    dishes_id: Mapped[int] = mapped_column(primary_key=True)
    dishes: Mapped[JSON] = mapped_column(JSON)
    meal_type_id:Mapped[int] = mapped_column(ForeignKey('MealType.meal_type_id'),nullable=False)
    day_id:Mapped[int] = mapped_column(ForeignKey('Day.day_id'),nullable=False)
    day: Mapped['Day'] = relationship(back_populates='day')
    mealtype:Mapped['MealType'] = relationship(back_populates='mealtype')
    def __repr__(self):
        return f"{self.dishes_id}"
    

    
class User(Base):
    __tablename__ = 'User'
    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(unique=True)
    roll:Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(nullable=False,unique=True)
    comment:Mapped['Comment'] = relationship(back_populates='author')
    passcode:Mapped[int] 

class Comment(Base):
    __tablename__ = 'Comment'
    id:Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] 
    user_id:Mapped[int] = mapped_column(ForeignKey('User.id'),nullable=False)
    dishes_id:Mapped[int] = mapped_column(ForeignKey('Dish.dishes_id'),nullable=False)
    author:Mapped['User'] = relationship(back_populates='comment')
   
