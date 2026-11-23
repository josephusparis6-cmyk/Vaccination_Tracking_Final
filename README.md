# Vaccination Record and Tracking System

**Module:** PROG211 — Object-Oriented Programming 1  
**Assignment:** Real-World Solutions under Digital Public Goods (DPG) Standards  
**Institution:** Limkokwing University of Creative Technology, Sierra Leone  
**Student:** Josephus P Paris
**Project type:** Python console application 

## Project overview

The Vaccination Record and Tracking System is a console-based Python application demonstrating introductory Object-Oriented Programming (OOP). It allows a user to register a vaccination record, look it up using a unique record ID, update its vaccination status, display all records and count records stored during the current program session.

The program is an **educational example**, not an operational healthcare records system. Use **fictional data only**.

## Problem and proposed solution

Paper-based vaccination records can be difficult to organize, retrieve and update. This project shows how Python classes, objects, methods and a dictionary can structure a simple record-management workflow. Records are held only in memory and disappear when the application closes.

## Features

- Register a patient and vaccination record.
- Assign unique IDs such as `VAC001`, `VAC002`, and `VAC003`.
- Search for a vaccination record by ID.
- Update vaccination status: `Pending`, `Vaccinated`, or `Completed`.
- Display all records and the total number stored in the current session.
- Handle invalid menu selections and selected invalid inputs.

## Requirements

- Python **3.9 or later**.
- No third-party packages, database, or internet connection.

## How to run

Open a terminal in the project folder and run:

```bash
python3 vaccination.py
```

On Windows, use `python vaccination.py` if `python3` is not recognized.

The menu displays:

```text
================================================
       VACCINATION RECORD & TRACKING SYSTEM
================================================
1. Register Vaccination
2. Search Vaccination Record
3. Update Vaccination Status
4. Display All Records
5. Display Total Records
6. Exit
================================================
```

## Sample input and output
Example registration inputs (enter these after choosing menu option `1`):

```text
Enter Patient ID: DEMO001
Enter Patient Name: Demo Patient
Enter Age: 24
Enter Phone Number (demo only): 000000000
Enter Vaccine Name: Demo Vaccine
Enter Dose Number: 1
Enter Vaccination Date (e.g., 10/10/2026): 10/10/2026

Select Vaccination Status
1. Pending
2. Vaccinated
3. Completed
Enter choice: 2
```

Expected registration output:

```text
Vaccination record created successfully.
Record ID: VAC001
Patient ID: DEMO001
Patient Name: Demo Patient
Age: 24
Phone: 000000000
Vaccine Name: Demo Vaccine
Dose Number: 1
Vaccination Date: 10/10/2026
Status: Vaccinated
```

Further example actions:

| Menu choice | Example input | Expected result |
|---|---|---|
| `2` Search | `VAC001` | Displays the saved vaccination details |
| `3` Update | `VAC001`, status `3` | Updates status to `Completed` |
| `4` Display all | None | Displays all stored records |
| `5` Total records | None | Displays `Total vaccination records: 1` |
| `2` Search missing | `VAC999` | Displays `Vaccination record not found.` |
| `6` Exit | None | Displays `Goodbye!` |

These are illustrative inputs and expected outputs; take fresh screenshots from a real run for your hard-copy report.

## Object-Oriented Programming concepts

### Classes and object interaction

- `Patient`: stores a patient ID, name, age, and demonstration phone value. Its instance method `display_details()` returns formatted information.
- `VaccinationRecord`: stores vaccine information and **contains a `Patient` object**. It has instance methods `display_record()` and `update_status()`, class method `get_total_records()`, and static method `validate_status()`.
- `VaccinationSystem`: manages `VaccinationRecord` objects, registration, searches, updates, display, and counting.

The interaction is: `Patient` object → `VaccinationRecord` object → `VaccinationSystem` dictionary.

### Exactly one collection for stored records

The application stores multiple record objects in one Python dictionary:

```python
self.vaccination_records = {}
```

Keys are record IDs and values are `VaccinationRecord` objects. The program uses standard control flow and strings, but no other collection for record storage.

### Methods

- **Instance:** `display_details()`, `display_record()`, `update_status()`, `register_vaccination()`, `search_record()`.
- **Class:** `VaccinationRecord.get_total_records()` reports the number of record objects created in the current Python process.
- **Static:** `VaccinationRecord.validate_status()` checks whether a status value is supported.

## Digital Public Goods (DPG) principles

1. **Open source:** The code can be studied and reused under the included [MIT License](LICENSE). Publishing the repository makes its source visible.
2. **Inclusive and accessible:** A numbered text-based menu works without a graphical interface or an internet connection.
3. **Privacy-respecting:** The program retains entries in memory for the session only. It sends no information to external services. Do **not** use real patient information.
4. **Modular and reusable:** Separate classes make the educational application easier to understand and extend.

These design choices align with DPG principles; they do **not** establish formal Digital Public Goods Alliance certification.

## Project structure

```text
Vaccination_Tracking_Final/
├── vaccination.py    # Python console application
├── README.md         # Overview, instructions, OOP and DPG explanation, sample I/O
└── LICENSE           # MIT open-source license
```

## Limitations

- Data are not saved after the program exits.
- There is no login or authentication and no database.
- Date input is text; this is not a clinical validation system.
- No real vaccination status, identity, or medical record is verified.

