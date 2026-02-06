## Design patterns used (W7-A3)

### 1) Factory Pattern
In `botfactory.py`, `Maker.produce(unit_type, id)` centralizes object creation and returns the correct `Unit` subtype (Either `Helper` or `Friend`) based on a string, so `main.py` doesn’t need to know concrete classes.

- **Advantages**
  - Calling code depends on the `Unit`, not specific subclasses.
  - New unit types can be added in one place.
- **Disadvantages**
  - Can grow into a long if/elif chain: adding many types makes the factory harder to maintain.

### 2) Singleton Pattern
In `core.py`, `KeeperMeta.__call__` ensures only one `Keeper` instance exists, so all code that calls `Keeper()` shares the same central `units` collection.

- **Advantages**
  - Shared manager for state like `units`.
  - Prevents accidental multiple managers
- **Disadvantages**
  - Can make behaviour harder to reason about and debug.

### 3) Observer Pattern
In `tracker.py`, `Watcher` defines a common `notice(msg)` class and `Screen` and `Record` provide interchangeable implementations.

- **Advantages**
  - Output/logging can change without touching core logic
  - We can add new notification targets by creating another `Watcher` class.
- **Disadvantages**
  - For small programs can feel over-engineered
