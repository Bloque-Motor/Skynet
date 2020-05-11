import os
import shutil
import ntpath

print('Extracting Data for Speaker Trainer...')

sourcePath = "Dataset/"
sourcePathValidate = sourcePath + "Validate/"
sourcePathTrain = sourcePath + "Train/"

destinationPath = "Dataset/"

speakersValidate = [f.path for f in os.scandir(sourcePathValidate) if f.is_dir()]
speakersTrainers = [f.path for f in os.scandir(sourcePathTrain) if f.is_dir()]

for x in range(len(speakersValidate)):

    speakerV = ntpath.basename(speakersValidate[x])
    extractValidatePath = sourcePathValidate + speakerV + "/"

    for filename in os.listdir(extractValidatePath):

      if filename.endswith(".png"):

        shutil.move(extractValidatePath + filename, destinationPath, )

    try:
        os.rmdir(extractValidatePath)
    except OSError as e:
        print("Error: %s : %s" % (extractValidatePath, e.strerror))


for y in range(len(speakersValidate)):

    speakerT = ntpath.basename(speakersTrainers[y])
    extractTrainPath = sourcePathTrain + speakerT + "/"

    for filename in os.listdir(extractTrainPath):

      if filename.endswith(".png"):

        shutil.move(extractTrainPath + filename, destinationPath, )

    try:
        os.rmdir(extractTrainPath)
    except OSError as e:
        print("Error: %s : %s" % (extractTrainPath, e.strerror))


try:
    os.rmdir(sourcePathValidate)
except OSError as e:
    print("Error: %s : %s" % (sourcePathValidate, e.strerror))


try:
    os.rmdir(sourcePathTrain)
except OSError as e:
    print("Error: %s : %s" % (sourcePathTrain, e.strerror))