import cv2
from math import gcd

"""

Image to ASCII art with openCV

"""

# TODO: Outputs are squashed, use better chars, delete last line for precision

imgPath = 'god.png'
img = cv2.cvtColor(cv2.imread(imgPath), cv2.COLOR_BGR2GRAY)
ht, wt = img.shape[:2]
PXL_SIZE = gcd(ht, wt)
ascii_img = []

for y in range(0, ht, PXL_SIZE):
    newRow = []
    for x in range(0, wt, PXL_SIZE):
        rowSum = 0
        for y_s in range(y, y + PXL_SIZE):
            for x_s in range(x, x + PXL_SIZE):
                rowSum += img[y_s][x_s]
        newRow.append(rowSum / PXL_SIZE ** 2)
    ascii_img.append(newRow)

colGrad = ('%', '+', '-', '.', ' ')
interval = 255 / len(colGrad)

with open('outputAscii.txt', 'w') as out_file:
    for row in ascii_img:
        for gCol in row:
            for m in range(len(colGrad)):
                if interval * m <= gCol <= interval * (m + 1):
                    out_file.write(colGrad[m] + ' ')

        out_file.write('\n')

