# Calculator - Unit Test Automation (Assignment 3)

Open-source (MIT) Python calculator written by Ahmed Sufian and Abdullah Amir,
with an automated pytest suite. FAST NUCES, Software Quality Engineering.

Repository: https://github.com/AbdullahA35/Basic-Python-Calculator.git

## Project layout

| Path | Purpose |
|---|---|
| `calculator/` | `addition.py`, `subtraction.py`, `multiplication.py`, `division.py` (one function each) and `calculator.py` (`Calculator` class with history) |
| `tests/unit/ahmed/`, `tests/unit/abdullah/` | Each person's tests: function tests, `Calculator` method tests, class-level tests |
| `tests/workflow/` | Ordered, stateful session tests |
| `tests/test_smoke.py` | Smoke tests, run first |
| `tests/test_csv_data.py`, `tests/data/calculator_cases.csv` | CSV-driven tests (one test per row) |
| `tests/test_excel_cases.py`, `test_cases.xlsx` | Excel test cases (Author column), executed by pytest |
| `scripts/update_excel_results.py` | Runs the Excel cases and writes Actual Result / Status back |
| `docs/test_design_notes.md` | ECP and BVA notes |
| `docs/video_demo_setup.mp4` | Environment setup video |

## Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest --version
```

## Running tests

| Goal | Command (prefix with `.\.venv\Scripts\python.exe -m`) |
|---|---|
| Everything, in the configured order | `pytest -v` |
| In parallel | `pytest -n auto -v` |
| One suite | `pytest -m addition` (also `subtraction`, `multiplication`, `division`, `method`, `class_level`, `workflow`, `csvdata`, `excel`, `smoke`) |
| One person's tests | `pytest -m ahmed` or `pytest -m abdullah` |
| Show the execution order | `pytest --collect-only -q` |
| Coverage | `pytest --cov=calculator --cov-branch` |
| Refresh Excel results | `python scripts/update_excel_results.py` |

## Execution order (pytest-order)

Groups carry a module-level `pytest.mark.order(N)`; the workflow steps carry their own
indexes (801-806).

| Order | Group |
|---|---|
| 100 | smoke |
| 200 / 300 / 400 / 500 | addition / subtraction / multiplication / division function tests |
| 600 | `Calculator` method tests |
| 700 | `Calculator` class-level tests |
| 801-806 | workflow session (step 1 to 6) |
| 900 | CSV and Excel data-driven tests |

## Parallel execution (pytest-xdist)

`pytest.ini` sets `--dist loadfile`, so with `-n` each test file stays on one worker and the
order inside a file is kept. pytest-order guarantees order per worker only, so use a serial
run when the full global order matters. The suite is small, so `-n auto` is mostly a demo:
worker start-up can cost more than it saves.

## Test counts

150 tests: 71 by Ahmed, 64 by Abdullah, 15 shared (smoke, workflow, CSV/Excel row-count checks
and the four CSV examples).
