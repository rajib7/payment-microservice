from typing import Optional
from pydantic import BaseModel, PositiveInt

class PaymentCreate(BaseModel):
    amount_cents: PositiveInt
    currency: Optional[str] = "USD"
    metadata: Optional[dict] = None

class PaymentOut(BaseModel):
    id: int
    external_id: Optional[str]
    amount_cents: int
    currency: str
    status: str
    metadata: Optional[dict]
    created_at: str
    updated_at: str

class ConfirmResponse(BaseModel):
    success: bool
    message: Optional[str]

class RefundRequest(BaseModel):
    amount_cents: Optional[int] = None
    reason: Optional[str] = None
