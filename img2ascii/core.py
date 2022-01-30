import numpy as np
from PIL import Image

# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
complexGrayScale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,"^`\'. '

# 10 levels of gray
easyGrayScale = '@%#*+=-:. '


def getAverageColor(image: Image) -> object:
    '''
    Given PIL Image, return average value of grayscale color
    '''

    im = np.array(image)

    w, h = im.shape

    return np.average(im.reshape(w*h))


def img2ascii(file: str, width: int = 70, scale: float = 0.43, moreLevels: bool = False) -> str:

    if width < 1:
        raise ValueError("Width must be greater than 0.")

    if scale <= 0:
        raise ValueError("Scale must be greater than 0.")

    image = Image.open(file).convert('L')
    imgWidth, imgHeight = image.size

    columns = imgWidth//width
    ratio = columns/scale
    height = int(imgHeight//ratio)

    if width > imgWidth:
        width = imgWidth

    if height > imgHeight:
        height = imgHeight

    asciiArray = [''] * height

    for j in range(height):
        y1, y2 = int(j*ratio), int((j+1)*ratio)

        if j == height-1:
            y2 = imgHeight

        for i in range(width):
            x1, x2 = i*columns, (i+1)*columns

            if i == width-1:
                x2 = imgWidth

            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageColor(img))

            if moreLevels:
                gsval = complexGrayScale[((avg*len(complexGrayScale))-1)//255]

            else:
                gsval = easyGrayScale[((avg*len(easyGrayScale))-1)//255]

            asciiArray[j] += gsval

    return '\n'.join(asciiArray)
