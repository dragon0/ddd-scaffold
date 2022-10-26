import logging
from typing import Optional

from .interfaces.customer_lookup import CustomerLookup
from .interfaces.order_processor import OrderProcessor
from .interfaces.notifier import Notifier

from .models.order import Order, OrderResult

logger = logging.getLogger(__name__)


class DomainLogic:
    '''
    This class implements the high-level domain logic, delegating implementation
    details to the implmentations of the domain interfaces.

    The interfaces/ subdirectory declares abstract classes representing
    adapter-layer logic. These interfaces are implemented by classes in
    ../adapters.

    This class declares those interfaces as constructor dependencies so they can
    be injected.
    '''

    def __init__(self, customer_lookup: CustomerLookup, order_processor: OrderProcessor, notifier: Notifier):
        self.customer_lookup = customer_lookup
        self.order_processor = order_processor
        self.notifier = notifier

    def place_order(self, order: Order) -> Optional[OrderResult]:
        customer = self.customer_lookup.get_customer_by_id(order.customer_id)
        order_result = self.order_processor.place_order(order)
        if order_result:
            self.notifier.notify_successful_order(customer, order_result)
        else:
            logger.error(f'Failed order {order.id}')
            self.notifier.notify_failed_order(customer, order)
        return order_result
