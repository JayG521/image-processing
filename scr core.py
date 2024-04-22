## image processing
import PIL
from PIL import Image

'''
rope = [50, 22, 22, 22, 2, 10, 7]
total=0

for n in rope:
    total = total + 2*n
'''
## paper settings
emulsion = 0.5

luster = [222+emulsion, 210+emulsion, 206+emulsion]
canvas = [199+emulsion, 190+emulsion, 200+emulsion]
heavyCotton = [240+emulsion, 230+emulsion, 206+emulsion]
artPaper = [179+emulsion, 180+emulsion, 177+emulsion]


## import image
pick = Image.open("lab-test-page.jpg")

## print(total)
## preview
pick.draft("L", (pick.width // 2, pick.height // 2))