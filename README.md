# Code used for the REMBRANDT MRI paper to extract PyRadiomics features from Rembrandt MRI data

## Prerequisites
* Python installed on your machine, version 3.5 or higher.
* Pandas installed
* Download data folder on your machine

## Install PyRadiomics
* Depending on your environment use either pip or conda to install PyRadiomics :
`python -m pip install pyradiomics` 
`conda install -c radiomics pyradiomics`

## How the python code works
* There is a loop that walks through the directory tree (the root folder data). It uses the function `os.walk()` . The parameters to pass are
  * dirName: The next directory it found.
  * subdirList: A list of sub-directories in the current directory. 
  * fileList: A list of files in the current directory. 
* For each patient, the PyRadiomics features are extracted and saved in a data frame. 
* Save your final data frame into a csv
