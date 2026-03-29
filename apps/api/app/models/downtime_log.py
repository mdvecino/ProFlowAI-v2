import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import AuditMixin, Base


class DowntimeCategory(str, enum.Enum):
    MACHINE_ISSUE = "machine_issue"
    NO_FRUIT_SUPPLY = "no_fruit_supply"
    QUALITY_HOLD = "quality_hold"
    STAFF_SHORTAGE = "staff_shortage"
    MAINTENANCE = "maintenance"
    PACKAGING_SHORTAGE = "packaging_shortage"


class DowntimeSeverity(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class DowntimeLog(Base, AuditMixin):
    __tablename__ = "downtime_logs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    packing_line_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("packing_lines.id"),
        nullable=True,
        index=True,
    )
    batch_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("batches.id"), nullable=True, index=True)
    category: Mapped[DowntimeCategory] = mapped_column(Enum(DowntimeCategory, name="downtime_category"), nullable=False)
    severity: Mapped[DowntimeSeverity] = mapped_column(
        Enum(DowntimeSeverity, name="downtime_severity"),
        nullable=False,
        default=DowntimeSeverity.MEDIUM,
    )
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, index=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    reported_by: Mapped[str | None] = mapped_column(String(255), nullable=True)
