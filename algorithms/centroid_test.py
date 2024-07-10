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
        if file.endswith(".png"):
            img = Image.open(file_path + file)
            # print(file_path + file)
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

# image = Image.open("images_data/test_images/noisy_image.jpg") 
image = Image.open("images_data/dslr_night_images_gray/focused_star_dsc0014_752x502_gray.png") 
# image = Image.open("images_data/dslr_night_images/distortion_corrected/focused_star_dsc0014_752x502_gray_hip75458.png_corrected_image.png") 
# image = Image.open("images_data/mag5_1608_no_adverserial_gray/11345001.png") # Determined as the star with the lowest amount of centroids around it (106 other stars)
sources = ct.centroids_from_img(image)
ct.overlay_centroids(image, sources)

# Run code to generate centroid sources
# centroid_sources_to_dataset("images_data/mag5_1608_no_adverserial_gray/") # use this line to create a csv dataset.