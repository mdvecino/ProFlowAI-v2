import enum
import uuid

from sqlalchemy import Enum, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import AuditMixin, Base


class PackingLineStatus(str, enum.Enum):
    ACTIVE = "active"
    IDLE = "idle"
    DOWN = "down"


class PackingLine(Base, AuditMixin):
    __tablename__ = "packing_lines"
    __table_args__ = (UniqueConstraint("company_id", "code", name="uq_packing_lines_company_code"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[PackingLineStatus] = mapped_column(
        Enum(PackingLineStatus, name="packing_line_status"),
        default=PackingLineStatus.IDLE,
        nullable=False,
    )

    company = relationship("Company", back_populates="packing_lines")
    batches = relationship("Batch", back_populates="packing_line")
