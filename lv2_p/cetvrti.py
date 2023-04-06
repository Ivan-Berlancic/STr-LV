import numpy as np
import matplotlib.pyplot as plt

def checkerboard(square_size, num_squares_height, num_squares_width):
    # dimenzije slike
    height = square_size * num_squares_height
    width = square_size * num_squares_width

    # kreiranje polja crnih i bijelih kvadrata
    black_square = np.zeros((square_size, square_size))
    white_square = np.ones((square_size, square_size)) * 255

    # složenje crnih i bijelih kvadrata u jednu sliku
    rows = []
    for i in range(num_squares_height):
        row = []
        for j in range(num_squares_width):
            if (i+j) % 2 == 0:
                row.append(black_square)
            else:
                row.append(white_square)
        rows.append(np.hstack(row))
    img = np.vstack(rows)

    return img.astype(np.uint8)

# primjer korištenja funkcije
img = checkerboard(50, 8, 10)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
