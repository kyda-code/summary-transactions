import csv


def read_file(file_name):
    records = []

    # Validate is file_name is null or empty
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                records.append(row)
                line_count += 1

    return records
