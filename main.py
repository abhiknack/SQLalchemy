
from sqlalchemy.orm import sessionmaker
from connect import engine
# engine = create_engine("postgresql://mess_bgz8_user:QghoHtgB4IJpPkaqYu3tPC9tTib7a35o@dpg-cmejskacn0vc73bpcrkg-a/mess_bgz8")

Session = sessionmaker(bind=engine)
session = Session()

