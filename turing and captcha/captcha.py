import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import time

WIDTH = 220
HEIGHT = 100
CAPTCHA_LENGTH = 6


def generate_captcha_text(length=CAPTCHA_LENGTH):
    # Includes UPPERCASE + lowercase + digits
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))


def add_noise(draw):
    # Random lines
    for _ in range(5):
        draw.line(
            (
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT),
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT)
            ),
            fill="gray",
            width=1
        )

    # Random dots
    for _ in range(100):
        draw.point(
            (
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT)
            ),
            fill="black"
        )


def generate_captcha_image(text):
    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)

    for i, char in enumerate(text):
        x = 30 + i * 25 + random.randint(-5, 5)
        y = 30 + random.randint(-10, 10)
        draw.text((x, y), char, font=font, fill="black")

    add_noise(draw)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

    filename = "captcha_image.png"
    image.save(filename)
    return filename


def main():
    print("Generating CAPTCHA...\n")

    captcha_text = generate_captcha_text()
    image_file = generate_captcha_image(captcha_text)

    # Open image automatically (Windows)
    os.system(f'"{image_file}"')

    start_time = time.time()

    user_input = input("Enter CAPTCHA text: ")

    # Expiry check (2 minutes)
    if time.time() - start_time > 120:
        print("Captcha expired!")
        return

    if user_input == captcha_text:
        print(" CAPTCHA Verified Successfully!")
    else:
        print(" Incorrect CAPTCHA!")


if __name__ == "__main__":
    main()
