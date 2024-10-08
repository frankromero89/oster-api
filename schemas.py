from pydantic import BaseModel


class userCreate(BaseModel):
    name: str
    paternal_lastname: str
    maternal_lastname: str
    email: str
    mobile_phone: str
    land_line: str
    street: str
    block: str
    postal_code: str
    locality: str
    birth_date: str
    gender: str
    ticket_folio: str
    purchase_date: str
    purchase_amount: float
    store: str
    terminal: str
    seller: str