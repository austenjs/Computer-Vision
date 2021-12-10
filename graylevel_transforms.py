import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def graylevel_transforms(file_name : str):
    pil_im = np.array(Image.open(file_name).convert('L'))

    # Inverting image
    plt.figure()
    pil_im_2 = 255 - pil_im
    plt.imshow(pil_im_2)

    # Clamp from 100 - 200
    plt.figure()
    pil_im_3 = 100 + (100.0 / 255) * pil_im
    plt.imshow(pil_im_3)

    # Quadratic transformation
    plt.figure()
    pil_im_4 = 255.0 * (pil_im / 255.0) * pil_im
    plt.imshow(pil_im_4)

    plt.show()
