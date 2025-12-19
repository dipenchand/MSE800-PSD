import sqlite3

from clinic_db import ClinicDatabase


class PatientRepository:
    def __init__(self, db: ClinicDatabase) -> None:
        self.db = db

    def add_patient(self, name: str, age: int, email: str, phone: str | None = None) -> int:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO patients (name, age, email, phone) VALUES (?, ?, ?, ?)",
                (name, age, email, phone),
            )
            conn.commit()
            return int(cursor.lastrowid)

    def list_senior_patients(self) -> list[sqlite3.Row]:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, age, email, phone FROM patients WHERE age > ? ORDER BY name",
                (65,),
            )
            return list(cursor.fetchall())
