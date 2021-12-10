import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def plot_countour_histogram(file_name: str):
    # Convert('L') convert image to grayscale
    pil_im = np.array(Image.open(file_name).convert('L'))

    # Contour plot
    plt.figure()
    plt.gray()
    plt.contour(pil_im, origin = 'image')
    plt.axis('equal')
    plt.axis('off')

    # Histogram plot
    plt.figure()
    plt.hist(pil_im.flatten(), 128)

    plt.show()
