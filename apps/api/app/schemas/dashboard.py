from pydantic import BaseModel


class DashboardSummary(BaseModel):
    active_batches: int
    delayed_batches: int
    downtime_today: int
    active_lines: int
