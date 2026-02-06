# Innovative Solutions (Task 2 — LO2)

## Proposed / Implemented Innovation: Multi-Company (Multi-Tenant) Car Rental

### Summary

A common limitation in simple car rental systems is that they only support a single business. CRMS goes beyond this by supporting **multiple companies/branches** inside the same system.

### What the System Does

- Stores companies in the `companies` table.
- Associates users, cars, and bookings with a `company_id`.
- During registration, users can select a company (or use the default).
- The application filters cars and bookings by the currently selected company context.

### Why It Matters (Industry Requirement)

Real car rental operators frequently run multiple branches/brands or manage fleets on behalf of partner organisations. Multi-tenancy supports:

- Company-level separation of inventory and bookings
- Centralised administration of the platform
- Reduced operational costs by avoiding separate deployments/databases

### Competitive Advantage

- **Scalability**: new companies can be onboarded without new infrastructure.
- **Maintainability**: one codebase and database schema supports many tenants.
- **Clear governance**: data is partitioned by `company_id` across the core entities.

### Where It Appears in the Code

- Database schema: `database.py` tables `companies`, `users.company_id`, `cars.company_id`, `bookings.company_id`
- Services:
  - `services/company_service.py`
  - `services/car_service.py` (optional `company_id` filters)
  - `services/rental_service.py` (optional `company_id` filters)
- UI:
  - `main.py` registration includes company selection
  - `main.py` lists cars/bookings under the active company context

### Future Enhancements (Next Step)

To further strengthen the innovation, future versions could add:

- Admin UI for company creation/deactivation
- Company-specific pricing rules (peak/off-peak, loyalty tiers)
- Reporting dashboards (utilisation rate per company)
