from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..schemas import PaymentCreate, PaymentOut, ConfirmResponse, RefundRequest
from ..db import get_session
from ..crud import create_payment, get_payment, list_payments, update_payment_status, add_event
from ..gateway import get_gateway
from typing import List
import json

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("", response_model=PaymentOut)
def create_payment_endpoint(payload: PaymentCreate, session: Session = Depends(get_session)):
    p = create_payment(session, payload.amount_cents, payload.currency, payload.metadata)
    gateway = get_gateway()
    external_id, info = gateway.create_intent(p.amount_cents, p.currency)
    update_payment_status(session, p, "created", external_id)
    add_event(session, p.id, "created", {"gateway_info": info})
    return PaymentOut(
        id=p.id,
        external_id=p.external_id,
        amount_cents=p.amount_cents,
        currency=p.currency,
        status=p.status,
        metadata=json.loads(p.metadata) if p.metadata else None,
        created_at=p.created_at.isoformat(),
        updated_at=p.updated_at.isoformat(),
    )
