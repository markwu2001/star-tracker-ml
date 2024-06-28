# Import algorithm that converts star location on image plane to star unit vector

def star_to_unit_vectors(centroid_x_corrected, centroid_y_corrected, principal_point_x = 0, principal_point_y = 0, focal_length = 0.0028, pixel_pitch_x = 0.0000056, pixel_pitch_y = 0.0000056):
    unit_vector = [0,0,0]
    """
    Convert star locations on image plane to star unit vectors
    Be caeful with units of focal lengths and pixel pitchs when inputting parameters
    """
    unit_vector[0] = (centroid_x_corrected-principal_point_x)*(pixel_pitch_x/focal_length)*(1 + ((centroid_x_corrected-principal_point_x)*(pixel_pitch_x/focal_length))**2 + ((centroid_y_corrected-principal_point_y)*(pixel_pitch_y/focal_length))**2)**0.5
    unit_vector[1] = (centroid_y_corrected-principal_point_y)*(pixel_pitch_y/focal_length)*(1 + ((centroid_x_corrected-principal_point_x)*(pixel_pitch_x/focal_length))**2 + ((centroid_y_corrected-principal_point_y)*(pixel_pitch_y/focal_length))**2)**0.5
    unit_vector[2] = (1 + ((centroid_x_corrected-principal_point_x)*(pixel_pitch_x/focal_length))**2 + ((centroid_y_corrected-principal_point_y)*(pixel_pitch_y/focal_length))**2)**0.5

    return unit_vector