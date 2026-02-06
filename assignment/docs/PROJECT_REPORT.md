# Project Report — Car Rental Management System (CRMS)

## Programme / Course / Assessment Context

- **Programme**: Master of Software Engineering
- **Course**: MSE800 Professional Software Engineering (Level 8, 30 Credits)
- **Assignment**: Assignment 1 — Object-Oriented Programming (Individual)
- **System**: Car Rental Management System (CRMS)

## Executive Summary

CRMS is a terminal-based (TUI) car rental system implemented in Python using a layered, object-oriented architecture.
The system supports **role-based access** (Admin vs Customer), manages **cars**, and manages **rental bookings** end-to-end (request, approval/rejection, and availability updates). Data persistence is handled via **SQLite**, accessed through a thread-safe **Singleton** database manager.

A distinguishing enhancement over a basic car-rental example is **multi-company (multi-tenant) support**, enabling multiple rental companies/branches to co-exist in the same application and database.

## Learning Outcomes Mapping

- **Task 1 (Design and Architecture)** → **LO1**, **GPO1**
- **Task 2 (Innovative Solutions)** → **LO2**, **GPO4**
- **Task 3 (Software Evolution)** → **LO2**, **GPO4**

## System Overview

### Core Features

- **User Management**
  - Registration and login
  - Role differentiation: Admin and Customer
  - Company assignment (multi-tenant)

- **Car Management (Admin)**
  - Add, update, delete car records
  - View all cars for a selected company

- **Rental Booking (Customer)**
  - View available cars
  - Create booking request with rental dates
  - Fee calculation based on day count and daily rate

- **Rental Management (Admin)**
  - View bookings
  - Approve or reject pending bookings
  - Approving a booking marks the car as unavailable

## Deliverables in This Repository

- **User + Programmer Documentation**
  - `README.md`

- **Design and Architecture (Task 1)**
  - `docs/Design_and_Architecture.md`
  - UML sources (PlantUML)
    - `docs/uml/class_diagram.puml`
    - `docs/uml/use_case_diagram.puml`
    - `docs/uml/sequence_booking.puml`
    - `docs/uml/sequence_approval.puml`

- **Innovative Solutions (Task 2)**
  - `docs/Innovative_Feature.md`

- **Software Evolution + Maintenance & Support (Task 3)**
  - `docs/Maintenance_and_Support.md`

## Testing Summary

Automated tests are provided in `test_all.py` and cover:

- User registration + login
- Car add/list
- Booking creation + approval workflow

## Conclusion

CRMS demonstrates key professional software engineering practices expected at Level 8:

- Object-oriented decomposition into **models**, **services**, and **UI utilities**
- Use of common patterns (Singleton, simple Factory, service layer)
- Persistent storage via SQLite
- A clear pathway for maintenance, versioning, and future evolution
