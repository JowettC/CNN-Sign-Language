from tensorflow import keras
from sys import exit

try:
    model = keras.models.load_model('./model')
    print("Model Loaded Successfully")
except:
    print("Model not found")
    exit()
