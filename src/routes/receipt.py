from fastapi import APIRouter, Response, status
from src.models.receipt import Receipt
from src.core.receipt import ReceiptCore
from src.static.messages import DELETE_SUCESS, NOT_FOUND
from src.models.update_receipt import UpdateReceipt

from src.errors.user_not_found_exception import UserNotFoundException
from src.static.messages import NOT_FOUND, INTERNAL_ERROR


api_router = APIRouter(prefix="/receipt")


@api_router.get("", status_code=status.HTTP_200_OK)
def list_receipts():
    receipt_core = ReceiptCore()
    receipts = receipt_core.list_receipts()
    return receipts


@api_router.post("", status_code=status.HTTP_201_CREATED)
def add_receipt(receipt: Receipt):
    receipt_core = ReceiptCore()
    receipt_core.create_receipt(receipt)
    return receipt

@api_router.put("/{id}")
def update_registry(id: str, receipt: UpdateReceipt, response: Response):
    user_registry = ReceiptCore()
    try:
        return user_registry.update_receipt(id, receipt)
    except UserNotFoundException:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": NOT_FOUND.format("Receipt")}
    # except Exception:
    #     response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    #     return {"message": INTERNAL_ERROR}


@api_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_receipt(id: str, response: Response):
    receipt_core = ReceiptCore()
    receipt = receipt_core.delete_receipt(id)
    if not receipt:
        response.status_code = status.HTTP_404_NOT_FOUND
        return NOT_FOUND.format("Recibo")
    return DELETE_SUCESS.format("Recibo")


