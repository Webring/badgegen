import json

from bs4 import BeautifulSoup


def save_users_to_json(input_file_path, output_file_path):
    data = []

    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")
        list_items = soup.find("div", {"class": "ChatSettingsMembersWidget__list"}).find_all("div", {
            "class": "ListItem__main"})
        for list_item in list_items:
            img = list_item.find("img")
            if img is not None:
                name, surname = list_item.find("div", {"class": "Entity__title"}).find("span").text.strip().split(" ",
                                                                                                                  1)
                img_url = list_item.find("img")["src"]
                user_data = {"name": name, "surname": surname, "img_url": img_url}
                data.append(user_data)

    with open(output_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    save_users_to_json("html/pm42.html", "users.json")
