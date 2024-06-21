import csv

def open_csv_file(filename):
    """ Open and read a CSV file, returning the CSV reader object. """
    try:
        file = open(filename, newline='')
        return csv.reader(file)
    except FileNotFoundError:
        print("File not found.")
        return None

def extract_columns(csv_reader, *column_names):
    """ Extract specific columns from the CSV file based on column names. """
    if csv_reader is None:
        return []
    columns = []
    header = next(csv_reader)
    indices = [header.index(name) for name in column_names]
    for row in csv_reader:
        selected_columns = [row[index] for index in indices]
        columns.append(selected_columns)
    return columns

# Usage
filename = 'catalogue/hippacros-mag-5.csv'
csv_reader = open_csv_file(filename)
columns = extract_columns(csv_reader, 'HIP', 'RAdeg', 'DEdeg')
print(columns)
print("Number of entities: ", len(columns))

# Now take columns and write to a new file with stellarium syntax