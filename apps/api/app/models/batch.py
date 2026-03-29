import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import AuditMixin, Base


class BatchStatus(str, enum.Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    DELAYED = "delayed"


class Batch(Base, AuditMixin):
    __tablename__ = "batches"
    __table_args__ = (UniqueConstraint("company_id", "batch_number", name="uq_batches_company_batch_number"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    packing_line_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("packing_lines.id"),
        nullable=True,
        index=True,
    )
    batch_number: Mapped[str] = mapped_column(String(100), nullable=False)
    product_name: Mapped[str] = mapped_column(String(255), nullable=False)
    planned_quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    actual_quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    due_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, index=True)
    status: Mapped[BatchStatus] = mapped_column(Enum(BatchStatus, name="batch_status"), default=BatchStatus.PLANNED, nullable=False)

    company = relationship("Company", back_populates="batches")
    packing_line = relationship("PackingLine", back_populates="batches")
    stages = relationship("Stage", back_populates="batch")
