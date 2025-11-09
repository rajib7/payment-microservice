from sqlmodel import Session, select
from .models import Payment, PaymentEvent
from datetime import datetime
import json

def create_payment(session: Session, amount_cents: int, currency: str, metadata: dict | None):
    p = Payment(amount_cents=amount_cents, currency=currency, metadata=json.dumps(metadata) if metadata else None)
    session.add(p)
    session.commit()
    session.refresh(p)
    return p

def get_payment(session: Session, payment_id: int):
    return session.get(Payment, payment_id)

def list_payments(session: Session, limit: int = 100):
    q = select(Payment).limit(limit)
    return session.exec(q).all()

def update_payment_status(session: Session, payment: Payment, status: str, external_id: str | None = None):
    payment.status = status
    if external_id:
        payment.external_id = external_id
    payment.updated_at = datetime.utcnow()
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment

def add_event(session: Session, payment_id: int, event_type: str, payload: dict | None):
    ev = PaymentEvent(payment_id=payment_id, event_type=event_type, payload=json.dumps(payload) if payload else None)
    session.add(ev)
    session.commit()
    session.refresh(ev)
    return ev
