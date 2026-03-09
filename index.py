import os
import cv2
import numpy as np
from feature import extract_feature

DATASET_PATH = "dataset"

features = []
names = []

for file in os.listdir(DATASET_PATH):

    path = os.path.join(DATASET_PATH,file)

    img = cv2.imread(path)

    if img is None:
        continue

    f = extract_feature(img)

    features.append(f)
    names.append(file)

np.save("features.npy",features)
np.save("names.npy",names)

print("Index created:",len(features))