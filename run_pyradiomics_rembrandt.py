#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:04:23 2020

@author: cameliabencheqroun
"""


import os  # needed navigate the system to get the input data
import pandas as pd
import time

import radiomics
from radiomics import featureextractor

start_time = time.time()

data_path = "/Users/cameliabencheqroun/Documents/Projects/REMBRANDT Project/Rembrandt Final Data Corrected"

#print("data_path, relative path:", data_path)
#print("data_path, absolute path:", os.path.abspath(data_path))

# Gerenate Rembrandt features 
df_all = pd.DataFrame(columns=['ID','feature','value'])
for dirName, subdirList, fileList in os.walk(data_path):
    for filename in fileList:
        if "_label.nii"in filename.lower() :
            case = filename.split('_')[0]
            imageName = filename.split('_')[0] + "_image.nii.gz"
            # Store the file paths image and label map into two variables
            imagePath = os.path.join(dirName,imageName)
            labelPath = os.path.join(dirName,filename)
         #   print(imagePath)
         #   print(labelPath)
            #pyradiomics
            # Instantiate the extractor
            extractor = featureextractor.RadiomicsFeatureExtractor()
            #extracting features
            result = extractor.execute(imagePath, labelPath)
            #create dataframe from result
            df = pd.DataFrame(list(result.items()),columns=['feature', 'value'])
            df.insert(0, 'ID', case)            
            df_all=df_all.append(df, ignore_index = True)

df_final = df_all.pivot(index='ID',columns='feature', values = 'value')
df_final.insert(len(df_final.columns), 'Source', 'Rembrandt')
 
   
#save into csv
#data_path_final = "/Users/cameliabencheqroun/Documents/Projects/REMBRANDT Project/Rembrandt_Glistrboost"
df_final.to_csv(os.path.join(data_path,r'pyradomics_rembrandt_features_final.csv'))   

total_time = (time.time() - start_time)/60
print(" Time generating features ", total_time, " min")