import numpy as np
import matplotlib.pyplot as plt

# Učitavanje slike i pretvaranje u grayscale
img = plt.imread("tiger.png")
img = img[:,:,0].copy()

# a) Posvijetljivanje slike
brightened_img = np.clip(img + 50, 0, 255).astype(np.uint8)

# b) Rotacija slike za 90 stupnjeva u smjeru kazaljke na satu
rotated_img = np.rot90(img, k=-1)

# c) Zrcaljenje slike
flipped_img = np.fliplr(img)

# d) Smanjivanje rezolucije slike za 10 puta
downsampled_img = img[::10, ::10]

# e) Prikazivanje samo druge četvrtine slike po širini, a cijele slike po visini
h, w = img.shape
quarter_w = w // 4
cropped_img = np.zeros((h, w), dtype=np.uint8)
cropped_img[:, quarter_w:quarter_w*3] = img[:, quarter_w:quarter_w*3]
plt.imshow(cropped_img, cmap='gray')
plt.show()
