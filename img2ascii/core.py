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


def img2ascii(file: str, scale: float = 0.25, moreLevels: bool = False, reverseLight: bool = False) -> str:

    if scale <= 0:
        raise ValueError("Scale must be greater than 0.")

    image = Image.open(file).convert('L')
    width, height = image.size

    image = image.resize((int(width * scale), int(height * scale)))
    width, height = image.size

    asciiArray = [''] * height
    reverse = 1 if not reverseLight else -1

    for j in range(height):
        y1, y2 = int(j), int((j+1))

        if j == height-1:
            y2 = height

        for i in range(width):
            x1, x2 = i, (i+1)

            if i == width-1:
                x2 = width

            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageColor(img))

            if moreLevels:
                gsval = complexGrayScale[::reverse][((avg*len(complexGrayScale))-1)//255]

            else:
                gsval = easyGrayScale[::reverse][((avg*len(easyGrayScale))-1)//255]

            asciiArray[j] += gsval

    return '\n'.join(asciiArray)
