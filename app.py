from random import shuffle
import cv2
import numpy as np

imgs = [
    'img/bears/1.jpg',
    'img/bears/2.jpg',
    'img/lions/1.jpg',
    'img/lions/2.jpg',
    'img/tigers/1.jpg',
    'img/tigers/2.jpg',
]
shuffle(imgs)

def normalize(imgs):
    '''Normalize BRG values in images to be between -1 and 1'''
    for img in imgs:
        im = cv2.imread(img)
        
        im = im / 112.5
        im -= 1

        yield (im, ''.join(imgs[0].split('/')[-2:]))

print(next(normalize(imgs)))