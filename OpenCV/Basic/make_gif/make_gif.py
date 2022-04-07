from PIL import Image
import cv2
import glob

images = [Image.open(img) for img in glob.glob('../make_gif/*.jpg')]



images = [img.convert('RGBA') for img in images]
images_one = images[0]

images_one.save('sixth.gif',format="GIF",append_images=images,save_all=True,duration=500,loop=0)

print(images)
print(images_one)