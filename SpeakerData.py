import os
import shutil
import ntpath
import math
import random

print('Getting 25 speakers...')

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
        rutaSpeaker = "spk_" + speaker + "/"

        if not os.path.exists(sourcePath + rutaSpeaker):
            os.makedirs(sourcePath + rutaSpeaker)

        shutil.move(sourcePath + filename, sourcePath + rutaSpeaker, )

speakers = [f.path for f in os.scandir(sourcePath) if f.is_dir()] # cuidado con ejecutar dos veces que toma train y validate como speakers, se podria hacer un remove despues
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

for y in arr[:4]: #poner el numero 25

    speakersPath = y[0]
    files = [f.path for f in os.scandir(sourcePath + speakersPath + "/") if f.is_file()]
    num_files = len(files)
    #print(num_files)
    val_num = max(math.ceil(0.2 * num_files), 1)
    #print(val_num)
    to_move = []

    for x in range(0, val_num):
        repeated = True
        while repeated:
            rnd = random.randint(0, num_files - (x + 1))
            file = files[rnd]
            if not file in to_move:
                to_move += [file]
                repeated = False

    for file in to_move:
        speaker = file[23:29]
        dest = destinationValidate + "spk_" + speaker + "/"
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.move(file, dest,)



