import os

import numpy
from keras import backend as K
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing import image
import operator
import spectrumExtractor


def analyze(file):
    print('Loading latest model...')

    img_width, img_height = 160, 120
    sentence_path = 'Model/Sentence/'
    files = [f.path for f in os.scandir(sentence_path) if f.path.endswith('.h5')]
    num_files = len(files)

    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    model_sentence_name = [sentence_path, 'model_sentence_', str(num_files - 1), '.h5']

    model_sentence = Sequential()
    model_sentence.add(Conv2D(32, (7, 7), input_shape=input_shape, strides=(2, 2)))
    model_sentence.add(Activation('relu'))
    model_sentence.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))

    model_sentence.add(Conv2D(32, (4, 4), strides=(2, 2)))
    model_sentence.add(Activation('relu'))

    model_sentence.add(Conv2D(64, (2, 2)))
    model_sentence.add(Activation('relu'))

    model_sentence.add(Flatten())
    model_sentence.add(Dense(64))
    model_sentence.add(Activation('sigmoid'))
    model_sentence.add(Dropout(0.2))

    model_sentence.add(Dense(5, input_dim=2))
    model_sentence.add(Activation('softmax'))

    model_sentence.compile(loss='categorical_crossentropy',
                           optimizer='adam',
                           metrics=['accuracy'])

    model_sentence.load_weights("".join(model_sentence_name))

    print('Opening file ' + file + 'for analysis...')

    temp_file = sentence_path + 'temp.png'
    spectrumExtractor.extract(file, temp_file)
    spectrogram = image.load_img(temp_file, target_size=(img_width, img_height))
    spectrogram = image.img_to_array(spectrogram)
    spectrogram = numpy.expand_dims(spectrogram, axis=0)

    print('Running prediction...')

    result_sentence = model_sentence.predict(spectrogram)

    arrayAux = numpy.array(result_sentence).tolist() # convertimos el numpy en un array, por cosas curiosas el numpy trae doble [[]], aqui lo dividimos en diferentes numeros

    arrayNum = max(arrayAux) # aquí nos quedamos con el array con un solo []
    maxValue = max(arrayNum) # cogemos el maximo valor del array
  
    index = arrayNum.index(maxValue) # vemos en que posicion se encuentra el valor maximo

    print('Tras el analisis, el archivo introducido se asemeja a la Sentence ' + str(index+1) + ' con una confianza del : ' + str(round(maxValue*100,4)) + '%') # el metodo este redondea, no se hasta que punto vale, sino usamos un %.2f para mostrar solo 2
    print(result_sentence)

    os.remove(temp_file)
