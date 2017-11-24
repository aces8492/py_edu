#5x5 pix prewitt-filter

import math
import copy

#image size
_HEIGHT = 5
_WIDTH = 5

#prewitt filter for 5x5 pixel image
def prewitt_filter(pixels):
    pixels_temp = copy.deepcopy(pixels)

    for i in range(1,_HEIGHT-1):
        for j in range(1,_WIDTH-1):
            sumrw = sumrh = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    sumrw += int(l * pixels_temp[(i+k)*_WIDTH+j+l])
                    sumrh += int(k * pixels_temp[(i+k)*_WIDTH+j+l])
            pixels[j+i*_WIDTH] = int(math.sqrt(sumrw * sumrw + sumrh * sumrh)) 

    return pixels


#print pixels
def print_pixels(pixels):
    for i in range(0,_HEIGHT*_WIDTH):
        if i != 0 and i % _WIDTH == 0:
            print()
        print("{0}\t".format(pixels[i]),end="")
    print()

    # print(pixels[i] for i in range(0,_HEIGHT*_WIDTH))

#initialize image pix
pixels = [j if i % 2 != 0 else 0 if j % 2 == 0 else 1 for i in range(0,_HEIGHT) for j in range(0,_WIDTH)]

#print
print("before")
print_pixels(pixels)
print("after")
prewitt_pixels = prewitt_filter(pixels)
print_pixels(prewitt_pixels)


