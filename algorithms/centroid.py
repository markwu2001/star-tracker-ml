import numpy as np
from PIL import Image
from photutils.centroids import centroid_sources
from astropy.stats import sigma_clipped_stats
from astropy.io import fits
from photutils.detection import DAOStarFinder
import os
import csv

import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils.aperture import CircularAperture


def centroids_from_img(img):
    """
    Calculate the center of mass of stars in an image to retrieve subpixel accurate centroids
    """
    # 1. Segment image plane using photutils
    # 2. Use photutils BFS centroid algorithm https://photutils.readthedocs.io/en/stable/centroids.html
    # 3. Append centroids to list

    data = np.array(img)
    # the following is for background noise removal. Implement later and see https://photutils.readthedocs.io/en/stable/detection.html
    mean, median, std = sigma_clipped_stats(data, sigma=3.0)  
    print((mean, median, std))  

    daofind = DAOStarFinder(fwhm=3.0, threshold=2*std)  # TODO make the threshold a tunable parameter
    sources = daofind(data - median)
    # daofind = DAOStarFinder(fwhm=3.0, threshold=5)  # Run this for no background noise removal TODO: Adjust fwhm and threshold later.
    # sources = daofind(data)

    return sources


def overlay_centroids(img, sources): # Move this to centroid_test.py when it's time to port files to MCU
    """
    Overlay the centroids on an image
    """
    data = np.array(img)

    for col in sources.colnames:  
        if col not in ('id', 'npix'):
            sources[col].info.format = '%.2f'  # for consistent table output
    sources.pprint(max_width=110)  

    positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
    apertures = CircularAperture(positions, r=4.0)
    norm = ImageNormalize(stretch=SqrtStretch())
    plt.imshow(data, cmap='Greys', origin='lower', norm=norm, interpolation='nearest')
    apertures.plot(color='blue', lw=1.5, alpha=0.5)
    plt.show() # If this isn't working on WSL2, try isntalling tkinter:  sudo apt-get install python3-tk
    return None


    



