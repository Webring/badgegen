import json

from drawer import create_badge


def main():
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    for user in users:
        name = user["name"]
        surname = user["surname"]
        image_url = user["img_url"]
        create_badge(name, surname, image_url,
                     output_file=f"badges/{name} {surname}.png")
        print(f"{name} {surname} готов!")


if __name__ == '__main__':
    main()
