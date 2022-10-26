import pytest

from ddd_scaffold.domain.domain_logic import DomainLogic

from ddd_scaffold.domain.models.order import Order


@pytest.fixture()
def domain_logic(fake_factory):
    return DomainLogic(fake_factory.create_customer_lookup(),
                       fake_factory.create_order_processor(),
                       fake_factory.create_notifier())


def test_domain_logic(domain_logic):
    order = Order(1234, 5678)
    result = domain_logic.place_order(order)
    assert result
