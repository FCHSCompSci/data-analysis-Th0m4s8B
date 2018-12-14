import csv
import matplotlib

filename = 'urban-heat-management-actions-neighborhood-data-1.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    new_trees = []
    for row in reader:
        new_trees.append(row[3])

    print(new_trees)