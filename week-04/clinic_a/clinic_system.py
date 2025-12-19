from clinic_service import ClinicService, seed_demo_data


if __name__ == "__main__":
    clinic = ClinicService("clinic.db")
    clinic.setup()
    seed_demo_data(clinic)

    seniors = clinic.report_senior_patients()
    print("Senior patients (age > 65):")
    for p in seniors:
        print(p)

    total_oph = clinic.report_ophthalmology_doctor_count()
    print("Total doctors specialising in ophthalmology:")
    print(total_oph)

