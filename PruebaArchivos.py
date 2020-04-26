import os
import glob
import ntpath

path = 'Data/'

subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]

for x in range(len(subfolders)):

    subfoldersSpeakers = [f.name for f in os.scandir(subfolders[x]) if f.is_dir()]
    sentence = ntpath.basename(subfolders[x])
    for y in range (len(subfoldersSpeakers)):

        locutor = subfoldersSpeakers[y]
        print(locutor)
        ruta = locutor + "/*"
        path = subfolders[x]
        for filename in glob.glob(os.path.join(subfolders[x], ruta)):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:

                #print(ntpath.basename(filename))

                outputName = "output_" + ntpath.basename(filename)

                filepath = os.path.join('Output/', outputName)
                if not os.path.exists('Output/'):
                    os.makedirs('Output/')
                f = open(filepath, "w")
                f.close()







