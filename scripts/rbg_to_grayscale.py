# 1. Convert files from RGB to 12 bit Grayscale
from PIL import Image
import os

filepath = "images_data/dslr_night_images"

if (os.path.exists(filepath+"_gray") == False):
    os.mkdir(filepath+"_gray")

# TODO: Add support for 12 bit grayscale images later
for images in os.listdir(filepath):
    if images.endswith(".JPG") or images.endswith(".png"):
        img1 = Image.open(filepath+"/"+images).convert('L')
        img1.save(filepath+"_gray"+"/"+images)