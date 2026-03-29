from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserRead)
def get_current_user_profile(current_user: User = Depends(get_current_user)) -> UserRead:
    return UserRead.model_validate(current_user)


@router.get("", response_model=list[UserRead])
def list_company_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[UserRead]:
    users = db.scalars(select(User).where(User.company_id == current_user.company_id)).all()
    return [UserRead.model_validate(user) for user in users]
