from sys import argv, exit
from img2ascii import img2ascii

def usage():
    print("Usage :")
    print("python3 " + argv[0] + " <FILENAME>")

def main():
    if len(argv) < 2:
        usage()
        exit(1)

    ascii = img2ascii(argv[1], width=215, reverseLight=1)
    with open("result.txt", "w+") as stream:
        stream.write(ascii)
    stream.close()
    exit(0)

if __name__ == "__main__":
    main()
