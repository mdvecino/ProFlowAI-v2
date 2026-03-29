import uuid

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Company(Base, TimestampMixin):
    __tablename__ = "companies"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    timezone: Mapped[str] = mapped_column(String(100), nullable=False, default="Pacific/Auckland")

    users = relationship("User", back_populates="company")
    packing_lines = relationship("PackingLine", back_populates="company")
    batches = relationship("Batch", back_populates="company")
