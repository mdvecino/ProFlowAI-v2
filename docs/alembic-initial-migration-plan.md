# Alembic Initial Migration Plan

## Goal

Create a single baseline migration that introduces all MVP foundation tables and constraints.

## Baseline Tables

- `companies`
- `roles`
- `users`
- `packing_lines`
- `batches`
- `stages`
- `downtime_logs`
- `shift_reports`
- `notifications`
- `audit_logs`

## Migration Order

1. Create lookup-independent tables:
   - `companies`
   - `roles`
2. Create identity tables:
   - `users` (FK to `companies`, `roles`)
3. Create operations tables:
   - `packing_lines` (FK to `companies`)
   - `batches` (FK to `companies`, `packing_lines`)
   - `stages` (FK to `batches`, `packing_lines`)
   - `downtime_logs` (FK to `companies`, `packing_lines`, `batches`)
4. Create reporting and support tables:
   - `shift_reports`
   - `notifications`
   - `audit_logs`

## Core Constraints and Indexes

- Unique constraints:
  - `roles`: (`company_id`, `name`)
  - `users`: (`company_id`, `email`)
  - `packing_lines`: (`company_id`, `code`)
  - `batches`: (`company_id`, `batch_number`)
- Indexes:
  - timestamps (`created_at`) for high-write entities
  - status columns used for dashboard filtering
  - foreign-key columns for tenant and relationship joins

## Seed Recommendations

After baseline migration:

1. Insert default role rows (`admin`, `supervisor`, `worker`) per company onboarding flow.
2. Create first company and admin user through a secure bootstrap command or management script.
