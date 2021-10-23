from Classification_human_orr_horse import model
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from keras.preprocessing import image
import numpy as np
import cv2
filename="myTf1.sav"
model=pickel.load(open(filename,'rb'))
Tk().withdraw() 
filename = askopenfilename() 
print(filename)
img = image.load_img(filename, target_size=(200, 200))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images, batch_size=10)
print(classes[0])
