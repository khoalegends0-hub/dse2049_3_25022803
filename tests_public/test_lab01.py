from pathlib import Path

import pytest
from testbook import testbook


NOTEBOOK_PATH = Path(__file__).parents[1] / "lab01.ipynb"


@pytest.fixture(scope="module")
def notebook():
    """Execute the notebook once and share its kernel across public tests."""
    with testbook(NOTEBOOK_PATH, execute=True) as tb:
        yield tb


@pytest.mark.parametrize(
    ("values", "expected_mean", "expected_std"),
    [
        ([1, 2, 3], 2.0, 0.816496580927726),
        ([5, 5, 5], 5.0, 0.0),
        ([-2, 0, 2], 0.0, 1.632993161855452),
    ],
)
def test_describe_values(notebook, values, expected_mean, expected_std):
    describe_values = notebook.ref("describe_values")
    result = describe_values(values)

    assert set(result) == {"mean", "std"}
    assert result["mean"] == pytest.approx(expected_mean)
    assert result["std"] == pytest.approx(expected_std)


@pytest.mark.parametrize(
    ("records", "expected"),
    [
        (
            [
                {"product": "book", "revenue": 10},
                {"product": "pen", "revenue": 4},
                {"product": "book", "revenue": 7},
            ],
            {"book": 17.0, "pen": 4.0},
        ),
        ([], {}),
    ],
)
def test_revenue_by_product(notebook, records, expected):
    revenue_by_product = notebook.ref("revenue_by_product")
    assert revenue_by_product(records) == expected
