import os
import glob
import ntpath

path = 'Data/'

subfolders = [ f.name for f in os.scandir(path) if f.is_dir() ]

for x in range(len(subfolders)):

    ruta = path + subfolders +"/"
    subfoldersSpeakers = [f.name for f in os.scandir(path) if f.is_dir()]

    for y in range (0,2):
        locutor = subfoldersSpeakers[y]
        ruta = locutor + "/*"

        for filename in glob.glob(os.path.join(path, ruta)):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:

                print(ntpath.basename(filename))

                outputName = "output_" + ntpath.basename(filename)

                filepath = os.path.join('Output/', outputName)
                if not os.path.exists('Output/'):
                    os.makedirs('Output/')
                f = open(filepath, "a")
                f.close()







