from pydantic import BaseModel, EmailStr


class Customer(BaseModel):
    id: int
    email: EmailStr
