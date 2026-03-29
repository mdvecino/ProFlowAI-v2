# Backend Architecture Plan

## Objectives

- Keep route handlers thin and focused on HTTP concerns.
- Keep business logic in services.
- Use repositories for persistence-heavy modules where it improves readability.
- Support multi-tenant design from day one through `company_id` boundaries.
- Ensure audit-friendly fields and timestamps across core entities.

## Runtime Layers

1. **API Layer** (`app/api/v1/routes`)
   - Auth endpoints, operational endpoints, dashboard endpoints.
   - Input/output validation via Pydantic schemas.
2. **Service Layer** (`app/services`)
   - Authentication, dashboard summary, domain workflows.
3. **Repository Layer** (`app/repositories`)
   - User lookup and future domain repositories.
4. **Data Layer** (`app/models`, `app/db`)
   - SQLAlchemy 2.x ORM models and session management.

## Key Modules (MVP Foundation)

- `auth`: login + current user profile
- `company`: tenancy boundary
- `users`: user identity and role assignment
- `packing lines`: line setup and status foundation
- `batches`: operational batch tracking foundation
- `downtime`: event logging foundation
- `dashboard`: summary aggregates for supervisor visibility

## Security and Access

- JWT bearer tokens for API authentication.
- Password hashing via `passlib[bcrypt]`.
- Role model includes `admin`, `supervisor`, `worker`.
- Current-user dependency validates token and loads active user.

## Multi-Tenant Readiness

- Domain models include `company_id` where applicable.
- API patterns assume data filtering by tenant context.
- Auditable timestamps and actor fields (`created_by`, `updated_by`) are included in core tables.

## Next Implementation Steps

1. Create base DB and model foundation.
2. Wire auth and user repository.
3. Add batch, line, downtime CRUD endpoints.
4. Add dashboard aggregate endpoint with tenant-scoped filters.
5. Generate and apply first Alembic migration.
