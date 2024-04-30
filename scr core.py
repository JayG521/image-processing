## image processing
# import PIL
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


## image object
pick.effect_spread(4)
nSize = (300, 190)
pick = pick.resize(nSize)
pick = pick.transpose(Image.Transpose.FLIP_TOP_BOTTOM)


# print(total)
##outputs
pick.show()

pick.save("lab-test-page-convert-test.png")
## preview