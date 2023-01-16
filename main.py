from tensorflow import keras
from sys import exit
import cv2

try:
    model = keras.models.load_model('./model')
    print("Model Loaded Successfully")
except:
    print("Model not found")
    exit()


im_gray = cv2.imread('test_image.jpg', cv2.IMREAD_GRAYSCALE)