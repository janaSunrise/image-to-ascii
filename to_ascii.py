from PIL import Image

# -- Constants --
ASCII_CHARS = ["$", "@", "#", "S", "&", "%", "?", "*", "+", ";", ":", "~", "-", ",", "."]


# -- Utility functions --
def to_grayscale(image: Image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixels_to_ascii(image: Image) -> str:
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def resize_image(image: Image, new_width: int = 100) -> Image:
    width, height = image.size
    ratio = height / width

    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))

    return resized_image


def image_to_ascii(image: Image, new_width: int = 100) -> str:
    new_img = pixels_to_ascii(to_grayscale(resize_image(image, new_width=new_width)))

    pixel_count = len(new_img)
    ascii_image = "\n".join(
        [new_img[index:(index + new_width)] for index in range(0, pixel_count, new_width)]
    )

    return ascii_image
