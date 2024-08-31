from PIL import Image

from avatars import get_image_via_url, generate_robohash_avatar
from draw_utils import round_corners, insert_image, add_text_centered

from config import *


def create_badge(name, surname, image_url):
    image = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))

    border = Image.new("RGB", (WIDTH, HEIGHT), "#555555")
    border = round_corners(border, 70)
    image = insert_image(image, border)
    border = Image.new("RGB", (WIDTH - 2, HEIGHT - 2), "white")
    border = round_corners(border, 70)
    image = insert_image(image, border, (1, 1))

    if ("impf" in image_url and USE_ROBOHASH_AVATARS) or not image:  # Проверка, что аватарки нет
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

    return image


def create_pages(users):
    positions = [(65, 50), (1440, 50), (65, 715), (1440, 715), (65, 1380), (1440, 1380)]

    users_on_page = []
    page_image = Image.new("RGB", (2800, 1980), (255, 255, 255))

    page_id = 1

    for i, user in enumerate(users):
        name = user["name"]
        surname = user["surname"]
        image_url = user["img_url"]
        badge = create_badge(name, surname, image_url)
        badge.save(f"badges/{i + 1}. {name} {surname}.png")

        users_on_page.append(badge)
        if len(users_on_page) == 6 or i == len(users) - 1:
            for i in range(len(users_on_page)):
                page_image = insert_image(page_image, users_on_page[i], positions[i])
            page_image.save(f"pages/{page_id}.png")

            page_id += 1

            users_on_page.clear()
            page_image = Image.new("RGB", (2800, 1980), (255, 255, 255))

        print(f"{name} {surname} готов!")
