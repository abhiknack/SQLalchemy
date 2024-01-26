from main import session
from tables import Day,Dish


# delete all rows from the Day table
session.query(Dish).delete()

# commit the transaction to the database
session.commit()