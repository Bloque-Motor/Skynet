import os
import glob
import ntpath
import spectrumExtractor as se

path = 'Data/'

subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

for x in range(len(subfolders)):

    subfoldersSpeakers = [f.name for f in os.scandir(subfolders[x]) if f.is_dir()]
    sentence = ntpath.basename(subfolders[x])

    for y in range(len(subfoldersSpeakers)):

        locutor = subfoldersSpeakers[y]
        ruta = locutor + "/*"
        path = subfolders[x]

        recording = 0

        for filename in glob.glob(os.path.join(subfolders[x], ruta)):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:

                # print(ntpath.basename(filename))

                outputName = locutor + "_" + sentence + "_" + str(recording)
                recording += 1

                filepath = os.path.join('Output/', outputName)
                if not os.path.exists('Output/'):
                    os.makedirs('Output/')
                # f = open(filepath, "w")
                # f.close()
                se.extract(filename, filepath)
