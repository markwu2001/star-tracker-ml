import numpy as np
import cv2

def generate_grid_image(height, width, dot_size, dot_spacing):
    # Calculate the number of dots in each dimension
    num_dots_height = int(height / (dot_size + dot_spacing))
    num_dots_width = int(width / (dot_size + dot_spacing))

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw black dots on the image
    for i in range(num_dots_height):
        for j in range(num_dots_width):
            x = j * (dot_size + dot_spacing) + dot_spacing
            y = i * (dot_size + dot_spacing) + dot_spacing
            cv2.circle(image, (x, y), dot_size, (0, 0, 0), -1 , lineType=cv2.LINE_AA)

    return image

# Configurable parameters
height = 1440
width = 2560
dot_size = 8
dot_spacing = 16

# Generate the grid image
grid_image = generate_grid_image(height, width, dot_size, dot_spacing)

# Save the image as a PNG file
cv2.imwrite('images_data/calibration_images/calibration_image.png', grid_image)