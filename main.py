from app.io.input import get_input_from_console, read_data_from_file, read_data_from_csv
from app.io.output import output_to_console, write_text_to_file, write_text_to_csv


def main():
    input_from_console = get_input_from_console()
    output_to_console(input_from_console)
    write_text_to_file(input_from_console, "./data/output_data")

    data_from_file = read_data_from_file("./data/input_data")
    output_to_console(data_from_file)
    write_text_to_file(data_from_file, "./data/output_data")

    data_from_csv = read_data_from_csv("./data/color_srgb.csv")
    output_to_console(data_from_csv)
    write_text_to_csv(data_from_csv, "./data/output_data")


if __name__ == '__main__':
    main()
