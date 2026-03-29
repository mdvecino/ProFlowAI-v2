from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.user_repository.get_by_email(email=email)
        if not user:
            return None
        if not user.is_active:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def create_user_access_token(self, user: User) -> str:
        return create_access_token(subject=str(user.id))
