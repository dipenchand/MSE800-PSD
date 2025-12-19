import sqlite3

from clinic_db import ClinicDatabase


class DoctorRepository:
    def __init__(self, db: ClinicDatabase) -> None:
        self.db = db

    def _get_or_create_specialisation_id(self, name: str) -> int:
        normalized = name.strip()
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR IGNORE INTO specialisations (name) VALUES (?)",
                (normalized,),
            )
            cursor.execute("SELECT id FROM specialisations WHERE name = ?", (normalized,))
            row = cursor.fetchone()
            conn.commit()
            if row is None:
                raise RuntimeError("Failed to create or fetch specialisation")
            return int(row["id"])

    def add_doctor(
        self,
        name: str,
        specialisation_name: str,
        email: str | None = None,
        phone: str | None = None,
    ) -> int:
        specialisation_id = self._get_or_create_specialisation_id(specialisation_name)
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO doctors (name, email, phone, specialisation_id)
                VALUES (?, ?, ?, ?)
                """,
                (name, email, phone, specialisation_id),
            )
            conn.commit()
            return int(cursor.lastrowid)

    def count_doctors_by_specialisation(self, specialisation_name: str) -> int:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT COUNT(*) AS total
                FROM doctors d
                JOIN specialisations s ON s.id = d.specialisation_id
                WHERE LOWER(s.name) = LOWER(?)
                """,
                (specialisation_name.strip(),),
            )
            row = cursor.fetchone()
            return int(row["total"]) if row is not None else 0
