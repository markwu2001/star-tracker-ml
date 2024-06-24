# star-tracker-ml
Second Attempt at a ML Star Tracker

Order to run files for full scale development

1. Stellarium Image Set Generation
2. Centroid Dataset Extraction 
3. Adverserial Copy & Modification of Centroid Dataset
4. Feature Extraction into Training Dataset
5. Training Model
6. Model Evaluation Dataset Generation using Original Stellarium Image Set

Notes:
Perhapas train model on Magnitude 4 stars for initial testing. Mag 5 produces a minimum of 107 stars per image and generates a dataset of size 17,000 for 10 adverserial cases per image. At the target of 360 adverserial cases per star, the training datset will be a size of 578,000 
