import os

from sqlalchemy import inspect
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

from ddd_scaffold.adapters.fake.factory import DB_FILE
from ddd_scaffold.adapters.fake.entities import Base, Customer, Order

def populate_tables():

    db_basename = os.path.basename(DB_FILE)
    if os.path.exists(db_basename):
        os.remove(db_basename)

    db_engine = create_engine(DB_FILE, echo=True, future=True)

    if not inspect(db_engine).has_table(Customer.__name__):
        Base.metadata.create_all(db_engine)

    c1 = Customer(email="test1@example.com")
    c2 = Customer(email="test2@example.com")
    c3 = Customer(email="test3@example.com")

    customers = [c1, c2, c3]

    orders = []

    with Session(db_engine) as session:
        for x in customers + orders:
            session.add(x)
        session.commit()

if __name__ == '__main__':
    populate_tables()
