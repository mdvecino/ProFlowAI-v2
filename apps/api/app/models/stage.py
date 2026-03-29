import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import AuditMixin, Base


class StageName(str, enum.Enum):
    RECEIVING = "receiving"
    SORTING = "sorting"
    GRADING = "grading"
    PACKING = "packing"
    LABELLING = "labelling"
    PALLETIZING = "palletizing"
    DISPATCH = "dispatch"


class StageStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Stage(Base, AuditMixin):
    __tablename__ = "stages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    batch_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("batches.id"), nullable=False, index=True)
    packing_line_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("packing_lines.id"),
        nullable=True,
        index=True,
    )
    name: Mapped[StageName] = mapped_column(Enum(StageName, name="stage_name"), nullable=False)
    sequence_order: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    status: Mapped[StageStatus] = mapped_column(Enum(StageStatus, name="stage_status"), nullable=False, default=StageStatus.PENDING)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    batch = relationship("Batch", back_populates="stages")
