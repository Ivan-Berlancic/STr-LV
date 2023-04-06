import numpy as np
import matplotlib.pyplot as plt

def kvadrati_funkcija(vel_kvadrata, height, width):
    h = vel_kvadrata * height
    w = vel_kvadrata * width

    black = np.zeros((vel_kvadrata, vel_kvadrata))
    white = np.ones((vel_kvadrata, vel_kvadrata)) * 255

    redovi = []
    
    for i in range(height):
        red = []
        for j in range(width):
            if (i+j) % 2 == 0:
                red.append(black)
            else:
                red.append(white)
        redovi.append(np.hstack(red))
    img = np.vstack(redovi)
    return img.astype(np.uint8)
img = kvadrati_funkcija(50, 4, 5)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
