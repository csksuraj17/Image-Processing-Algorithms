import glob
from PIL import Image
i=0
for fil in glob.glob("/source/file/address/*"):
    image = Image.open(fil)
    gray_image = image.convert('L')
    gray_image.save('/destination/file/addresss/%d.jpg'%i)
    i+=1
