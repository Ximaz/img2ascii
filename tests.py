import sys

from img2ascii import *

def usage():
    print("Usage :")
    print("python3 " + sys.argv[0] + " <FILENAME>")

def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    image = get_image(path=sys.argv[1])
    img_ascii = img2ascii(image=image, scale=0.5, detailed=True, reverse_light=True)
    with open("result.txt", "w+") as stream:
        stream.write(img_ascii)
    stream.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
