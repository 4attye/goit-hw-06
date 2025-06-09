import matplotlib.pyplot as plt
import numpy as np


image = "karta-metro-kiev.png"
image = plt.imread(image)
height, width = image.shape[0], image.shape[1]
plt.figure(figsize=(16, 10))
plt.imshow(image)
tick_spacing = 40
plt.xticks(np.arange(0, width, tick_spacing))
plt.yticks(np.arange(0, height, tick_spacing))
plt.grid(True)
plt.show()