import uuid
from typing import Tuple
from .config import settings

class MockGateway:
    def create_intent(self, amount_cents: int, currency: str) -> Tuple[str, dict]:
        external_id = f"mock_{uuid.uuid4()}"
        return external_id, {"status": "requires_confirmation"}

    def confirm_payment(self, external_id: str) -> dict:
        return {"status": "succeeded", "external_id": external_id}

    def refund(self, external_id: str, amount_cents: int | None = None) -> dict:
        return {"status": "refunded", "external_id": external_id, "amount_refunded": amount_cents}

def get_gateway():
    if settings.MOCK_GATEWAY:
        return MockGateway()
    return MockGateway()
