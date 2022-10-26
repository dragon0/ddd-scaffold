import logging
from typing import Optional

from pydantic import ValidationError

from ...adapters.fake.factory import FakeFactory

from ...domain.models.customer import Customer

from . import dtos

logger = logging.getLogger(__name__)


class ExternalApiAdapter:
    def __init__(self, db_engine=None):
        self.db = FakeFactory(db_engine)

    def get_customer(self, customer_dto: dtos.Customer) -> Customer:
        return Customer(customer_dto.id, customer_dto.email)

    def process_request(self, contents: str) -> Optional[Customer]:
        '''
        contents is a JSON string payload
        '''
        try:
            customer_dto = dtos.Customer.parse_raw(contents)
        except ValidationError as e:
            logger.error(e)
            return None
        else:
            return self.get_customer(customer_dto)
