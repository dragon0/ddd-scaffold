import logging

from ...domain.interfaces.notifier import Notifier

from ...domain.models.customer import Customer
from ...domain.models.order import Order, OrderResult

logger = logging.getLogger(__name__)


class FakeNotifier(Notifier):
    def notify_successful_order(self, customer: Customer, order_result: OrderResult):
        logger.info(f'Successful order for {customer.email}')

    def notify_failed_order(self, customer: Customer, order: Order):
        logger.error(f'Failed order {order.id} for {customer.email}')
