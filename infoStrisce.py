from PIL import Image
import os
import shutil

imageDirectory = r"E:\_pytest\88_Putifigari\2014"
outPutDir = os.path.join(imageDirectory, "verifiche")

try:
    shutil.rmtree(outPutDir, ignore_errors=True)  # DANGER !!!!!! - MAKE SURE YOU WANT TO DELETE oupPutDir
except FileNotFoundError:
    print("File {0} assente".format(outPutDir))

os.mkdir(outPutDir)  # crea ex nuovo

estraiBox = (0, 0, 1000, 240)  # taglia
newImageSize = (500, 120)       # resample

for root, dirs, files in os.walk(imageDirectory, topdown=False):
    for name in files:
        fileName = os.path.join(root, name)
        onlyName, extension = os.path.splitext(name)

        try:
            stazione, nomeStazione, annoStazione, progressivoStazione = onlyName.split("_")
            if int(progressivoStazione) % 2 == 1:
                newFileName = "_".join([stazione, nomeStazione, annoStazione, progressivoStazione, "sintesi.jpg"])
                newFileNameWithPath = os.path.join(root, outPutDir, newFileName)

                im = Image.open(fileName)
                newImage = im.crop(estraiBox)

                newImage.thumbnail(newImageSize, Image.ANTIALIAS)
                newImage.save(newFileNameWithPath, "JPEG")
                print(newFileNameWithPath)

        except ValueError:
            print("File nome non previsto: {}", onlyName)
