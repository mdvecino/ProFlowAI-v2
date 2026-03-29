# ProFlowAI v2

ProFlowAI v2 is a production operations platform for packhouses and packaging SMEs. It helps supervisors and operations teams track packing progress, monitor downtime, identify bottlenecks, and respond to delays in real time.

This is not a capstone prototype. ProFlowAI v2 is being built as a real-world, production-ready SaaS platform focused on practical operations visibility for small and medium packhouse businesses.

---

## Vision

Many packhouses still rely on paper records, spreadsheets, chat messages, and verbal updates to track daily operations. This makes it difficult to know:

- which batch is delayed
- which packing line is underperforming
- what downtime happened
- why output dropped
- what needs urgent attention during a shift

ProFlowAI v2 aims to solve that by providing a lightweight, usable system for real operational control without requiring expensive IoT infrastructure.

---

## Target Users

### Primary Users
- Packhouse supervisors
- Production managers
- Shift leaders
- Operations coordinators

### Secondary Users
- Packing line workers
- Administrators
- Business owners

---

## Core Problem

Packhouses often struggle with fragmented operational tracking. Daily production data is spread across multiple tools and informal communication channels, making it hard to maintain visibility and act early on delays.

Common operational pain points include:

- delayed batches discovered too late
- no consistent downtime records
- poor shift-to-shift handover visibility
- low traceability of issues
- difficulty identifying bottlenecks
- lack of simple performance dashboards

---

## Solution

ProFlowAI v2 is a packhouse-focused operations platform that centralizes:

- batch and packing line tracking
- stage-by-stage progress updates
- downtime logging
- shift reporting
- alerts and operational summaries
- practical AI-assisted insights

---

## Initial Product Scope

### MVP Modules

#### 1. Authentication and Access Control
- Secure login
- Role-based access control
- Multi-company support
- User roles:
  - Admin
  - Supervisor
  - Worker

#### 2. Batch and Work Tracking
- Create and manage packing batches
- Assign batches to packing lines
- Track stages such as:
  - Receiving
  - Sorting
  - Grading
  - Packing
  - Labelling
  - Palletizing
  - Dispatch
- Monitor planned vs actual progress

#### 3. Packing Line Monitoring
- View active lines
- View line status
- Track line output
- Track line performance by shift

#### 4. Downtime Logging
- Record downtime events quickly
- Categorize causes such as:
  - Machine issue
  - No fruit supply
  - Quality hold
  - Staff shortage
  - Maintenance
  - Packaging material shortage
- Add notes and timestamps
- Link downtime to a line, stage, or batch

#### 5. Supervisor Dashboard
- Active batches
- Delayed batches
- Current downtime
- Output by line
- Bottleneck stages
- Shift performance summary

#### 6. Alerts and Notifications
- Batch delay alerts
- Repeated downtime alerts
- Line slowdown alerts
- Missed target alerts

#### 7. Shift Reporting
- End-of-shift summary
- Completed batches
- Delayed batches
- Downtime causes
- Key issues and actions taken

#### 8. AI Insights
- Daily operational summary
- Delay risk indicators
- Repeated issue detection
- Bottleneck identification
- Natural language operational queries

---

## Product Goals

- Help supervisors know what is happening in production right now
- Reduce reaction time when delays happen
- Improve downtime visibility and accountability
- Make shift handovers clearer
- Provide usable insights without enterprise complexity
- Build a system SMEs can actually adopt

---

## Non-Goals for MVP

The following are intentionally out of scope for the first version:

- full ERP integration
- advanced predictive maintenance
- complex IoT hardware integration
- highly customized enterprise workflows
- heavy machine learning pipelines
- mobile app before core web platform is stable

---

## Tech Stack

### Frontend
- React
- TypeScript
- Vite
- Material UI
- React Router
- TanStack Query
- Recharts

### Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

### Infrastructure
- Docker
- Docker Compose
- Environment-based configuration
- REST API architecture

---

## Proposed Architecture

### Frontend
- Web dashboard for supervisors
- Worker task and update interface
- Admin settings and configuration pages

### Backend Services
- Auth service
- User and role service
- Batch tracking service
- Packing line service
- Downtime service
- Notification service
- Reporting service
- AI insights service

### Data Layer
- Multi-tenant PostgreSQL database
- Audit logging
- Operational event history

---

## Core Domain Entities

- Company
- User
- Role
- PackingLine
- Batch
- Stage
- Task
- DowntimeLog
- Notification
- ShiftReport
- AuditLog

---

## Sample User Flow

1. Supervisor creates a batch
2. Batch is assigned to a packing line
3. Workers update stage progress
4. Downtime is logged when issues happen
5. Dashboard updates line and batch status
6. Supervisor receives alerts on delays or repeated issues
7. End-of-shift summary is generated

---

## Example Use Cases

- A supervisor checks which line is falling behind target
- A worker logs a machine jam in under 10 seconds
- A manager reviews the most common downtime cause this week
- A shift leader reads an AI-generated summary before handover
- An admin reviews operational performance across lines

---

## Project Principles

- SME-first
- Simple before complex
- Fast data entry
- High operational visibility
- Practical AI, not hype
- Production-ready engineering
- Clear auditability
- Domain-specific design for packhouses

---

## Development Phases

### Phase 1 — Foundation
- Repository setup
- Monorepo or split repo decision
- Auth
- RBAC
- Database schema
- API skeleton
- Frontend shell

### Phase 2 — Core Operations
- Batch management
- Packing line views
- Stage progress tracking
- Downtime logging
- Dashboard

### Phase 3 — Operational Intelligence
- Alerts
- Shift summaries
- Reporting
- Basic AI insights

### Phase 4 — Production Readiness
- Multi-tenant hardening
- Audit logs
- Validation
- Error handling
- Testing
- Deployment
- Monitoring

---

## Folder Direction

```text
proflowai-v2/
  apps/
    web/
    api/
  packages/
    shared-types/
    ui/
  infrastructure/
    docker/
    scripts/
  docs/