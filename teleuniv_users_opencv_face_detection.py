import cv2
import os
import imghdr
# fnames = os.listdir("C:/Users/andey/Desktop/teleuniv-images") #I tried this, for some reason I wasn't able to read the file names
# Load the cascade
face_cascade = cv2.CascadeClassifier('C:/Users/andey/Documents/MyGithubRepos/TeleunivUserImages/haarcascade_frontalface_default.xml')

base_dir = "" #enter base dir
for i in range(910,22000):
    num=str(i)
    if imghdr.what(base_dir+num+'.jpg')==None: #If it is not an image we get None. So delete it.
        os.remove(base_dir+num+'.jpg')
        continue
    img = cv2.imread(base_dir+num+'.jpg') # Read the input image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces)==0:
        os.remove(base_dir+num+'.jpg')
