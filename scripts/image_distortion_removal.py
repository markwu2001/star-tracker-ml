import os
import numpy as np
import discorpy.losa.loadersaver as io
import discorpy.prep.preprocessing as prep
import discorpy.proc.processing as proc
import discorpy.post.postprocessing as post

distorted_image_path = "images_data/dslr_night_images/"
distorted_image_filename = "focused_star_dsc0014_752x502_gray_hip75458.png"
output_dir = "images_data/dslr_night_images/distortion_corrected/"
distortion_coefficients_file = "images_data/calibration_images/corrected/coefficients_radial_distortion.txt"



def remove_distortion(distorted_image_path, distorted_image_filename, output_dir , distortion_coefficients_file):
    mat0 = io.load_image(distorted_image_path + distorted_image_filename).astype("uint32") # Load image

    # Load coefficients from previous calculation if need to
    (xcenter, ycenter, list_fact) = io.load_metadata_txt(distortion_coefficients_file)
    # Correct the image
    corrected_mat = post.unwarp_image_backward(mat0, xcenter, ycenter, list_fact)
    # Save results. Note that the output is 32-bit numpy array. Convert to lower-bit if need to.
    io.save_image(output_dir + "/" + distorted_image_filename + "_corrected_image.png", corrected_mat)
    io.save_image(output_dir + "/" + distorted_image_filename + "_difference.png", corrected_mat - mat0)


if not (os.path.exists(output_dir)):
    os.makedirs(output_dir)

remove_distortion(distorted_image_path, distorted_image_filename, output_dir , distortion_coefficients_file)