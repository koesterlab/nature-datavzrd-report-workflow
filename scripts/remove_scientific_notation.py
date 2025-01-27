import os
import csv
from decimal import Decimal

def is_scientific_notation(value):
    try:
        float(value)
        if 'e' in value.lower():
            return True
    except ValueError:
        return False
    return False

def process_csv_file(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=';')
        rows = list(reader)

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                if is_scientific_notation(value):
                    try:
                        decimal_value = Decimal(value)  # Use Decimal to preserve precision
                        # Format to avoid scientific notation when saving
                        rows[row_idx][col_idx] = f"{decimal_value:.50f}".rstrip('0').rstrip('.')  # Adjust precision
                    except ValueError:
                        pass

    with open(file_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerows(rows)
    print(f"Processed and saved: {file_path}")

def process_all_csv_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            process_csv_file(file_path)

directory_path = 'bioinformatics'
process_all_csv_files_in_directory(directory_path)
