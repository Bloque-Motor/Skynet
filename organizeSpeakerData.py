import os
import shutil

print('Moving files...')

sourcePath = "Dataset/"
destinationValidate = sourcePath + "Validate/"
destinationTrain = sourcePath + "Train/"

if not os.path.exists(destinationValidate):
    os.makedirs(destinationValidate)
if not os.path.exists(destinationTrain):
    os.makedirs(destinationTrain)

for filename in os.listdir(sourcePath):
    if filename.endswith(".png"):

        speaker = filename[4:10]
        dest = destinationTrain + "spk_" + speaker + "/"
        if not os.path.exists(dest):
            os.makedirs(dest)

        shutil.move(sourcePath + filename, dest, )



