import cv2
from matplotlib import pyplot as plt
import os
import pickle
from SiftHelperFunctions import *


def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)



data = []

sift = cv2.SIFT_create()
path1 = '../Data_Set/TrainingData/'
listing = os.listdir(path1)
# listing.remove('.git')
for file in listing:
    img = cv2.imread(path1 + file)

    # image comparison
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # need to do some more processing here

    # find the keypoints and descriptors with SIFT
    kp, des = sift.detectAndCompute(gray_img, None)
    img_size = (len(gray_img[0]), len(gray_img))

    centroid = get_centroid(kp)
    # centroid = (img_size[0]/2, img_size[1]/2)

    temp_kp = make_temp_kp(kp)
    datum = [temp_kp, des, img_size, centroid, path1 + file]
    data.append(datum)

save_object(data, '../Data_Set/training_data.pkl')
