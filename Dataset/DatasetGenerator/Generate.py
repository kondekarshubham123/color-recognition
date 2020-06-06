import numpy as np
from PIL import Image
import random
import re

width = 150
height = 150
pixel = 3

array = np.zeros([height, width, pixel], dtype=np.uint8)

for i in range(1,25):
    array[:,:] = [random.randint(70,85) , 0, random.randint(120,140)]
    img = Image.fromarray(array)
    # img.save('Blue/colorBlue'+ str(i) +".png")
    # img.save('Red/colorRed'+ str(i) +".png")
    # img.save('Green/colorGreen'+ str(i) +".png")
    # img.save('Yellow/colorYellow'+ str(i) +".png")
    # img.save('Orange/colorOrange'+ str(i) +".png")
    # img.save('Indigo/colorIndigo'+ str(i) +".png")
    # img.save('Voilet/colorViolet'+ str(i) +".png")

array[:,:] = [255,255,0]
img = Image.fromarray(array)
img.save("Yellow/colorYellow2.png")