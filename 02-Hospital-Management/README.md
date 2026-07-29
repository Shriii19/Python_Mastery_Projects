# Hospital Management

A simple command-line Hospital Management System built with Python.

## Features

- Add and view patients
- Add and view doctors
- Book and view appointments
- Persist data in JSON files
- Write logs to `logs/hospital.log`

## Project Structure

- `data/` stores JSON data files
- `logs/` stores runtime logs
- `tests/` stores test files

## Run

```bash
python main.py
```

## Notes

- IDs for patients, doctors, and appointments must be unique.
- Appointment booking requires existing patient and doctor IDs.
