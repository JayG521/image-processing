## image processing
import PIL
from PIL import Image

rope = [50, 22, 22, 22, 2, 10, 7]
total=0

for n in rope:
    total = total + 2*n


## import image
pick = Image.open("lab-test-page.jpg")

print(total)
## preview
pick.draft("L", (pick.width // 2, pick.height // 2))