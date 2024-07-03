#1. TODO: Post Centroiding False Star Error (0-5 count random)
#2. TODO: Post Centroiding Gaussian Positional Error applied to all stars
#3. TODO: Post Centoiding Gaussian Positional Error applied to single stars

import csv
import os
import random
import shutil

def apply_adverserial_false_stars(file_path, sensor_x, sensor_y, adverserial_cases = 360):
    # adverserial_cases = 10 # how many adverserial datapoints are created per original data point. Recommended 360 
    adverserial_stars = 5 # max false stars to be injected into a data point
    # Traverse through adverserial datasets and write to csvs
    # Create a new csv for every adverserial case
    for file in os.listdir(file_path):
        
        for i in range(adverserial_cases): # Create x adverserial datasets for each case 
            # Choose random number of stars to perform false centroid injection
            star_count = random.randint(0, adverserial_stars)

            new_file_path_name = file_path + "/" + file.strip(".csv") + "_case_" + str(i) + "_false_stars_" + str(star_count) + ".csv"
            shutil.copy(file_path + "/" + file , new_file_path_name)
            csv_file = open(new_file_path_name, 'a', newline='')
            csv_writer = csv.writer(csv_file)
            # If i in range 0 error, then add error handling here. 
            for j in range(star_count): 
                csv_writer.writerow([f"{random.uniform(0, sensor_x):.14f}", f"{random.uniform(0, sensor_y):.14f}"]) # Perhaps weight the false stars to the center of the image? Maybe not yet

            csv_file.close()
    return

def apply_adverserial_positional_error(file_path, sensor_x, sensor_y, sigma_all_stars=0.01, sigma_single_stars=0.0001):
    for file in os.listdir(file_path):

        # Read the CSV file and store its content in a list
        with open(file_path + "/" + file, 'r') as file_opened:
            reader = csv.reader(file_opened)
            rows = list(reader)

        # Add positional error to all stars in the csv. ensure the values do not exceed the maximum sensor values
        errorXAll = random.gauss(0, sigma_all_stars)
        errorYAll = random.gauss(0, sigma_all_stars)
        for row in rows[1:]:
            errorXSingle = random.gauss(0, sigma_single_stars)*random.randint(0,1)
            errorYSingle = random.gauss(0, sigma_single_stars)*random.randint(0,1)
            if ((float(row[0]) + errorXAll + errorXSingle) < sensor_x  and  (float(row[0]) - errorXAll - errorXSingle) > 0):
                row[0] = float(row[0]) + errorXAll+errorXSingle
            if ((float(row[1]) + errorYAll + errorYSingle) < sensor_y  and  (float(row[1]) - errorYAll - errorYSingle) > 0):
                row[1] = float(row[1]) + errorYAll + errorYSingle
            # print(row)

        # Clear the content of the CSV file
        with open(file_path + "/" + file, "w", newline="") as file_opened:
            pass

        # Write the modified list back to the CSV file
        with open(file_path + "/" + file, "w", newline="") as file_opened:
            writer = csv.writer(file_opened)
            writer.writerows(rows)
    return


# Script Usage

# First create duplicate clean folder for adverserial dataset
# filepath_no_adverserial = "images_data\mag5_1608_no_adverserial_gray\centroids"
# filepath_adverserial = "images_data\mag5_adverserial_centroids"

# if not os.path.exists(filepath_adverserial):
#     os.makedirs(filepath_adverserial)

# for file in os.listdir(filepath_no_adverserial):
#     shutil.copy(filepath_no_adverserial + "/" + file, filepath_adverserial + "/" + file.replace("_no_adverserial", "_adverserial")) 

# apply_adverserial_false_stars(filepath_adverserial, 480, 752, 10)

# apply_adverserial_positional_error(filepath_adverserial, 480,752,0.01,0.0001)