# Frontend Scaffold Plan

## Goals

- Build a clean supervisor-first dashboard experience.
- Keep worker data-entry flows fast and minimal.
- Use role-aware routing and page access from the beginning.

## Initial App Skeleton

- Vite + React + TypeScript app shell.
- Material UI theme and base layout.
- React Router route tree with protected routes.
- TanStack Query client setup.

## Initial Pages

- `LoginPage`
- `DashboardPage`
- `BatchesPage`
- `PackingLinesPage`
- `DowntimeLogPage`
- `ShiftReportsPage`

## Layout and Navigation

- Sidebar with role-aware nav items.
- Top bar showing company and active user context.
- Main content area optimized for tables, cards, and quick forms.

## Form and Validation Standards

- `react-hook-form` for form handling.
- `zod` schemas for client-side validation.
- Compact forms with operational labels used by packhouse teams.

## API Integration Approach

- Centralized API client module.
- Auth token persistence and refresh-safe request handling.
- Query keys by module (`dashboard`, `batches`, `lines`, `downtime`, `shiftReports`).

## Milestone Sequence

1. Scaffold app shell + routing.
2. Implement login and auth guard.
3. Build dashboard widgets with placeholder API integration.
4. Add list and create flows for batches, lines, and downtime.
5. Add shift report view and summary cards.
