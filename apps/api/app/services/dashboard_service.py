from datetime import datetime, timedelta, timezone
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.batch import Batch, BatchStatus
from app.models.downtime_log import DowntimeLog
from app.models.packing_line import PackingLine, PackingLineStatus
from app.schemas.dashboard import DashboardSummary


class DashboardService:
    def __init__(self, db: Session):
        self.db = db

    def get_summary(self, company_id: UUID) -> DashboardSummary:
        active_batches = self.db.scalar(
            select(func.count(Batch.id)).where(
                Batch.company_id == company_id,
                Batch.status == BatchStatus.IN_PROGRESS,
            )
        ) or 0

        delayed_batches = self.db.scalar(
            select(func.count(Batch.id)).where(
                Batch.company_id == company_id,
                Batch.status == BatchStatus.DELAYED,
            )
        ) or 0

        now = datetime.now(timezone.utc)
        day_start = datetime(year=now.year, month=now.month, day=now.day, tzinfo=timezone.utc)
        day_end = day_start + timedelta(days=1)

        downtime_today = self.db.scalar(
            select(func.count(DowntimeLog.id)).where(
                DowntimeLog.company_id == company_id,
                DowntimeLog.start_time >= day_start,
                DowntimeLog.start_time < day_end,
            )
        ) or 0

        active_lines = self.db.scalar(
            select(func.count(PackingLine.id)).where(
                PackingLine.company_id == company_id,
                PackingLine.status == PackingLineStatus.ACTIVE,
            )
        ) or 0

        return DashboardSummary(
            active_batches=active_batches,
            delayed_batches=delayed_batches,
            downtime_today=downtime_today,
            active_lines=active_lines,
        )
