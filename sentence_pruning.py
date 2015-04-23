##Sentence pruning takes reviews text and features as input and extracts only those sentences, which contain any of the features from our list of frequent noun features.
##Output file is a json file with format: {business_id:business_name:[list of reviews with pruned sentences]}

import pickle
import sys
import json
import re

if(len(sys.argv)<3):
	print("usage:python sentence_pruning.py ReviewsFileName.json FeatureFileName > OutputFileName.json")
	sys.exit()

## Open the ReviewsFile
reviews=open(sys.argv[1]);	
data=json.load(reviews)

## Open the list of FeatureFile
featurefile=open(sys.argv[2],"rb")
feature_vector=pickle.load(featurefile)
featurefile.close()
features=set(feature_vector)
##Extract only the features

##OutputJson
output=dict()
# For each business and it's review list
for business,reviewList in data.items():
	## For each review in the review list
	output[business]=list()
	for review in reviewList:
		##print("\n\nreview:"+review)
		##For each sentence in a review
		sentenceList=filter(None, re.split("[.!?\-]+", review))
		#sentenceList=reviews.split("\n")
		text="";
		for sentence in sentenceList:
			#print(sentence)
			words=sentence.split()
			words=set(words)
			#print(feature_vector)
			#print(words)
			##Check if the sentence contains any of the feature list words and add that sentence
			if words & features:
			#if any(word in words for word in features):
				#print("******")
				text+=sentence+".";	
		if text!= "":
			output[business].append(text)
	#print(output)
json_data=json.dumps(output)
print(json_data)
