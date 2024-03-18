import pandas as pd


def get_input_from_console():
    """
    Gets user's input from the console.

    Returns:
        str: user's input from the console.
    """
    user_input = input("Enter your data: ")
    return user_input


def read_data_from_file(path):
    """
    Reads data from given file.

    Args:
        path (str): path to file to read data from.

    Returns:
        str: data from the file.

    Raises:
        FileNotFoundError: if file does not exist.
    """
    with open(path, "r") as f:
        text = f.read()
    return text


def read_data_from_csv(path):
    """
    Reads data from csv file using Pandas library.

    Args:
        path (str): path to file to read data from.

    Returns:
        pd.DataFrame: data from the csv file.

    Raises:
        FileNotFoundError: if csv file does not exist.
    """
    data = pd.read_csv(path)
    return data
