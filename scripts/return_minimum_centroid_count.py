# This script returns the minimum number of centroids in a dataset of centroid csvs

import csv
import os

file_path = "images_data/mag5_1608_no_adverserial_gray/centroids"

min_row_count = 10000
min_file = None

for file in os.listdir(file_path):
    with open(file_path + "/" + file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        row_count = len(list(csv_reader))
        # print(row_count)
        if row_count < min_row_count:
            min_row_count = row_count
            min_file = file

print("Filename: ", min_file)
print("Minimum number of stars: ", min_row_count)