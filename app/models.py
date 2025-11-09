from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    external_id: Optional[str] = None
    amount_cents: int
    currency: str = "USD"
    status: str = "created"
    metadata: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class PaymentEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    payment_id: int
    event_type: str
    payload: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
