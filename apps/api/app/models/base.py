from sqlalchemy.orm import DeclarativeBase

from app.models.mixins import AuditMixin, TimestampMixin


class Base(DeclarativeBase):
    pass
