# import the necessary packages
from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import os, json
from matplotlib import pyplot as plt

PATH_DATASET = "dataset/"
 
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--dataset", required = True,help = "Path to the directory that contains the images to be indexed")
# ap.add_argument("-i", "--index", required = True,help = "Path to where the computed index will be stored")
# args = vars(ap.parse_args())
 
# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))

dataset_features = {}
dataset_features['features'] = []

print()

# open the output index file for writing
# output = open(args["index"], "w")
# use glob to grab the image paths and loop over them
for imagePath in os.listdir(PATH_DATASET):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath
    
    # load image
    image = cv2.imread(PATH_DATASET+imagePath)
    
    # describe the image
    features = cd.describe(image)

    # write the features to file
    features = [f for f in features]
    
    # append feature
    dataset_features['features'].append({
        'nama': imageID,
        'region_1': features[0].tolist(),
        'region_2': features[1].tolist(),
        'region_3': features[2].tolist(),
        'region_4': features[3].tolist(),
        'url': 'tester'
    })

with open('dataset_features.json', 'w') as outfile:
    json.dump(dataset_features, outfile)
 
# close the index file
# output.close()