import numpy as np
import matplotlib.pyplot as plt


img = plt.imread("tiger.png")

print(img.shape)
print(img.dtype)
brig_img = img + 0.5
plt.figure()
plt.subplot(1, 5, 1)
plt.imshow(brig_img, cmap ="gray")

img2 = img[:,:,0].copy()
(h, w) = img2.shape
img_rot = np.zeros((w,h))
for i in range(0, h):
    img_rot[ :, h-1-i] = img2[i, : ]


plt.subplot(1, 5, 2)
plt.imshow(img_rot, cmap ="gray")


img_zrc = np.zeros((h,w))
for i in range(0, h):
    img_zrc[h-1-i, :] = img2[i, :]

plt.subplot(1, 5, 3)
plt.imshow(img_zrc, cmap ="gray")

img_res = img2[::10,::10]

plt.subplot(1, 5, 4)
plt.imshow(img_res, cmap ="gray")

img_zadnja = np.zeros((h,w))
for i in range(240, 480):
    img_zadnja[:,i] = img2[:,i]

plt.subplot(1, 5, 5)
plt.imshow(img_zadnja, cmap ="gray")
plt.show()
