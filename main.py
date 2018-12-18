import csv
import matplotlib
from matplotlib import pyplot as plt


filename = 'urban-heat-management-actions-neighborhood-data-1.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    new_trees = []
    neighborhoods = []
    for row in reader:
        neighborhoods.append(str(row[0]))
        new_trees.append(int(row[3]))

    print(new_trees)
    print(neighborhoods)

    objects = neighborhoods
    plt.bar((len(objects)), new_trees, align='center', alpha=0.5)
    plt.xticks(objects)
    plt.title("New trees planted", fontsize=24)
    plt.xlabel(objects, fontsize=16)
    plt.ylabel("Number of trees", fontsize=16)
    plt.show()
