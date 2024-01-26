from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:abhi@localhost/Mess",echo=True)
