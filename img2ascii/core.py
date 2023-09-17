import numpy as np
import PIL.Image

# http://paulbourke.net/dataformats/asciiart/

COMPLEX_GRAY_SCALE = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,"^`\'. '

EASY_GRAY_SCALE = '@%#*+=-:. '


def get_avg_color(image: PIL.Image.Image) -> int:
    return int(np.average(np.array(image)))

def get_image(path: str) -> PIL.Image.Image:
    return PIL.Image.open(path).convert('L')

def get_gray_scale(detailed: bool = True, reverse_light: bool = False):
    return (COMPLEX_GRAY_SCALE if detailed else EASY_GRAY_SCALE)[::(1 if not reverse_light else -1)]

def img2ascii(image: PIL.Image.Image, scale: float = 1, detailed: bool = True, reverse_light: bool = False) -> str:
    width, height = list(map(int, image.size[:2]))
    width, height = int(width * 2 * scale), int(height * scale)

    image = image.resize((width, height))

    buffer = [''] * height
    gray_scale = get_gray_scale(detailed=detailed, reverse_light=reverse_light)
    gray_scale_length = len(gray_scale)

    for j in range(height):
        y1, y2 = j, (j+1)

        if j == height - 1:
            y2 = height

        for i in range(width):
            x1, x2 = i, (i+1)

            if i == width - 1:
                x2 = width

            img = image.crop((x1, y1, x2, y2))
            avg = int(get_avg_color(img))

            gsval = gray_scale[(avg * gray_scale_length - 1) // 255]

            buffer[j] += gsval

    return '\n'.join(buffer)
