# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
import argparse
import cv2
import os
import sys

x = 0;
path2 = 'good'





def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# loop over the input images
for imagePath in paths.list_images(args["images"]):
	x = x + 1
	# load the image, convert it to grayscale, and compute the
	# focus measure of the image using the Variance of Laplacian
	# method
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	text = "Not Blurry"
	
	cascPath = 'haarcascade_profileface.xml'
	faceCascade = cv2.CascadeClassifier(cascPath)
	faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
	)
	
	cascPath = 'haarcascade_frontalface_default.xml'
	faceCascade = cv2.CascadeClassifier(cascPath)
	
	faces2 = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)
	

	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
	#if fm < args["threshold"] or len(faces) == 0:
	if len(faces) == 0 and len(faces2) == 0 and fm < args["threshold"]:
		text = "Blurry"
		path = 'bad'
		cv2.imwrite(os.path.join(path , str(x)+'.jpg'), image)
		print("Found no faces and moved to bad!")
		
	else:
		cv2.imwrite(os.path.join(path2 , str(x)+'.jpg'), image)
		print("Found {0} faces and moved to good!".format(len(faces)))
			
		

