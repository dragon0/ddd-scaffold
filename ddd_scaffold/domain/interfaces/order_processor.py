from abc import ABC, abstractmethod
from typing import Optional

from ..models.order import Order, OrderResult


class OrderProcessor(ABC):
    @abstractmethod
    def place_order(self, order: Order) -> Optional[OrderResult]:
        raise NotImplementedError
