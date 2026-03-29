from fastapi import APIRouter, HTTPException, Depends
from app.schemas.book_schema import BookCreate, BookUpdate
from app.services.book_service import BookService
from app.core.dependencies import require_role

router = APIRouter(tags=["Books"])

book_service = BookService()

@router.get("/")
async def get_books():
    return await book_service.get_books()

@router.get("/{book_id}")
async def get_book(book_id: str):
    try:
        return await book_service.get_book(book_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/")
async def create_book(book: BookCreate, admin=Depends(require_role("admin"))):
    return await book_service.create_book(book.dict())

@router.put("/{book_id}")
async def update_book(
    book_id: str,
    book: BookUpdate,
    admin=Depends(require_role("admin"))
):
    await book_service.update_book(book_id, book.dict(exclude_unset=True))
    return {"message": "Updated"}

@router.delete("/{book_id}")
async def delete_book(book_id: str, admin=Depends(require_role("admin"))):
    await book_service.delete_book(book_id)
    return {"message": "Deleted"}
