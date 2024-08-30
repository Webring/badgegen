from PIL import Image, ImageDraw, ImageFilter, ImageFont


def round_corners(image, radius):
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)

    draw.rounded_rectangle(
        [(0, 0), image.size],
        radius=radius,
        fill=255
    )

    rounded_image = image.copy()
    rounded_image.putalpha(mask)

    return rounded_image


def insert_image(background, overlay, position=(0, 0)):
    background.paste(overlay, position, overlay.convert("RGBA").getchannel('A') if overlay.mode == 'RGBA' else None)
    return background


def add_text_centered(image, text, font_path, font_size, text_color, x_start, x_end, y):
    image = image.convert("RGBA")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font_path, font_size)

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]

    x = x_start + (x_end - x_start - text_width) / 2

    draw.text((x, y), text, font=font, fill=text_color)

    return image

