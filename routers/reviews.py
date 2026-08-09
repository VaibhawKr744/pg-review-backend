from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from auth_utils import get_current_user
import models
import schemas

router = APIRouter(prefix="/pgs/{pg_id}/reviews", tags=["reviews"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ReviewOut)
def create_review(
    pg_id: int,
    review: schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    pg = db.query(models.PG).filter(models.PG.id == pg_id).first()
    if not pg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PG not found",
        )

    new_review = models.Review(
        pg_id=pg_id,
        user_id=current_user.id,
        rating=review.rating,
        deposit_returned=review.deposit_returned,
        comment=review.comment,
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review


@router.get("/", response_model=List[schemas.ReviewOut])
def list_reviews(pg_id: int, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.pg_id == pg_id).all()
