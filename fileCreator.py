import os
import glob
import ntpath
import spectrumExtractor as se

# import random as rnd


def generate():
    path = 'Data/'
    output_path = "Dataset/"
    destination_validate = output_path + "Validate/"
    destination_train = output_path + "Train/"

    makeOutputDirs(output_path, destination_validate, destination_train)

    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

    for x in range(len(subfolders)):

        subfolders_speakers = [f.name for f in os.scandir(subfolders[x]) if f.is_dir()]
        sentence = ntpath.basename(subfolders[x])

        for y in range(len(subfolders_speakers)):

            locutor = subfolders_speakers[y]
            ruta = locutor + "/*"
            path = subfolders[x]
            print(str(locutor) + " " + str(sentence))
            recording = 0

            for filename in glob.glob(os.path.join(subfolders[x], ruta)):
                with open(os.path.join(os.getcwd(), filename), 'r') as f:

                    outputName = locutor + "_" + sentence + "_" + str(recording)
                    recording += 1

                    # if rnd.randint(1, 101) > 80:
                    if int(locutor[4:]) > 749:
                        dest = destination_validate
                    else:
                        dest = destination_train

                    if sentence == 'S1':
                        dest = dest + "S1/"
                    elif sentence == 'S2':
                        dest = dest + "S2/"
                    elif sentence == 'S3':
                        dest = dest + "S3/"
                    elif sentence == 'S4':
                        dest = dest + "S4/"
                    elif sentence == 'S5':
                        dest = dest + "S5/"

                    filepath = os.path.join(dest, outputName)

                    se.extract(filename, filepath)


def makeOutputDirs(output_path, destination_validate, destination_train):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if not os.path.exists(destination_validate):
        os.makedirs(destination_validate)
    if not os.path.exists(destination_train):
        os.makedirs(destination_train)

    if not os.path.exists(destination_validate + 'S1'):
        os.makedirs(destination_validate + 'S1')

    if not os.path.exists(destination_validate + 'S2'):
        os.makedirs(destination_validate + 'S2')

    if not os.path.exists(destination_validate + 'S3'):
        os.makedirs(destination_validate + 'S3')

    if not os.path.exists(destination_validate + 'S4'):
        os.makedirs(destination_validate + 'S4')

    if not os.path.exists(destination_validate + 'S5'):
        os.makedirs(destination_validate + 'S5')

    if not os.path.exists(destination_train + 'S1'):
        os.makedirs(destination_train + 'S1')

    if not os.path.exists(destination_train + 'S2'):
        os.makedirs(destination_train + 'S2')

    if not os.path.exists(destination_train + 'S3'):
        os.makedirs(destination_train + 'S3')

    if not os.path.exists(destination_train + 'S4'):
        os.makedirs(destination_train + 'S4')

    if not os.path.exists(destination_train + 'S5'):
        os.makedirs(destination_train + 'S5')
