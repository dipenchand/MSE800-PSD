# Maintenance and Support (Task 3 — LO2)

## Objectives

This plan outlines how CRMS can evolve over time while remaining reliable and maintainable. It focuses on:

- Managing ongoing maintenance
- Versioning and release strategy
- Backward compatibility and safe evolution

## Maintenance Strategy

### Defect Management

- **Bug reporting**
  - Record steps to reproduce, expected vs actual behaviour, environment details.
- **Triage**
  - Classify by severity (blocker/major/minor) and impacted area (UI/service/data).
- **Fix workflow**
  - Add a failing test (where possible), implement fix, ensure tests pass.

### Logging and Diagnostics

- Application logging is enabled via Python `logging` in `main.py` to `car_rental.log`.
- Future improvements:
  - Rotate logs (size-based)
  - Add structured logging fields (company_id, user_id, booking_id)

### Security Maintenance

- Passwords are hashed (`sha256`) before storing.
- Future improvements:
  - Use salted hashing (e.g., `bcrypt`) for stronger security
  - Avoid logging sensitive values

## Versioning Strategy

Use **Semantic Versioning**:

- **MAJOR**: breaking changes (schema changes without migration, API changes)
- **MINOR**: new features (new reports, pricing rules, company admin UI)
- **PATCH**: bug fixes, small improvements

Example: `v1.2.3`

## Backward Compatibility Strategy

### Database Schema Evolution

- Introduce a controlled migration process:
  - Keep a `schema_version` table
  - Apply incremental SQL migrations: `migrations/001_init.sql`, `migrations/002_add_indexes.sql`, etc.

### Data Contract Stability

- Preserve core entity fields (`users`, `cars`, `bookings`) unless a MAJOR release is planned.
- Prefer additive changes:
  - Add new nullable columns rather than removing existing ones.

### UI Compatibility

- Maintain stable menu navigation keys where possible.
- Add new features as additional menu items (MINOR version) rather than changing existing workflows.

## Release and Deployment Plan

### Release Process

- Maintain a changelog:
  - Added / Changed / Fixed
- Tag releases in version control.
- Package release build:
  - Zip the project folder
  - Ensure `car_rental.db` is not shipped unless intended (prefer fresh DB on install)

### Quality Gates

- Unit tests (`test_all.py`) pass
- Manual smoke tests:
  - Admin: add car, list cars, approve/reject booking
  - Customer: register, login, view cars, book, view history

## Roadmap (Evolution Over Time)

- **v1.1 (Minor)**
  - Company management UI (admin): create/deactivate companies
  - Improve validation (rent period checks, availability checks)

- **v1.2 (Minor)**
  - Pricing enhancements: minimum/maximum rental period enforcement and surcharges
  - Booking overlap detection

- **v2.0 (Major)**
  - Replace SHA-256 with bcrypt
  - Introduce full migration support and stronger transaction handling

## Known Risks and Mitigations

- **DatabaseManager singleton in tests**
  - Risk: tests may unintentionally share the main DB depending on initialization order.
  - Mitigation: allow dependency injection of DB name into services or reset singleton for tests.

- **Transaction safety during approval**
  - Risk: booking approval updates booking and car in separate calls.
  - Mitigation: implement explicit SQLite transactions.
