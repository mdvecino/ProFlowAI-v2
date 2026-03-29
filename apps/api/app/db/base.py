from app.models.base import Base
from app.models import (  # noqa: F401
    AuditLog,
    Batch,
    Company,
    DowntimeLog,
    Notification,
    PackingLine,
    Role,
    ShiftReport,
    Stage,
    User,
)

metadata = Base.metadata
