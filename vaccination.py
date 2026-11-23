"""PROG211 — Vaccination Record and Tracking System (educational demo).

No external packages, database, or patient-data persistence.
Use fictional demonstration data only.
"""


class Patient:
    """Represents a patient associated with a vaccination record."""

    def __init__(self, patient_id, name, age, phone):
        if not patient_id.strip() or not name.strip():
            raise ValueError("Patient ID and name are required.")
        if age < 0 or age > 130:
            raise ValueError("Age must be between 0 and 130.")
        self.patient_id = patient_id.strip()
        self.name = name.strip()
        self.age = age
        self.phone = phone.strip()

    def display_details(self):
        return (
            f"Patient ID: {self.patient_id}\n"
            f"Patient Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Phone: {self.phone}"
        )


class VaccinationRecord:
    """Connects a Patient object to vaccine details and a status."""

    total_records = 0

    def __init__(self, record_id, patient, vaccine_name, dose_number,
                 vaccination_date, status):
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient object.")
        if not vaccine_name.strip():
            raise ValueError("Vaccine name is required.")
        if dose_number < 1:
            raise ValueError("Dose number must be at least 1.")
        if not vaccination_date.strip():
            raise ValueError("Vaccination date is required.")
        if not self.validate_status(status):
            raise ValueError("Invalid vaccination status.")
        self.record_id = record_id
        self.patient = patient
        self.vaccine_name = vaccine_name.strip()
        self.dose_number = dose_number
        self.vaccination_date = vaccination_date.strip()
        self.status = status
        type(self).total_records += 1

    def display_record(self):
        return (
            f"Record ID: {self.record_id}\n"
            f"{self.patient.display_details()}\n"
            f"Vaccine Name: {self.vaccine_name}\n"
            f"Dose Number: {self.dose_number}\n"
            f"Vaccination Date: {self.vaccination_date}\n"
            f"Status: {self.status}"
        )

    def update_status(self, new_status):
        if not self.validate_status(new_status):
            raise ValueError("Invalid vaccination status.")
        self.status = new_status

    @classmethod
    def get_total_records(cls):
        """Total records created since this Python process started."""
        return cls.total_records

    @staticmethod
    def validate_status(status):
        return status == "Pending" or status == "Vaccinated" or status == "Completed"


class VaccinationSystem:
    """Manages records using exactly one dictionary of record objects."""

    def __init__(self):
        self.vaccination_records = {}
        self._next_record_number = 1

    def register_vaccination(self, patient_id, name, age, phone, vaccine_name,
                             dose_number, vaccination_date, status):
        patient = Patient(patient_id, name, age, phone)
        record_id = "VAC" + str(self._next_record_number).zfill(3)
        record = VaccinationRecord(record_id, patient, vaccine_name,
                                   dose_number, vaccination_date, status)
        self.vaccination_records[record_id] = record
        self._next_record_number += 1
        return record

    def search_record(self, record_id):
        return self.vaccination_records.get(record_id.strip().upper())

    def update_vaccination_status(self, record_id, new_status):
        record = self.search_record(record_id)
        if record is None:
            return False
        record.update_status(new_status)
        return True

    def display_all_records(self):
        if not self.vaccination_records:
            return "No vaccination records available."
        return "\n\n".join(
            record.display_record() for record in self.vaccination_records.values()
        )

    def display_total_records(self):
        return len(self.vaccination_records)


def choose_status():
    print("\nSelect Vaccination Status")
    print("1. Pending\n2. Vaccinated\n3. Completed")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        return "Pending"
    if choice == "2":
        return "Vaccinated"
    if choice == "3":
        return "Completed"
    raise ValueError("Please select status 1, 2 or 3.")


def read_integer(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError as exc:
        raise ValueError("Enter a whole number.") from exc


def main():
    system = VaccinationSystem()
    while True:
        print("\n" + "=" * 48)
        print("       VACCINATION RECORD & TRACKING SYSTEM")
        print("=" * 48)
        print("1. Register Vaccination")
        print("2. Search Vaccination Record")
        print("3. Update Vaccination Status")
        print("4. Display All Records")
        print("5. Display Total Records")
        print("6. Exit")
        print("=" * 48)
        try:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                print("\nREGISTER VACCINATION RECORD")
                patient_id = input("Enter Patient ID: ")
                name = input("Enter Patient Name: ")
                age = read_integer("Enter Age: ")
                phone = input("Enter Phone Number (demo only): ")
                vaccine_name = input("Enter Vaccine Name: ")
                dose = read_integer("Enter Dose Number: ")
                date = input("Enter Vaccination Date (e.g., 10/10/2026): ")
                status = choose_status()
                record = system.register_vaccination(
                    patient_id, name, age, phone, vaccine_name,
                    dose, date, status
                )
                print("\nVaccination record created successfully.")
                print(record.display_record())
            elif choice == "2":
                record = system.search_record(input("Enter Record ID: "))
                print("\n" + (record.display_record() if record else "Vaccination record not found."))
            elif choice == "3":
                record_id = input("Enter Record ID: ")
                record = system.search_record(record_id)
                if record is None:
                    print("Vaccination record not found.")
                else:
                    print("Current Status: " + record.status)
                    status = choose_status()
                    system.update_vaccination_status(record_id, status)
                    print("Vaccination status updated successfully.")
                    print("New Status: " + status)
            elif choice == "4":
                print("\nALL VACCINATION RECORDS")
                print(system.display_all_records())
            elif choice == "5":
                print("Total vaccination records: " + str(system.display_total_records()))
            elif choice == "6":
                print("Goodbye!")
                return
            else:
                print("Invalid menu choice. Please select 1–6.")
        except ValueError as exc:
            print("Input error: " + str(exc))
        except (EOFError, KeyboardInterrupt):
            print("\nProgram closed.")
            return


if __name__ == "__main__":
    main()
