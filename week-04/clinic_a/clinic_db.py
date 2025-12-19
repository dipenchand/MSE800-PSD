import sqlite3


class ClinicDatabase:
    def __init__(self, db_path: str = "clinic.db") -> None:
        self.db_path = db_path

    def connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def initialize_schema(self) -> None:
        with self.connect() as conn:
            cursor = conn.cursor()

            # Create Patient Table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    phone TEXT
                )
                """
            )

            # Create Specialisation Table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS specialisations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT
                )
                """
            )

            # Create Doctor Table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS doctors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialisation_id INTEGER NOT NULL,
                    phone TEXT,
                    FOREIGN KEY (specialisation_id) REFERENCES specialisations (id)
                )
                """
            )

            # Create Appointment Table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    doctor_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    status TEXT DEFAULT 'scheduled',
                    FOREIGN KEY (patient_id) REFERENCES patients (id),
                    FOREIGN KEY (doctor_id) REFERENCES doctors (id)
                )
                """
            )

            conn.commit()
