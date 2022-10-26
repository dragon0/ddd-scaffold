import pytest
from sqlalchemy import inspect
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

from ddd_scaffold.adapters.fake.factory import DB_FILE, FakeFactory
from ddd_scaffold.adapters.fake.entities import Base, Customer
from ddd_scaffold.domain.models.customer import Customer as DomainCustomer


@pytest.fixture(scope="class")
def db_engine():
    return create_engine(DB_FILE,
                         # echo=True,
                         future=True)


@pytest.fixture(scope="class", autouse=True)
def populate_tables(db_engine):
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


@pytest.fixture(scope="class")
def fake_factory(db_engine):
    return FakeFactory(db_engine)


@pytest.fixture()
def domain_customer() -> DomainCustomer:
    return Customer(1234, "fake@example.com")
