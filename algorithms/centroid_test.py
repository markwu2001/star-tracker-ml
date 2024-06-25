# 1. Use center of mass algorithm
# 2. Visual test function to overlay centroids on image

import centroid as ct
from PIL import Image
import os
import csv

def centroid_sources_to_dataset(file_path):
    if not os.path.exists(file_path + "/centroids"):
        os.makedirs(file_path + "/centroids")

    # Open folder and read all images
    for file in os.listdir(file_path):
        img = Image.open(file_path + file)
        # Calculate centroids for each image
        sources = ct.centroids_from_img(img)

        # Initialize empty csv file
        csv_file = open(file_path + "/centroids/" + file.strip('.png') + '_centroids_no_adverserial.csv', 'w', newline='')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['x_centroid', 'y_centroid'])
        # Append centroids to a dataset
        for source in sources:
            csv_writer.writerow([source['xcentroid'], source['ycentroid']])
        # Save dataset to a file
        csv_file.close()
    return 

# Run code for image demo

# image = Image.open("images_data/mag5_1608_no_adverserial_gray/122001.png") # first star in catalogue
# image = Image.open("images_data/mag5_1608_no_adverserial_gray/11345001.png") # Determined as the star with the lowest amount of centroids around it (106 other stars)
# sources = ct.centroids_from_img(image)
# ct.overlay_centroids(image, sources)

# Run code to generate centroid sources
centroid_sources_to_dataset("images_data/mag5_1608_no_adverserial_gray/") # use this line to create a csv dataset.