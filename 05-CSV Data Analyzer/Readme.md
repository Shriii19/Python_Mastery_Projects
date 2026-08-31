# CSV Data Analyzer

**Status:** In Development

## Project Purpose

CSV Data Analyzer is a beginner-friendly local Python project for exploring employee data stored in a CSV file. It will demonstrate how to load, inspect, filter, sort, summarize, clean, and report on small datasets.

The project focuses on learning data analysis concepts with a simple dataset, not processing large volumes of data or connecting to external services.

## What the Application Will Do

The completed application will load an employee CSV file, analyze its contents, allow filtering and sorting, calculate useful statistics, and generate reports.

## Example Dataset

The included `data/employees.csv` file contains a small employee dataset with these columns:

- `id`
- `name`
- `department`
- `age`
- `salary`

The initial data is complete and has no duplicate rows. Missing and duplicate values will be introduced later while learning data cleaning.

## Planned Features

- Load CSV data
- View records and dataset information
- Search and filter records
- Sort records
- Calculate statistics
- Group records by department
- Detect missing values
- Detect duplicate records
- Clean data
- Generate reports

These features are planned and are not implemented yet.

## Basic Workflow

```text
CSV file
    -> Load data
    -> Analyze data
    -> Filter or sort
    -> Calculate statistics
    -> Generate reports
```

## Project Structure

```text
05-CSV-Data-Analyzer/
|
|-- data/
|   `-- employees.csv
|
|-- reports/
|
|-- tests/
|
|-- analyzer.py
|-- report.py
|-- config.py
|-- logger.py
|-- main.py
|
|-- README.md
|-- requirements.txt
`-- .gitignore
```

## Technologies

- Python
- Pandas
- CSV files
- Python Standard Library

## Installation

1. Create and activate a virtual environment.
2. Install the project dependency:

```bash
pip install -r requirements.txt
```

## How to Run

The application entry point will be `main.py`. A runnable application will be added in a later development step.

## Concepts You Will Practice

### Python Concepts

- Modules and imports
- Functions and classes
- File paths
- Exception handling
- Logging
- Testing

### Pandas Concepts

- Reading CSV files
- Inspecting DataFrames
- Filtering and sorting data
- Descriptive statistics
- Grouping data
- Missing-value and duplicate detection
- Exporting reports

### Software Engineering Concepts

- Organizing a project into focused modules
- Separating analysis, reporting, configuration, and user-interface responsibilities
- Keeping sample data separate from source code
- Writing tests as features are implemented

## Development Roadmap

1. Set up the project structure and sample data.
2. Load and display CSV data.
3. Add filtering, sorting, and statistics.
4. Add data-quality checks and cleaning.
5. Add report generation and tests.

## Learning Outcomes

After completing this project, you will be able to use Pandas to analyze a small CSV dataset, organize a Python data-analysis project, and create basic data reports.

## Project Status

In Development. The repository currently contains only the project setup and sample dataset; no application logic has been implemented.