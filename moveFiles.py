import os
import shutil

print('Moving files...')

sourcePath = "Dataset/"
destinationValidate = sourcePath + "Validate/"
destinationTrain = sourcePath + "Train/"


if not os.path.exists(destinationValidate + 'S1'):
    os.makedirs(destinationValidate + 'S1')

if not os.path.exists(destinationValidate + 'S2'):
    os.makedirs(destinationValidate + 'S2')

if not os.path.exists(destinationValidate + 'S3'):
    os.makedirs(destinationValidate + 'S3')

if not os.path.exists(destinationValidate + 'S4'):
    os.makedirs(destinationValidate + 'S4')

if not os.path.exists(destinationValidate + 'S5'):
    os.makedirs(destinationValidate + 'S5')

if not os.path.exists(destinationTrain + 'S1'):
    os.makedirs(destinationTrain + 'S1')

if not os.path.exists(destinationTrain + 'S2'):
    os.makedirs(destinationTrain + 'S2')

if not os.path.exists(destinationTrain + 'S3'):
    os.makedirs(destinationTrain + 'S3')

if not os.path.exists(destinationTrain + 'S4'):
    os.makedirs(destinationTrain + 'S4')

if not os.path.exists(destinationTrain + 'S5'):
    os.makedirs(destinationTrain + 'S5')

for filename in os.listdir(sourcePath):
    if filename.endswith(".png"):
        if int(filename[4:10]) > 749:
            dest = destinationValidate
        else:
            dest = destinationTrain

        sentence = filename[11:13]
        if sentence == 'S1':
            dest = dest + "S1"
        elif sentence == 'S2':
            dest = dest + "S2"
        elif sentence == 'S3':
            dest = dest + "S3"
        elif sentence == 'S4':
            dest = dest + "S4"
        elif sentence == 'S5':
            dest = dest + "S5"

        shutil.move(sourcePath + filename, dest)


