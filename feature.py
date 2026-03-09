import cv2
import numpy as np
from skimage.feature import local_binary_pattern
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")


def color_feature(image):

    image = cv2.resize(image,(224,224))

    hist = cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])

    cv2.normalize(hist,hist)

    return hist.flatten()


def texture_feature(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    lbp = local_binary_pattern(gray,8,1,method="uniform")

    hist,_ = np.histogram(lbp.ravel(),bins=10,range=(0,10))

    hist = hist.astype("float")

    hist /= hist.sum()

    return hist


def deep_feature(image):

    image = cv2.resize(image,(224,224))

    image = img_to_array(image)

    image = np.expand_dims(image,axis=0)

    image = preprocess_input(image)

    feature = model.predict(image)

    return feature.flatten()


def extract_feature(image):

    c = color_feature(image)

    t = texture_feature(image)

    d = deep_feature(image)

    return np.concatenate([c,t,d])