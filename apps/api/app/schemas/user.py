import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    company_id: uuid.UUID
    role_id: uuid.UUID
    email: EmailStr
    full_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
