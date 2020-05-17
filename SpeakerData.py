import os
import shutil
import ntpath

print('Getting 25 speakers...')

sourcePath = "Dataset/"
sourcePathValidate = sourcePath + "Validate/"
sourcePathTrain = sourcePath + "Train/"

for filename in os.listdir(sourcePath):
    if filename.endswith(".png"):
        speaker = int(filename[4:10])
        rutaSpeaker = "spk_" + str(speaker) + "/"

        if not os.path.exists(sourcePath + rutaSpeaker):
            os.makedirs(sourcePath + rutaSpeaker)

        shutil.move(sourcePath + filename, sourcePath + rutaSpeaker, )

speakers = [f.path for f in os.scandir(sourcePath) if f.is_dir()]
arr = []
for x in range(len(speakers)):
    speakerNumber = ntpath.basename(speakers[x])
    directory = os.listdir(sourcePath + speakerNumber +"/")
    number_files = len(directory)
    arr.append((speakerNumber, number_files))

def takeSecond(elem):
    return elem[1]

arr.sort(key=takeSecond, reverse=True)
print(arr[0:4]) #poner el numero de directorios que mostrar

for y in arr[:2]: #aumentar al numero de 25, to estaba trajando con una muestra más peuqeña por eso 3

    speakerPath = y[0]

    for filename in os.listdir(sourcePath + speakerPath + "/"):

        destinationPath = sourcePathTrain + speakerPath + "/"

        if not os.path.exists(destinationPath):
            os.makedirs(destinationPath)

        shutil.move(sourcePath + speakerPath + "/" + filename, destinationPath, )

for z in arr[3:4]: #aumentar al numero de 25, to estaba trajando con una muestra más pequeña por eso 3 a 4

    speakerPath = z[0]

    for filename in os.listdir(sourcePath + speakerPath + "/"):
        destinationPath = sourcePathValidate + speakerPath + "/"
        if not os.path.exists(destinationPath):
            os.makedirs(destinationPath)

        shutil.move(sourcePath + speakerPath + "/" + filename, destinationPath, )

