from scipy.ndimage.filters import gaussian_filter
import numpy as np
from imageio import imread, imsave

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype(np.uint8)


def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


s = imread('source.jpeg')
g=grayscale(s)
i = 255-g

b = gaussian_filter(i,sigma=10)
r= dodge(b,g)


imsave('result.png', r)
