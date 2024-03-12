from django.test import TestCase
import pytest
import pandas as pd
from ..tasks import *



@pytest.mark.parametrize("csv_path", [
    "D:/ML/concrete_data.csv",
    "D:/ML/student_records.csv",
    "D:/ML/student_records.csv"
])
def test_read_csv_successful(csv_path):
    result = pd.read_csv(csv_path)
    assert isinstance(result, pd.DataFrame), f"Expected DataFrame, but got {type(result)}"

def test_read_csv_file_not_found():
    # Specify a non-existent file path
    non_existent_path = "/path/to/nonexistent/file.csv"

    # Call the function and check the result
    result = read_csv(non_existent_path)
    assert result == "error reading file: File not found"

def test_read_csv_general_exception():
    # Create a temporary directory
    dir_path = "D:\\Django\\myworld\\temp2\\app1\\tests\\" + "test_directory"
    

    # Call the function with a directory path (which will raise a general exception)
    result = read_csv(dir_path)
    assert result.startswith("error reading file:")

