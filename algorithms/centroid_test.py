# 1. Use center of mass algorithm
# 2. Visual test function to overlay centroids on image

import centroid as ct
from PIL import Image

# Run code for demo
image = Image.open("images_data/mag5_1608_no_adverserial_gray/122001.png")
sources = ct.centroids_from_img(image)
ct.overlay_centroids(image, sources)