from app.io.input import read_data_from_file, read_data_from_csv
import pytest
import pandas as pd

PATH_TO_TXT_FILE = "tests/data/test_data"
PATH_TO_CSV_FILE = "tests/data/test_csv.csv"


def test_read_data_from_file():
    actual = read_data_from_file(PATH_TO_TXT_FILE)
    expected = "Most individuals don't think about numbers"
    assert actual == expected


def test_read_data_from_file_raise_exception():
    with pytest.raises(FileNotFoundError):
        read_data_from_file("non_existing_file")


def test_read_data_from_file_with_csv():
    actual = read_data_from_file(PATH_TO_CSV_FILE)
    expected = "Name,HEX,RGB\nWhite,#FFFFFF,\"rgb(100,100,100)\"\nSilver,#C0C0C0,\"rgb(75,75,75)\""
    assert actual == expected


def test_read_data_from_csv():
    actual = read_data_from_csv(PATH_TO_CSV_FILE)
    expected = pd.DataFrame([["White", "#FFFFFF", "rgb(100,100,100)"],
                             ["Silver", "#C0C0C0", "rgb(75,75,75)"]],
                            columns=["Name", "HEX", "RGB"])
    pd.testing.assert_frame_equal(expected, actual)


def test_read_data_from_csv_file_raise_exception():
    with pytest.raises(FileNotFoundError):
        read_data_from_csv("non_existing_file")


def test_read_data_from_csv_with_text_file():
    actual = read_data_from_csv(PATH_TO_TXT_FILE)
    expected = pd.DataFrame(columns=["Most individuals don't think about numbers"])
    pd.testing.assert_frame_equal(expected, actual)
