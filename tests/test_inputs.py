import pytest
from calculator.inputs import read_csv_values

"""
these tests were made as part 5 of the assignment to test the CSV integration
"""

def test_read_csv_default_column(tmp_path):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("value\n10\n20\n30\n")
    assert read_csv_values(csv_file) == [10, 20, 30]

def test_read_csv_custom_header(tmp_path):
    """tests reading values from a custom header column"""
    csv_file = tmp_path / "custom.csv"
    csv_file.write_text("observations\n100\n200\n300\n")
    assert read_csv_values(csv_file, column="observations") == [100, 200, 300]

def test_read_csv_missing_header(tmp_path):
    """test faliure when the specified header column does not exist"""
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("value\n10\n20\n30\n")
    with pytest.raises(ValueError):
        assert read_csv_values(csv_file, column="nonexistent_header")

