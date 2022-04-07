from immmm import build_montages
import imutils_path
import argparse
import random
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required =True,
                help = 'path of input directory of images')
ap.add_argument('-s','--sample',type=int,default=21,
                help='sample of images')

args = vars(ap.parse_args())

imagePath = list(imutils_path.list_images(args['image']))
random.shuffle(imagePath)
imagePath = imagePath[:args['sample']]

images = []

for image_path in imagePath:
    image = cv2.imread(image_path)
    images.append(image)
montages = build_montages(images,(150,200),(7,3))
for montage in montages:
    cv2.imshow("Montage",montage)
    cv2.imwrite('Montages.png',montage)
    cv2.waitKey(0)
