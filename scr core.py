## image processing

roww = [50, 22, 22, 22, 2, 10, 7]
total=0

for n in roww:
    total = total + 2*n

from PIL import Image

## import image
pick = Image.open("lab-test-page.jpg")

print(total)
## preview