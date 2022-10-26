from abc import ABC, abstractmethod

from ..models.customer import Customer
from ..models.order import Order, OrderResult


class Notifier(ABC):
    @abstractmethod
    def notify_successful_order(self, customer: Customer, order_result: OrderResult):
        raise NotImplementedError

    @abstractmethod
    def notify_failed_order(self, customer: Customer, order: Order):
        raise NotImplementedError
