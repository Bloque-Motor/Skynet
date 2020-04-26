import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

classesSentence = ['S1','S2','S3','S4','S5']
num_Sentences = lent(classesSentence)

train_path = 'Data'