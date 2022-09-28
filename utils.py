import json

def cleaning_json_file(text: str) -> None:
    """
    Обнуляет файл при повторном запуске парсинга по той же вакансии.
    :param text:
    :return:
    """
    with open(f"{text}.json", "w", encoding="utf-8") as file:
        data = []
        json.dump(data, file, ensure_ascii=False, indent=2)


def read_json_file(text: str) -> list:
    with open(f"{text}.json", encoding="utf-8") as file:
        data = json.load(file)
        return data


def update_json_file(text: str, vacancy: list) -> None:
    with open(f"{text}.json", encoding="utf-8") as file:
        data = json.load(file)
        # if vacancy is not None:
        data.extend(vacancy)
        with open(f"{text}.json", "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


def parcing_page(text: str, num_page: int, website) -> None:
    """
    Парсит каждую страницу на нужном сайте и записывает в файл.
    """
    for num in range(1, num_page+1):
        site = website(text, num)
        vacancies = site.get_request()
        if vacancies is not None:
            print(f"Парсинг {num} страницы")
            update_json_file(text, vacancies)



