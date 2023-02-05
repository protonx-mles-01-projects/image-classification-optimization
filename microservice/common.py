import cv2
import numpy as np

def preprocess_image(image):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(224,224))
    img = np.reshape(img,(1,224,224,3))
    img = img/255.
    img = img.astype(np.float32)
    return img