# Calculator Unit Test Automation

A Python calculator and automated test suite for Assignment 3 in Software Quality Engineering at FAST NUCES. The project demonstrates unit, class, workflow, and data-driven testing with pytest.

Contributors: Ahmed Sufian and Abdullah Amir.

Repository: https://github.com/AbdullahA35/Basic-Python-Calculator
License: MIT

## Project layout

| Path | Purpose |
|---|---|
| `calculator/` | Calculator package: four arithmetic functions and the `Calculator` class with operation history |
| `tests/unit/ahmed/` | Ahmed's unit and class tests, focused mainly on equivalence classes |
| `tests/unit/abdullah/` | Abdullah's unit and class tests, focused mainly on boundaries and invalid input |
| `tests/workflow/` | Ordered tests for a multi-step calculator session |
| `tests/test_smoke.py` | Fast checks that the package and class work |
| `tests/test_csv_data.py` and `tests/data/calculator_cases.csv` | One pytest case per CSV row; rows include their author's name |
| `tests/test_excel_cases.py` and `test_cases.xlsx` | Excel cases executed by pytest; each row includes its author |
| `docs/test_design_notes.md` | ECP and BVA test design notes |
| `docs/Assignment3_Documentation.docx` | Assignment report and contribution record |
| `docs/video_demo_setup.mp4` | Windows environment setup demonstration |
| `scripts/update_excel_results.py` | Runs workbook cases and updates Actual Result and Status |
| `pytest.ini` and `requirements.txt` | Test discovery, markers, ordering options, and dependencies |

The four arithmetic files at the repository root are retained from the original calculator project. The assignment tests use the package under `calculator/`.

## Setup

Python 3 and pip are required.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest --version
```

### macOS or Linux

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest --version
```

Activate the virtual environment in each new terminal before running the commands below.

## Run the tests

Run the full suite serially:

```sh
python -m pytest -v
```

Run it with four workers:

```sh
python -m pytest -n 4 -v
```

Run a suite or an individual's tests by marker:

```sh
python -m pytest -m addition -v
python -m pytest -m "ahmed" -v
python -m pytest -m "abdullah" -v
```

Other registered markers are `smoke`, `unit`, `subtraction`, `multiplication`, `division`, `method`, `class_level`, `workflow`, `csvdata`, and `excel`.

Show collected tests and their order:

```sh
python -m pytest --collect-only -q
```

Measure line and branch coverage:

```sh
python -m pytest --cov=calculator --cov-branch
```

Update the workbook's Actual Result and Status columns after running its cases:

```sh
python scripts/update_excel_results.py
```

Review the workbook changes before committing them. The script writes its results back to `test_cases.xlsx`.

## Test order

| Order | Test group |
|---|---|
| 100 | Smoke tests |
| 200–500 | Addition, subtraction, multiplication, and division function tests |
| 600 | `Calculator` method tests |
| 700 | `Calculator` class tests |
| 801–806 | Ordered workflow steps |
| 900 | CSV and Excel data-driven tests |

`pytest-order` applies order within a worker. With `pytest-xdist`, `--dist loadfile` keeps each test file on one worker, but it does not guarantee one global order across workers. Use a serial run when the overall order matters.

## Test counts

The suite contains 150 tests: 71 attributed to Ahmed, 64 to Abdullah, and 15 shared smoke, workflow, and data-check tests. The current repository passed all 150 tests in both serial and four-worker runs.
