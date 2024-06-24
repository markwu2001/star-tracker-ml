#1. TODO: Post Centroiding False Star Error (0-5 count random)
#2. TODO: Post Centroiding Gaussian Positional Error applied to all stars
#3. TODO: Post Centoiding Gaussian Positional Error applied to single stars

import csv
import os
import random
import shutil

def apply_adverserial_false_stars(file_path, sensor_x, sensor_y):
    adverserial_cases = 10 # how many adverserial datapoints are created per original data point. Recommended 360 
    adverserial_stars = 5 # max false stars to be injected into a data point
    # Traverse through adverserial datasets and write to csvs
    # Create a new csv for every adverserial case
    for file in os.listdir(file_path):

        for i in range(adverserial_cases): # Create x adverserial datasets for each case
            # Choose random number of stars to perform false centroid injection
            star_count = random.randint(0, adverserial_stars)

            new_file_path = file_path + "/" + file.append("false_stars_" + star_count)
            shutil.copy(file_path + "/" + file , new_file_path)
            csv_file = open(new_file_path + "/" + file, 'w')
            csv_writer = csv.writer(csv_file)
            # If i in range 0 error, then add error handling here. 
            for i in range(star_count):
                csv_writer.writerow(f"{random.uniform(0, sensor_x):.14f}", f"{random.uniform(0, sensor_y):.14f}") # Perhaps weight the false stars to the center of the image? Maybe not yet

            csv_file.close()
    return

def apply_adverserial_positional_error_all(file_path):
    pass

def apply_adverserial_positional_error_single(file_path):
    pass


# Run script here

# First create duplicate clean folder for adverserial dataset
filepath_no_adverserial = "images_data\mag5_1608_no_adverserial_gray\centroids"
filepath_adverserial = "images_data\mag5_adverserial_centroids"

if not os.path.exists(filepath_adverserial):
    os.makedirs(filepath_adverserial)

for file in os.listdir(filepath_no_adverserial):
    shutil.copy(filepath_no_adverserial + "/" + file, filepath_adverserial + "/" + file.replace("_no_adverserial", "_adverserial")) 

apply_adverserial_false_stars(filepath_adverserial, 480, 752)