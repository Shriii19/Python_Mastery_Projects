# Project 05: CSV Data Analyzer

**Status: 🟡 In Development**

## Description

A local console application that loads employee data from CSV, analyzes it with Pandas, identifies data-quality problems, and writes readable text reports. It uses no web server, database, API, or cloud service.

## Goals and Features

- Inspect complete data, head/tail records, shape, columns, types, and dataset info.
- Filter by department, salary, and age; sort by name, age, salary, or department.
- Calculate employee count, salary totals and ranges, and age averages and ranges.
- Group employees by department with counts and salary summaries.
- Detect missing values and duplicate rows.
- Create a cleaned in-memory DataFrame without changing the source CSV.
- Generate summary, department, and data-quality reports in `reports/`.
- Handle missing files, malformed CSV files, invalid columns, and invalid menu input.

## Dataset and Workflow

`data/employees.csv` contains employee `id`, `name`, `department`, `age`, and `salary` columns. It has 10 unique employee records plus one duplicate row, and one missing salary to make quality checks meaningful.

```text
CSV -> EmployeeAnalyzer -> inspect/filter/sort/analyze/clean -> ReportGenerator -> reports/
```

## Project Structure

```text
05-CSV-Data-Analyzer/
|-- data/employees.csv
|-- reports/
|-- tests/test_analyzer.py
|-- analyzer.py       # Data loading and analysis
|-- report.py         # Text report generation
|-- config.py         # Project paths
|-- logger.py         # Application logging
|-- main.py           # Console menu
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Technologies and Installation

- Python 3
- Pandas
- CSV and the Python standard library

Create a virtual environment if desired, activate it, and install the only external dependency:

```bash
pip install -r requirements.txt
```

## How to Run

From this directory:

```bash
python main.py
```

Choose `5` for statistics, `7` for quality checks, `8` for an in-memory cleaned view, or `9` to generate all reports.

Run the tests with the standard library:

```bash
python -m unittest discover -s tests -v
```

## Concepts Practiced

**Python:** modules, classes, type hints, pathlib, exceptions, logging, and unittest.

**Pandas:** DataFrames, `read_csv`, selection, boolean filtering, sorting, aggregation, `groupby`, missing-value detection, duplicate detection, and type conversion.

**Software engineering:** separation of concerns, configuration, non-destructive cleaning, validation, reporting, and automated tests.

## Development Roadmap

1. Add optional CSV export for cleaned data.
2. Add configurable report formats such as Markdown or CSV.
3. Add more reusable command-line arguments while preserving the interactive menu.
4. Expand validation for numeric ranges and duplicate IDs.

## Learning Outcomes

You will be able to build a small, maintainable Pandas application; reason about data quality; produce repeatable reports; and test analysis behavior independently from user interaction.

## Future Improvements and Project Status

Possible extensions include charts, configurable input files, richer validation, and additional report formats. The current implementation is complete for the roadmap requirements and remains **🟡 In Development** as a learning project.