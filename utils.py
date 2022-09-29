import json
from typing import Any

def cleaning_json_file(text: str) -> None:
    """
    Обнуляет файл при повторном запуске парсинга по той же вакансии.
    """
    with open(f"{text}.json", "w", encoding="utf-8") as file:
        data: list = []
        json.dump(data, file, ensure_ascii=False, indent=2)


def read_json_file(text: str) -> list:
    """
    Читает файл.
    """
    with open(f"{text}.json", encoding="utf-8") as file:
        data = json.load(file)
        return data


def update_json_file(text: str, vacancy: list) -> None:
    """
    Записывает файл с новыми данными.
    """
    with open(f"{text}.json", encoding="utf-8") as file:
        data = json.load(file)
        data.extend(vacancy)
        with open(f"{text}.json", "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


def parcing_page(text: str, website: Any) -> None:
    """
    Парсит каждую страницу на нужном сайте и записывает в файл.
    """
    for num in range(1, 10):
        site = website(text, num)
        vacancies = site.get_request()
        if not vacancies:
            break

        print(f"Парсинг {num} страницы")
        update_json_file(text, vacancies)



