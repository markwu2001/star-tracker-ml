import sys
import os
# Add the path to the algorithms directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'algorithms'))

# Now you can import the feature_extraction module
import feature_extraction as bin
import csv

# Open folder of CSV centroids and write bins to a single CSV file with file structure
# "HIP", bin0 , ... , binX

centroid_filepath = "images_data/mag5_adverserial_centroids/"

bin_filepath = "images_data/mag5_adverserial_bins/"
bin_filename = "mag5_adverserial_bins.csv"

if not os.path.exists(bin_filepath):
    os.makedirs(bin_filepath)

with open(bin_filepath + bin_filename, 'w' , newline='') as csvfile1:
    csvwriter = csv.writer(csvfile1)
    csvwriter.writerow(["HIP", "bin0", "bin1", "bin2", "bin3", "bin4", "bin5", "bin6", "bin7", "bin8", "bin9"])

    for file in os.listdir(centroid_filepath):
        centroids = []
        with open(centroid_filepath + file, 'r') as csvfile2:
            csvreader = csv.reader(csvfile2)
            next(csvreader)  # Skip the header row if there is one
            for row in csvreader:
                centroids.append([float(row[0]),float(row[1])])
        
        bin_count = 10
        bin_max_radius = 400
        bins = bin.feature_extraction_binning(centroids, 752, 480, bin_max_radius, bin_count)
        csvwriter.writerow([file.split("_centroids")[0]] + bins)

csvfile1.close()
csvfile2.close()
print("Completed!")