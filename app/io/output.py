import pandas as pd


def output_to_console(data):
    """
    Writes given text to console.

    Args:
        data (Any): text to write to console.
    """
    print(data)


def write_text_to_file(text, path):
    """
    Writes given text to file of given path.

    Args:
         text (str): text to write to file.
         path (str): path to file to write text to.

    Raises:
        FileNotFoundError: if file does not exist.
    """
    with open(path, 'a') as f:
        f.write(text)


def write_text_to_csv(data_frame, path):
    """
    Writes given data frame to file of given path

    Args:
        data_frame (pd.DataFrame): data frame to write to file.
        path (str): path to file to write data frame to.

    Raises:
        FileNotFoundError: if file does not exist.
    """
    data_frame.to_csv(path, mode='a')
