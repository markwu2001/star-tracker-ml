# Run inference from a sample image 

image_filepath = "images_data/mag5_1608_no_adverserial_gray/122001.png"
# image_filepath = "images_data/mag5_1608_no_adverserial_gray/4147001.png"
model_filepath = "ml/models/star_tracker_model_large.keras"

bin_count = 10
bin_max_radius = 400

import os
import sys
import csv
import tensorflow as tf
import pandas as pd
import numpy as np
from PIL import Image
from photutils.centroids import centroid_sources
from astropy.stats import sigma_clipped_stats
from astropy.io import fits
from photutils.detection import DAOStarFinder
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils.aperture import CircularAperture

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'algorithms'))
import centroid as ct
import feature_extraction as bin

np.set_printoptions(threshold=sys.maxsize)

centrosoids = []
bins = []
img = Image.open(image_filepath)

# Calculate centroids for each image
centroids = ct.centroids_from_img(img)
centroids = centroids['xcentroid', 'ycentroid']
print("Centroids: ", centroids)

# Binning Feature Extraction
bins = bin.feature_extraction_binning(centroids, 752, 480, bin_max_radius, bin_count)

# loaded_model = tf.saved_model.load(model_filepath)
loaded_model = tf.keras.models.load_model(model_filepath)
print("\nLoaded Model\n")

bins = np.array(bins)
reshaped_bins = bins.reshape(-1,10)
print("Reshaped Bins: ", reshaped_bins)

predictions = loaded_model(reshaped_bins)
# print("Predictions: ", predictions)
print("Max Prediction: ", np.max(predictions),"\n")

# sorted_predictions = np.sort(predictions) 
# print("Top 3 Predictions: ", sorted_predictions[-3:])

# TODO: Figure out labels


temp_y_label_source = "images_data/mag5_adverserial_bins/mag5_adverserial_bins.csv"
# TODO: read the header instead of hardcoding it
dataframe = pd.read_csv(temp_y_label_source, header=0, names=["HIP", "bin0", "bin1", "bin2", "bin3", "bin4", "bin5", "bin6", "bin7", "bin8", "bin9"])
dataset = dataframe.values
Y = dataset[:,0].astype(int)
encoder = LabelEncoder()
encoder.fit(Y)

print("Prediction Index: ", predictions.numpy().argmax())
print("Label: ", encoder.classes_[predictions.numpy().argmax()])

# encoded_predictions = np.zeros(len(predictions.numpy().flatten())).astype(int)
# encoded_predictions[predictions.numpy().argmax()] = 1
# print("Encoded Predictions: ",encoded_predictions)

# label = encoder.inverse_transform(encoded_predictions)
# print("Label: ", label)