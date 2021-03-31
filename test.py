import sys

import PIL

import to_ascii

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python test.py <IMAGE PATH>")

    _, path = sys.argv

    try:
        image = PIL.Image.open(path)
    except:
        print(f"{path} is not a valid path to an image.")
        sys.exit(1)

    ascii_img = to_ascii.image_to_ascii(image, 50)
    print(ascii_img)
