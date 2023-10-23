import torch

import pickle
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import io
class CPU_Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'torch.storage' and name == '_load_from_bytes':
            return lambda b: torch.load(io.BytesIO(b), map_location='cpu')
        else: return super().find_class(module, name)

with open('/home/nguyen/NTT/OCR/ProPos/Cluster_folder/ProNos_resnet50/byol_23/feature_byol_23.pkl', 'rb') as pickle_file:
    mem_features = CPU_Unpickler(pickle_file).load()

data = mem_features
# Perform dimensionality reduction (PCA)
pca = PCA(n_components=3)
reduced_data = pca.fit_transform(data)

n_clusters = 30  # Number of clusters

import json

with open('/home/nguyen/NTT/OCR/ProPos/Cluster_folder/ProNos_resnet50/byol_23/clust_folder_byol_23_20.json', 'r') as json_file:
    cluster_folder = json.load(json_file)

labels = []
for i, keys in enumerate(cluster_folder):
    for v in cluster_folder[keys]:
        labels.append(i)
        # print(cnt)
    
labels=np.array(labels)

# Visualize the clusters in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for cluster_id in range(n_clusters):
    ax.scatter(
        reduced_data[labels == cluster_id, 0],
        reduced_data[labels == cluster_id, 1],
        reduced_data[labels == cluster_id, 2],
        
        label=f'Cluster {cluster_id}'
    )

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
ax.legend()

plt.show()
