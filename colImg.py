import cv2
import argparse 
import numpy as np 

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", default="img", type=str, help="Base name of the images")
ap.add_argument("-c", "--classes", required=True, type=int, help="Number of classes")
ap.add_argument("-s", "--step", required=True, type=int, help="Number of images of each class")
ap.add_argument("-g", "--2gray", default=False, type=bool, help="Wether to convert to grayscale")
ap.add_argument("-r", "--resolution", default="NULL", type=str, help="Resolution of images, For instance: '128x128'")
args = vars(ap.parse_args())

