from pathlib import Path
import csv
import pytest

DATA_DIR = Path(__file__).parent / "data"
CSV_FILE = DATA_DIR / "calculator_cases.csv"


def load_csv_rows():
    with CSV_FILE.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


@pytest.fixture(scope="session")
def calculator_csv_rows():
    return load_csv_rows()


def pytest_generate_tests(metafunc):
    """Parametrize any test that asks for ``csv_case``: one test per CSV row.

    Each row is tagged with its author (ahmed / abdullah) so ``-m ahmed`` and
    ``-m abdullah`` also select the matching CSV rows.
    """
    if "csv_case" in metafunc.fixturenames:
        params = [
            pytest.param(
                row,
                id=row["description"].replace(" ", "_"),
                marks=getattr(pytest.mark, row["author"]),
            )
            for row in load_csv_rows()
        ]
        metafunc.parametrize("csv_case", params)
