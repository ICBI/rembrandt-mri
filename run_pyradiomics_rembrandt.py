#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:04:23 2020

@author: cameliabencheqroun
"""


import os  
import pandas as pd
import time

#import radiomics
from radiomics import featureextractor

start_time = time.time()

data_path ="/Users/cameliabencheqroun/Downloads/NITRC-multi-file-downloads"

# Gerenate Rembrandt features 
df_all = pd.DataFrame(columns=['ID','feature','value'])
for dirName, subdirList, fileList in os.walk(data_path):
    labelPath= ""
    imagePath =""
    case =""
    for filename in fileList:
        if "-labels.nii"in filename.lower() :
            case = filename.split('_')[0]
            labelPath = os.path.join(dirName,filename)
            #print('label path :     ',labelPath)
        elif "_t1_"in filename.lower() :
            imagePath = os.path.join(dirName,filename)
           # print('image path :     ', imagePath)
    
        if imagePath and labelPath :
            print('labelpatth and imagepath and case: ', case,labelPath, imagePath)
            extractor = featureextractor.RadiomicsFeatureExtractor()
            result = extractor.execute(imagePath, labelPath)
            #print('result:     ', result)
            #create dataframe from result
            df = pd.DataFrame(list(result.items()),columns=['feature', 'value'])
            df.insert(0, 'ID', case)            
            df_all=df_all.append(df, ignore_index = True)
            labelPath= ""
            imagePath =""
            case =""
         
df_final = df_all.pivot(index='ID',columns='feature', values = 'value')
df_final.insert(len(df_final.columns), 'Source', 'Rembrandt')

#save into csv
df_final.to_csv(os.path.join(data_path,r'pyradomics_rembrandt_features_final.csv'))   

total_time = (time.time() - start_time)/60
print(" Time generating features ", total_time, " min")
