from PIL import Image

from avatars import get_image_via_url, generate_robohash_avatar
from draw_utils import round_corners, insert_image, add_text_centered

from config import *


def create_badge(name, surname, image_url, output_file=None):
    if output_file is None:
        output_file = f"{name} {surname}.png"

    image = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))

    border = Image.new("RGB", (WIDTH, HEIGHT), "#555555")
    border = round_corners(border, 70)
    image = insert_image(image, border)
    border = Image.new("RGB", (WIDTH - 2, HEIGHT - 2), "white")
    border = round_corners(border, 70)
    image = insert_image(image, border, (1, 1))

    if "impf" in image_url and USE_ROBOHASH_AVATARS:  # Проверка, что аватарки нет
        avatar = generate_robohash_avatar(f"{name} {surname}", AVATAR_SIZE[0])
    else:
        avatar = get_image_via_url(image_url, AVATAR_SIZE, AVATAR_SIZE)
        avatar = round_corners(avatar, AVATAR_RADIUS)

    image = insert_image(image, avatar, AVATAR_POS)

    image = add_text_centered(image,
                              name,
                              NAME_FONT_FILE,
                              NAME_FONT_SIZE,
                              NAME_COLOR,
                              NAME_X_START,
                              NAME_X_END,
                              NAME_Y)
    image = add_text_centered(image,
                              surname,
                              SURNAME_FONT_FILE,
                              SURNAME_FONT_SIZE,
                              SURNAME_COLOR,
                              NAME_X_START,
                              NAME_X_END,
                              SURNAME_Y)

    image.save(output_file)
