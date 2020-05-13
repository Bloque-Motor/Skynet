import os
import numpy
from keras.models import load_model
from keras.preprocessing import image

import spectrumExtractor


def analyze(file):

    print('Loading latest model...')


    img_width, img_height = 160, 120
    sentence_path = 'Model/Sentence/'
    files = [f.path for f in os.scandir(sentence_path) if f.is_file()]
    num_files = len(files)

    model_sentence_name = [sentence_path, 'model_sentence_', str(num_files - 1), '.h5']
    model_sentence = load_model('Model/Sentence/model_sentence_0.h5')

    # model_sentence.compile(loss='categorical_crossentropy',
    #                        optimizer='adam',
    #                        metrics=['accuracy'])

    print('Opening file ' + file + 'for analysis...')

    temp_file = sentence_path + 'temp.png'
    spectrumExtractor.extract(file, temp_file)
    spectrogram = image.load_img(temp_file, target_size=(img_width, img_height))
    spectrogram = image.img_to_array(spectrogram)
    spectrogram = numpy.expand_dims(spectrogram, axis=0)
    spectrogram = spectrogram.reshape(img_width, img_height)

    print('Running prediction...')

    result = model_sentence.predict(spectrogram)
    print(result)
    os.remove(temp_file)
