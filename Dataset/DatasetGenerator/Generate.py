import numpy as np
from PIL import Image
import random
import re


class Generator():
    width = 150
    height = 150
    pixel = 3

    def __init__(self,color,height=height,width=width,pixel=pixel):
        self.IPcolor = color
        self.lookup = {}
        self.look = {}
        self.color = []
        self.Gen = []
        self.rgb = []
        self.array = np.zeros([height, width, pixel], dtype=np.uint8)

    def setRGB(self):
        fil = open("RGBRange")
        fil.readline()
        for line in fil.readlines():
            rawLi = re.findall("|.*|",line)[1].split('|')
            self.color.append(rawLi[0].strip()),self.Gen.append(rawLi[1].strip()),self.rgb.append(rawLi[2].strip())
        fil.close()
        for col,ge in list(zip(self.color,self.Gen)):
            self.lookup[col] = ge
        # return self.lookup[self.IPcolor]


    def sample(self):
        for col,sam in list(zip(self.color,self.rgb)):
            self.look[col] = sam
        exec('self.var = ' + self.look[self.IPcolor])
        self.array[:,:] = self.var
        img = Image.fromarray(self.array)
        img.save("../test/"+self.IPcolor+"/"+self.IPcolor+'-!-'+"Sample" +".png")

    def GenerateData(self,val):
        for i in range(0,val):
            exec('self.var = ' + self.lookup[self.IPcolor])
            self.array[:,:] = self.var
            img = Image.fromarray(self.array)
            img.save("../test/"+self.IPcolor+"/"+self.IPcolor+'-!-'+str(i) +".png")



# Choose color = [Blue ,Red ,Orange ,Green ,Voilet ,Indigo ,Yellow]

Color1 = Generator("Red")
Color2 = Generator("Green")
Color3 = Generator("Blue")
Color4 = Generator("Orange")
Color5 = Generator("Voilet")
Color6 = Generator("Indigo")
Color7 = Generator("Yellow")

for i in range(1,8):
    exec("Color"+str(i)+".setRGB()")
    exec("Color"+str(i)+".sample()")
    exec("Color"+str(i)+".GenerateData(25)")


# Color1.setRGB() 
# Color2.setRGB()
# Color3.setRGB()
# Color4.setRGB()
# Color5.setRGB()
# Color6.setRGB()
# Color7.setRGB()

# Color1.sample()
# Color2.sample()
# Color3.sample()
# Color4.sample()
# Color5.sample()
# Color6.sample()
# Color7.sample()


# Color1.GenerateData(25)
# Color2.GenerateData(25)
# Color3.GenerateData(25)
# Color4.GenerateData(25)
# Color5.GenerateData(25)
# Color6.GenerateData(25)
# Color7.GenerateData(25)
