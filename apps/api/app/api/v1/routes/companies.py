from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.company import Company
from app.models.user import User
from app.schemas.company import CompanyRead

router = APIRouter(prefix="/companies", tags=["companies"])


@router.get("/me", response_model=CompanyRead)
def get_my_company(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CompanyRead:
    company = db.scalars(select(Company).where(Company.id == current_user.company_id)).first()
    if company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return CompanyRead.model_validate(company)
