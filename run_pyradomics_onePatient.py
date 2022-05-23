#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:24:13 2020

@author: cameliabencheqroun
"""


import pandas as pd
from radiomics import featureextractor


imagePath ="/Users/cameliabencheqroun/Documents/HIDS Hands on/HIDS 509 Rembrandt hands on/HF1702_1996.03.16/HF1702_image.nii"
labelPath ="/Users/cameliabencheqroun/Documents/HIDS Hands on/HIDS 509 Rembrandt hands on/HF1702_1996.03.16/HF1702_1996.03.16_GlistrBoost_out_label.nii"

extractor = featureextractor.RadiomicsFeatureExtractor()
#extracting features
result = extractor.execute(imagePath, labelPath)
#create dataframe from result
df = pd.DataFrame(list(result.items()),columns=['feature', 'value'])

#save into csv
df.to_csv('/Users/cameliabencheqroun/Documents/HIDS Hands on/HIDS 509 Rembrandt hands on/HF1702_1996.03.16/example_pyradomics.csv')   
