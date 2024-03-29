import cv2
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from matplotlib.image import imread


i = imread('luffy.png')

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


if (len(i.shape) == 3):
    i = rgb2gray(i)

i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

filter = [[-1, -2, -1], [0,0,0],[1,2,1]]
weight = 1

for x in range(1,size_x -1):
    for y in range(1, size_y-1):
        output_pixel = 0.0
        output_pixel = output_pixel + (i[x - 1, y-1] * filter[0][0])
        output_pixel = output_pixel + (i[x, y-1] * filter[0][1])
        output_pixel = output_pixel + (i[x + 1, y-1] * filter[0][2])
        output_pixel = output_pixel + (i[x-1, y] * filter[1][0])
        output_pixel = output_pixel + (i[x, y] * filter[1][1])
        output_pixel = output_pixel + (i[x+1, y] * filter[1][2])
        output_pixel = output_pixel + (i[x-1, y+1] * filter[2][0])
        output_pixel = output_pixel + (i[x, y+1] * filter[2][1])
        output_pixel = output_pixel + (i[x+1, y+1] * filter[2][2])
        output_pixel = output_pixel * weight
        if (output_pixel < 0):
            output_pixel = 0
        if (output_pixel > 255):
            output_pixel = 255
        i_transformed[x,y] = output_pixel


new_x = int(size_x/2)
new_y = int(size_y/2)
newImage = np.zeros((new_x, new_y))
print(new_x, new_y)
for x in range(0, size_x -1, 2):
    for y in range(0,size_y-1, 2):
        pixels = []
        pixels.append(i_transformed[x,y])
        pixels.append(i_transformed[x+1, y])
        pixels.append(i_transformed[x, y+1])
        pixels.append(i_transformed[x+1, y+1])
        pixels.sort(reverse=True)
        newImage[int(x/2), int(y/2)] = pixels[0]

print(newImage.shape)
# PLot the image
plt.gray()
plt.grid(False)
plt.imshow(newImage)
plt.show()