# Design and Architecture (Task 1 — LO1)

## Architectural Style

CRMS uses a layered architecture with clear separation of concerns:

- **Presentation Layer**: `main.py` (curses-based TUI) + `utils/tui.py`
- **Service (Business Logic) Layer**: `services/*.py`
- **Domain Model Layer**: `models/*.py`
- **Data Access Layer**: `database.py` (SQLite)

This structure improves maintainability and testability by isolating UI concerns from business rules and persistence.

## Component Responsibilities

### Presentation Layer

- **`CarRentalApp` (`main.py`)**
  - Owns UI state (`current_user`, `current_company`)
  - Routes user actions to the correct service methods
  - Renders tables/menus via `TUI`

- **`TUI` (`utils/tui.py`)**
  - Reusable drawing and input helpers (`draw_top_bar`, `draw_table`, `get_input`, `get_password`)

- **`Validator` (`utils/validators.py`)**
  - Input validation helpers (email/date)

### Service Layer

- **`AuthService`**
  - Registers users (password hashing)
  - Authenticates login
  - Maps DB rows to domain objects (`Admin` / `Customer`)

- **`CompanyService`**
  - Creates and manages companies
  - Supports soft delete via `is_active`

- **`CarService`**
  - CRUD operations for cars
  - Lists all or available cars, optionally filtered by `company_id`

- **`RentalService`**
  - Calculates booking fee based on date delta and daily rate
  - Creates booking requests
  - Admin approval/rejection workflow

### Data Access Layer

- **`DatabaseManager` (`database.py`)**
  - Provides SQLite connections and table initialization
  - Exposes `execute_query`, `fetch_one`, `fetch_all`

## Design Patterns Used

- **Singleton (Thread-safe)**
  - `DatabaseManager` uses a lock and a single shared instance to ensure a consistent database connection configuration.

- **Service Layer / Facade**
  - `AuthService`, `CarService`, `RentalService`, `CompanyService` hide SQL details and expose higher-level operations.

- **Factory-like Object Creation**
  - `AuthService.login()` returns either `Admin` or `Customer` based on the `role` column.

## Key Data Entities

- **Company**: a rental company/branch (multi-tenant boundary)
- **User**: abstract base class; concrete roles `Admin` and `Customer`
- **Car**: inventory item with availability and rental constraints
- **Booking**: rental request and status (`PENDING`, `APPROVED`, `REJECTED`)

## Main Interaction Flows

### Customer Booking Flow (high level)

1. Customer logs in
2. Views available cars
3. Enters rental dates
4. System calculates fee
5. Booking is created as `PENDING`

### Admin Approval Flow (high level)

1. Admin views bookings
2. Selects a pending booking
3. Approves or rejects
4. If approved, booking becomes `APPROVED` and car availability becomes unavailable

## UML Diagrams

UML sources are provided as PlantUML files under `docs/uml/`:

- `docs/uml/class_diagram.puml`
- `docs/uml/use_case_diagram.puml`
- `docs/uml/sequence_booking.puml`
- `docs/uml/sequence_approval.puml`

### Exporting Diagrams to Images/PDF

You can render PlantUML using:

- VS Code extension: **PlantUML** (recommended)
- Local PlantUML + Graphviz install

After rendering to images (PNG/SVG), you can export this document to PDF using your editor’s Markdown-to-PDF feature.
