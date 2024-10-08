# business.py
from sqlalchemy.orm import Session
from models import User, SessionLocal
from schemas import userCreate

# Función para crear un nuevo ítem
def create_user(user: userCreate):
    session = SessionLocal()
    new_item = User(
        name=user.name,
        paternal_lastname=user.paternal_lastname,
        maternal_lastname=user.maternal_lastname,
        email=user.email,
        mobile_phone=user.mobile_phone,
        land_line=user.land_line,
        street=user.street,
        block=user.block,
        postal_code=user.postal_code,
        locality=user.locality,
        birth_date=user.birth_date,
        gender=user.gender,
        ticket_folio=user.ticket_folio,
        purchase_date=user.purchase_date,
        purchase_amount=user.purchase_amount,
        store=user.store,
        terminal=user.terminal,
        seller=user.seller
    )
    print(f'new_item: {new_item}')
    session.add(new_item)
    session.commit()
    session.refresh(new_item)
    session.close()
    return new_item
