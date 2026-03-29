# ProFlowAI v2 Architecture

ProFlowAI v2 uses a modular monorepo structure with separate API and web applications under `apps/`.

## API Architecture

- **Framework:** FastAPI
- **Data:** PostgreSQL via SQLAlchemy 2.x
- **Migrations:** Alembic
- **Auth:** JWT bearer tokens with bcrypt password hashing

### Layering

- `api/v1/routes`: HTTP endpoints and request/response orchestration
- `core`: configuration, security, and shared dependencies
- `services`: business logic and domain workflows
- `repositories`: focused data-access helpers where useful
- `models` + `schemas`: persistence entities and API contracts

### Multi-Tenant Direction

Operational entities include `company_id` and audit-friendly timestamps to support tenant boundaries and traceability.

## Web Architecture (planned)

- React + TypeScript + Vite
- Material UI + React Router
- TanStack Query for server-state management
- React Hook Form + Zod for validated data entry
