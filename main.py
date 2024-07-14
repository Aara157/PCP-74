import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
from keras.models import Sequential,load_model,Model
from keras.layers import Conv2D,MaxPool2D,Dense,Dropout,BatchNormalization,Flatten,Input
from sklearn.model_selection import train_test_split
from cvzone.FaceDetectionModule import FaceDetector

# Create a path variable to the path of your dataset


# Create empty images list and categories list


# Loop throught each img in path

    # Add try block
    
        # Print the img
        
    
        # Split the img address from "_" and get the first character and store in type variable
        
        # Load the image
        
        # Change image from BGR to RGB
        
        # Resize the image to 200,200
        
        # Append the image to images list
        
        # Append the type to categories list
        
    # Add except block  
    

# Print count of all image i.e len(images)

