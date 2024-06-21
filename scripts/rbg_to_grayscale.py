# 1. Convert files from RGB to 12 bit Grayscale
from PIL import Image
import os

filepath = "images_data/mag5_1608_no_adverserial"

if (os.path.exists(filepath+"_gray") == False):
    os.mkdir(filepath+"_gray")

for images in os.listdir(filepath):
    img1 = Image.open(filepath+"/"+images).convert('L')
    img1.save(filepath+"_gray"+"/"+images)