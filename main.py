import json

from drawer import create_pages


def main():
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    create_pages(users)


if __name__ == '__main__':
    main()
