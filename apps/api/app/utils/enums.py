import enum


class RoleName(str, enum.Enum):
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    WORKER = "worker"
