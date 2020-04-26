import os
import glob
import ntpath
import spectrumExtractor as se
# import random as rnd

path = 'Data/'

subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

for x in range(len(subfolders)):

    subfoldersSpeakers = [f.name for f in os.scandir(subfolders[x]) if f.is_dir()]
    sentence = ntpath.basename(subfolders[x])

    for y in range(len(subfoldersSpeakers)):

        locutor = subfoldersSpeakers[y]
        ruta = locutor + "/*"
        path = subfolders[x]
        print(str(locutor) + " " + str(sentence))
        recording = 0

        for filename in glob.glob(os.path.join(subfolders[x], ruta)):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:

                outputName = locutor + "_" + sentence + "_" + str(recording)
                recording += 1

                # if rnd.randint(1, 101) > 80:
                if int(locutor[4:]) > 849:
                    filepath = os.path.join('Dataset/Validate', outputName)
                else:
                    filepath = os.path.join('Dataset/Train', outputName)

                if not os.path.exists('Dataset/'):
                    os.makedirs('Dataset/')
                if not os.path.exists('Dataset/Validate'):
                    os.makedirs('Dataset/Validate')
                if not os.path.exists('Dataset/Train'):
                    os.makedirs('Dataset/Train')

                se.extract(filename, filepath)
