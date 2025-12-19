import sqlite3

from clinic_db import ClinicDatabase
from doctor_repository import DoctorRepository
from patient_repository import PatientRepository


class ClinicService:
    def __init__(self, db_path: str = "clinic.db") -> None:
        self.db = ClinicDatabase(db_path)
        self.patients = PatientRepository(self.db)
        self.doctors = DoctorRepository(self.db)

    def setup(self) -> None:
        self.db.initialize_schema()

    def report_senior_patients(self) -> list[dict]:
        return [dict(row) for row in self.patients.list_senior_patients()]

    def report_ophthalmology_doctor_count(self) -> int:
        return self.doctors.count_doctors_by_specialisation("ophthalmology")


def seed_demo_data(service: ClinicService) -> None:
    try:
        service.patients.add_patient("John Smith", 70, "john.smith@example.com", "021-111-111")
        service.patients.add_patient("Ava Chen", 34, "ava.chen@example.com", "021-222-222")
        service.patients.add_patient("Mary Patel", 82, "mary.patel@example.com", "021-333-333")
    except sqlite3.IntegrityError:
        pass

    try:
        service.doctors.add_doctor("Dr Alice Brown", "ophthalmology", "alice.brown@clinic.test")
        service.doctors.add_doctor("Dr Ben Wilson", "ophthalmology", "ben.wilson@clinic.test")
        service.doctors.add_doctor("Dr Chloe King", "cardiology", "chloe.king@clinic.test")
    except sqlite3.IntegrityError:
        pass
