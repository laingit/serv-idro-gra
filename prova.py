from PIL import Image
import os

infile = r"E:\_pytest\88_Putifigari_2014_0001.jpg"
im = Image.open(infile)
print(im.format, im.size, im.mode)

box = (0, 0, 1000, 240)  # taglia
size = (250, 60)         # resample
region = im.crop(box)

outfile = os.path.splitext(infile)[0] + "_sezione.jpg"
if infile != outfile:
    try:
        region.thumbnail(size, Image.ANTIALIAS)
        region.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for", infile)
