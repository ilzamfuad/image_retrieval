# import the necessary packages
from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2
import numpy as np
import sys ,json
 
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--index", required = True,help = "Path to where the computed index will be stored")
# ap.add_argument("-q", "--query", required = True,help = "Path to the query image")
# ap.add_argument("-r", "--result-path", required = True,help = "Path to the result path")
# args = vars(ap.parse_args())
 
# initialize the image descriptor
# image = bit image
# name = nama gambar
PATH_QUERY = "query/"
query = cv2.imread(PATH_QUERY+"query.jpg")

fname = "query.jpg"

# init ColorDescriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
features = cd.describe(query)
 
# perform the search
searcher = Searcher("dataset_features.json")
results = searcher.search(features)
 
# init dict result
query, result = {}, {}
result['result'], query['query'] = [], []

# display the query
# cv2.imshow("Query", query)
 
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	# result = cv2.imread(args["result_path"] + "/" + resultID)
	# cv2.imshow("Result", result)
	# cv2.waitKey(0)
	result['result'].append({
		'name':resultID,
		'photo': 'dataset/'+ resultID,
		'score': score,
		'url': 'testing'
	})

	query['query'].append({
		'nama': fname,
		'photo': 'dataset/'+fname,
		'url': 'tes'
	})
print(result)

with open('query_result.json', 'w') as outfile:
    json.dump(result, outfile)

