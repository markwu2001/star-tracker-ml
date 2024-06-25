import feature_extraction as bin
import csv

# Open CSV centroids and write to centroid array

filepath = "images_data/mag5_adverserial_centroids/122001_centroids_adverserial_case_0_false_stars_0.csv"
centroids = []

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row if there is one
    for row in csvreader:
        centroids.append([float(row[0]),float(row[1])])

print("Input Centroids:", centroids , '\n \n')

bins = bin.feature_extraction_binning(centroids, 752, 480, 400, 10)
print("Bins:", bins)