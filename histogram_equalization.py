import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def histeq(image, number_of_bins = 256):
    histogram, bins = np.histogram(image.flatten(), number_of_bins)
    cdf = histogram.cumsum()
    cdf = 255 * cdf / cdf[-1]

    new_image = np.interp(image.flatten(), bins[:-1], cdf)

    return new_image.reshape(image.shape)
