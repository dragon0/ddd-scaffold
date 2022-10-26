from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    email = Column(String(50))


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
