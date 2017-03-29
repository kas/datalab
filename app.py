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
shuffle(imgs) # randomize imgs list

def normalize(imgs):
    '''Normalize BRG values in images from [0, 255] to [-1, 1]'''
    for img in imgs:
        im = cv2.imread(img)
        
        im = im / 127.5 # [0, 2]
        im -= 1 # [-1, 1]

        yield (im, ''.join(img.split('/')[-2:]))

normalized_imgs = normalize(imgs)

for normalized_img in normalized_imgs:
    print(normalized_img)