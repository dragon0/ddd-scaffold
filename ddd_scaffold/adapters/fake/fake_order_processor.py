from typing import Optional

from ...domain.interfaces.order_processor import OrderProcessor

from ...domain.models.order import Order, OrderResult


class FakeOrderProcessor(OrderProcessor):
    def place_order(self, order: Order) -> Optional[OrderResult]:
        return OrderResult(order.id, order.customer_id)
