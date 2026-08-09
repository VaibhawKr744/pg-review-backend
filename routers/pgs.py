from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from auth_utils import get_current_user
import models
import schemas

router = APIRouter(prefix="/pgs", tags=["pgs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.PGOut)
def create_pg(
    pg: schemas.PGCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    new_pg = models.PG(name=pg.name, city=pg.city, address=pg.address)

    db.add(new_pg)
    db.commit()
    db.refresh(new_pg)

    return new_pg


@router.get("/", response_model=List[schemas.PGOut])
def list_pgs(city: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.PG)

    if city:
        query = query.filter(models.PG.city.ilike(f"%{city}%"))

    return query.all()


@router.get("/{pg_id}", response_model=schemas.PGOut)
def get_pg(pg_id: int, db: Session = Depends(get_db)):
    pg = db.query(models.PG).filter(models.PG.id == pg_id).first()

    if not pg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PG not found",
        )

    return pg


@router.put("/{pg_id}", response_model=schemas.PGOut)
def update_pg(
    pg_id: int,
    updated_pg: schemas.PGCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    pg = db.query(models.PG).filter(models.PG.id == pg_id).first()

    if not pg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PG not found",
        )

    pg.name = updated_pg.name
    pg.city = updated_pg.city
    pg.address = updated_pg.address

    db.commit()
    db.refresh(pg)

    return pg


@router.delete("/{pg_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pg(
    pg_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    pg = db.query(models.PG).filter(models.PG.id == pg_id).first()

    if not pg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="PG not found",
        )

    db.delete(pg)
    db.commit()
