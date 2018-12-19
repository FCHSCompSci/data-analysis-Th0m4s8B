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
    del new_trees[-1]
    del neighborhoods[-1]

    print(new_trees)
    print(neighborhoods)

    x = []
    i = 0
    while i <= 131:
        x.append(i)
        i += 1

    plt.bar(neighborhoods, new_trees, align='center', alpha=0.5, color='green')
    plt.xticks(x, neighborhoods, rotation=270, fontsize=5)
    plt.title("New trees planted", fontsize=24)
    plt.xlabel('Locations', fontsize=12)
    plt.ylabel("Number of trees", fontsize=12)
    plt.show()
