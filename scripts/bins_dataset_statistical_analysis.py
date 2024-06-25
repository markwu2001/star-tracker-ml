import pandas as pd

# Load the dataset
file_path = "images_data/mag5_adverserial_bins/mag5_adverserial_bins.csv"
data = pd.read_csv(file_path)

# Group by HIP
grouped = data.groupby('HIP')

# Calculate mean and standard deviation for each group
stats = grouped.agg(['mean', 'std'])

# Calculate how many unique instances with non-identical data there are per HIP
unique_instances_per_HIP = grouped.nunique()
# print(unique_instances_per_HIP)

#Calculate the average number of unique HIP instances
average_unique_instances_per_HIP = unique_instances_per_HIP.mean().mean()
print("Average number of unique HIP instances:", round(average_unique_instances_per_HIP, 3)) # print with a 3 decimal point precision


# Summarize the mean standard deviation across all bins
mean_std_dev = stats.iloc[:, 1:].mean()

# Print the statistics
# print(mean_std_dev)

# Create a list with only the std in mean_std_dev
std_list = mean_std_dev.loc[(slice(None), 'std')].tolist()
print("Average standard deviation of bins:", round(sum(std_list) / len(std_list), 3)) # print standard deviation to 3 decimal points



