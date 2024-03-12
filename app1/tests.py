from django.test import TestCase
import pytest
import pandas as pd
from .tasks import *
# Create your tests here.

@pytest.mark.parametrize("csv_path", [
    "D:\ML\concrete_data.csv",  
    "D:\ML\student_records.csv"
])
def test_read_csv_successful(csv_path):
    # Assuming your `read_csv_file` function reads the CSV file
    result = pd.read_csv(csv_path)
    assert isinstance(result, pd.DataFrame), f"Expected DataFrame, but got {type(result)}"
