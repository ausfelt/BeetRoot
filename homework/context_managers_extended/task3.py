import os

import pytest
from task1 import MyOpen


@pytest.fixture
def replace_file_obj():
    return "pytest_input.txt"


@pytest.fixture
def data_to_check(replace_file_obj):
    with MyOpen(replace_file_obj, "w") as io_file:
        io_file.write("Some text to test...")

    with MyOpen(replace_file_obj, "r") as io_file:
        data = io_file.read(9)
        yield data
    os.remove("pytest_input.txt")


def test_data(data_to_check):
    assert data_to_check == "Some text"