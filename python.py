from PIL import Image, ImageFilter
import os
import numpy
import matplotlib
from PIL import ImageEnhance


#Supreme Modified
image1 = Image.open('supreme.jpg')
image1.rotate(10, expand = True)
greyscale_image1 = image1.convert('L')

image1 = image1.filter(ImageFilter.EMBOSS)
image1 = image1.filter(ImageFilter.MinFilter(3))
image1= image1.filter(ImageFilter.MinFilter)
image1.save('supreme_mod4.jpg')



#Bike Modified
'''
#Bike Modified
image1 = Image.open('Bike.png')
enhancer = ImageEnhance.Sharpness(image1)
for i in range(8):
    factor = i / 4.0
    enhancer.enhance(factor).show("Sharpness %f" % factor)
image1.convert(mode = 'L')
image1.filter(ImageFilter.GaussianBlur(10)).save('Bike_mod.png')


image1.convert(mode = 'L').save('Bike_mod.png')
image1 = Image.open('Bike.png')
image1.filter(ImageFilter.GaussianBlur(15)).save('Bike_mod.png')
image1 = Image.open('Bike.png')
image1.rotate(180).save('Bike_mod.png')
'''


#Black and White
'''
image1 = Image.open('Bike.png')
image1.convert(mode = 'L').save('Bike_mod.png')
'''


#Rotate
'''
image1 = Image.open('Bike.png')
image1.rotate(90).save('Bike_mod.png')
'''


#Save as PNG
'''
#Save as PNG
size_300 = (300,300)

size_700 = (700, 700)
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))
'''
      
        


