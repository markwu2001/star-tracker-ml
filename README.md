# star-tracker-ml
Second Attempt at a ML Star Tracker

## Edit: This project has been depreciated. ##
### After some night sky testing, it was determined that the machine learning approach is very sensitive to the camera model, e.g. frequency-dependence of sensor sensitivity means that red stars of lower magnitudes are visible - causing predictable counts of false stars. Another star tracking project is being developed that utilizes [the lost algorithm](https://github.com/UWCubeSat/lost) ###

Order to run files for full scale development

1. Stellarium Image Set Generation ✅
2. Centroid Dataset Extraction ✅
3. Adverserial Copy & Modification of Centroid Dataset ✅
4. Feature Extraction into Training Dataset ✅
5. Training Model ✅
6. Model Evaluation Dataset Generation using Original Stellarium Image Set

Notes:
Perhapas train model on Magnitude 4 stars for initial testing. Mag 5 produces a minimum of 107 stars per image and generates a dataset of size 17,000 for 10 adverserial cases per image. At the target of 360 adverserial cases per star, the training datset will be a size of 578,000 

First Approach: Use ML to identify center star or two, then subgraph can be narrowed down if the confidence is high enough and use traditional subgraph matching. 

Alternate Idea: Treat the ML model as the voter in the voting algorithm and feed it the same features extracted from the traditional processes. Angle between two or three stars and their distance. This way, the model can be smaller and can predict many stars. Can use multimodal approach if robustness is needed. But one main advantage for one model is that it can have a O(1) time complexity and be highly predictable for the control algorithm (Especially compared to the traditional approach). Filtering will be needed and may reduce the constant time advantage. (In reality, this constant time advantage is not that big of a deal because control agorithms usually make up for non-linearities when the requirement is "eventually hit the steady state condition". Compute time will be more important here. ML scales well for large amounts of stars, producing a high quality estimation with minimal compute time)

