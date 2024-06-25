# Test two rotationally invariant feature extraction algorithms
# 1. Binning 
#   a. Calculate minimum/maximum binning radius based on dark parts in sky for magnitude < 5.0
# 2. Angle Feature Extraction from Centroids

def find_closest_center_centroid(centroids, sensor_w, sensor_h):
    center_x, center_y = sensor_w / 2, sensor_h / 2
    closest_centroid = None
    min_distance = float('inf')
    
    for centroid in centroids:
        x, y = centroid[0], centroid[1]
        distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_centroid = centroid
    
    return closest_centroid

def feature_extraction_binning(centroids, sensor_w, sensor_h, bin_max_radius = 300 , bin_count = 10):
    bins = [0] * bin_count
    # Define circular size and distribution (try exponentially spaced) of bins

    # Find most central star, calculate distance from all stars to central star
    polestar = find_closest_center_centroid(centroids, sensor_w, sensor_h)
    # print("Polestar:", polestar , '\n')

    distances = []
    # Find most central star, calculate distance from all stars to central star
    for centroid in centroids:
        distance = ((centroid[0] - polestar[0]) ** 2 + (centroid[1] - polestar[1]) ** 2) ** 0.5 # Centroid Euclidian distance to polestar
        if distance < bin_max_radius:
            distances.append(distance)

    distances.sort()
    # print("Sorted distances:", distances , '\n')
    # DONE: modify exponential gemoetric relationship. Pure exponential does not work very well. e.g. sample binning: [0, 0, 0, 0, 0, 0, 0, 14, 53, 0]
    # Note that ML doesn't require linear relationships. Can be aribitrary or even piecewise linear
    # Generate bin edges
    bin_edges = [bin_max_radius/bin_count * i for i in range(bin_count)]
    # print("Bin edges:", bin_edges , '\n')
    """
    # I just realized non linear bins are just stupid. Set default to linear and comment out this crap
    # Consider adding flag to test non linear binning vs linear binning performance
    bin_edges = [bin_max_radius/(2*bin_count) * i for i in range(int(bin_count/2))]
    bin_edges = bin_edges + [bin_max_radius/bin_count * j for j in range(int(bin_count/2), bin_count, 1)]
    print("Bin edges:", bin_edges , '\n')
    """

    # For testing, check if any bin edges exceed the maximum image size (only useful when tested with non-synthetic image set)
    for i in range(bin_count):
        if bin_edges[i] > min(sensor_h,sensor_w):
            print("Alert! Bin edges exceed image size:", bin_edges[i] , '\n')
            return None

    # Assign distances to bins
    bin_counter = 0
    for distance in distances:
        if (bin_counter + 1) == bin_count:
            bins[bin_counter] += 1
        elif bin_edges[bin_counter] <= distance < bin_edges[bin_counter + 1]:
            bins[bin_counter] += 1
        else:
            bin_counter += 1
    return bins

