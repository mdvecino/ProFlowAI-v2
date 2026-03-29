import uuid
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import AuditMixin, Base


class ShiftReport(Base, AuditMixin):
    __tablename__ = "shift_reports"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    packing_line_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("packing_lines.id"),
        nullable=True,
        index=True,
    )
    shift_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    shift_name: Mapped[str] = mapped_column(String(50), nullable=False)
    completed_batches: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    delayed_batches: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    downtime_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
