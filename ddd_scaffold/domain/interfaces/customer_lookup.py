from abc import ABC, abstractmethod

from ..models.customer import Customer


class CustomerLookup(ABC):
    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        raise NotImplementedError
