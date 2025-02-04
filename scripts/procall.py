import os
import pandas as pd


def is_valid_float(value):
    """
    Check if a string can be safely converted to a float.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def process_csv_files_in_directory(input_dir):
    """
    Process all CSV files in the given directory:
    - Correct float formatting from '1,76' to '1.76', if valid.
    - Rename files from 'Suppl. Tab. 13-Tabelle 1.csv' to 'Suppl. Tab. 13.csv'.
    """
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".csv"):
            file_path = os.path.join(input_dir, file_name)

            try:
                # Read the CSV with ";" delimiter
                df = pd.read_csv(file_path, delimiter=";", dtype=str)

                # Replace valid float strings with corrected format
                df = df.applymap(
                    lambda x: x.replace(",", ".") if isinstance(x, str) and "," in x and is_valid_float(
                        x.replace(",", ".")) else x
                )

                # Rename the file
                new_file_name = rename_file(file_name)
                new_file_path = os.path.join(input_dir, new_file_name)

                # Save the processed DataFrame
                df.to_csv(new_file_path, index=False, sep=";")
                print(f"Processed and saved: {new_file_name}")

            except Exception as e:
                print(f"Error processing file {file_name}: {e}")


def rename_file(file_name):
    """
    Rename files like 'Suppl. Tab. 13-Tabelle 1.csv' to 'Suppl. Tab. 13.csv'.
    """
    if "-Tabelle" in file_name:
        return file_name.split("-Tabelle")[0] + ".csv"
    return file_name


def main():
    """
    Main function to define directory and process files.
    """
    input_dir = "../anthropology"  # Replace with your actual directory
    if os.path.isdir(input_dir):
        process_csv_files_in_directory(input_dir)
    else:
        print(f"Directory {input_dir} does not exist.")


if __name__ == "__main__":
    main()
