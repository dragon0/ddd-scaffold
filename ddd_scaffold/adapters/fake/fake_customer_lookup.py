from ...domain.interfaces.customer_lookup import CustomerLookup
from ...domain.models.customer import Customer


class FakeCustomerLookup(CustomerLookup):
    def __init__(self):
        super().__init__()

    def get_customer_by_id(self, customer_id: int) -> Customer:
        return Customer(customer_id, 'fake@example.com')
