from sqlalchemy.engine import create_engine
from sqlalchemy.inspection import inspect

from ...domain.interfaces.customer_lookup import CustomerLookup
from ...domain.interfaces.order_processor import OrderProcessor
from ...domain.interfaces.notifier import Notifier

from .fake_customer_lookup import FakeCustomerLookup
from .fake_order_processor import FakeOrderProcessor
from .fake_notifier import FakeNotifier

from .entities import Base, Order

DB_FILE = 'sqlite+pysqlite:///database.db'


class FakeFactory:
    def __init__(self, engine=None):
        if engine:
            self.engine = engine
        else:
            self.engine = create_engine(DB_FILE, echo=True)

        if not inspect(self.engine).has_table(Order.__name__):
            Base.metadata.create_all(self.engine)

    def create_customer_lookup(self) -> CustomerLookup:
        return FakeCustomerLookup()

    def create_order_processor(self) -> OrderProcessor:
        return FakeOrderProcessor()

    def create_notifier(self) -> Notifier:
        return FakeNotifier()
