from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer_id: int


@dataclass
class OrderResult:
    id: int
    customer_id: int
