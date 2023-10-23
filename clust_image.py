import json
import os

with open('byol_23_15.json', 'r') as json_file:
    Cluster_folder = json.load(json_file)

import shutil

paths = '/home/nguyen/NTT/OCR/ProPos/Clusted/'
path_to_all_data = '/home/nguyen/NTT/OCR/ProPos/DATA/ocr_dataset/new_train/'
for i in Cluster_folder:
    #make folder
    class_folder = paths + i 
    os.mkdir(class_folder)
    
    for file_image_name in Cluster_folder[i]:
        shutil.copy(path_to_all_data + file_image_name, class_folder)
