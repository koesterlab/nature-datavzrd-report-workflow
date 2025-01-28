import os
import csv
import re

def process_csv_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    if not csv_files:
        print(f"No CSV files found in '{directory}'.")
        return

    for file in csv_files:
        file_path = os.path.join(directory, file)
        updated_rows = []

        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                updated_row = []
                for cell in row:
                    # Check if the cell has 3 or more dots
                    if cell.count('.') >= 3:
                        cleaned_cell = cell.replace('.', '')
                        if re.match(r'^-?\d+$', cleaned_cell):
                            updated_row.append(cleaned_cell)
                        else:
                            updated_row.append(cell)
                    else:
                        updated_row.append(cell)
                updated_rows.append(updated_row)

        output_file = os.path.join(directory, f"processed_{file}")
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(updated_rows)

        print(f"Processed file saved as '{output_file}'.")

directory_name = 'bioinformatics'
process_csv_files(directory_name)