from io import BytesIO

import requests
from PIL import Image


def get_image_via_url(image_url, output_image_size=None, cs_size=None):
    if cs_size is None:
        cs_size = "300x300"
    elif isinstance(cs_size, tuple):
        cs_size = "{}x{}".format(*cs_size)

    replaced_image_url = _replace_url_params(image_url, {"cs": cs_size})

    response = requests.get(replaced_image_url, stream=True)
    image = Image.open(BytesIO(response.content)).resize(output_image_size)
    return image


def _replace_url_params(url, params_to_replace):
    base_url, params_string = url.split("?", 1)

    params_to_replace_keys = params_to_replace.keys()

    new_params = dict()

    for param in params_string.split("&"):
        key, value = param.split("=", 1)
        if key in params_to_replace_keys:
            value = params_to_replace[key]
        new_params[key] = value

    return f"{base_url}?{'&'.join([f'{key}={value}' for key, value in new_params.items()])}"


def generate_robohash_avatar(nickname, size=200):
    url = f"https://robohash.org/{nickname}.png?size={size}x{size}"

    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        print(f"Failed to fetch Robohash image. Status code: {response.status_code}")
        return None

