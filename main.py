from classes import *
from utils import *

def main():
    print("Привет! Найдем подходящую вакансию вместе на сайтах HH и Superjob!")
    job = input("Введите название профессии:\n>>> ")
    print("Отлично, начинаем поиск. Можем вместе наблюдать как обрабатываются данные")
    cleaning_json_file(job)
    print("Начинаем парсить сайт HH")
    parcing_page(job, 16, HH)
    print("Начинаем парсить сайт Superjob")
    parcing_page(job, 4, Superjob)
    list_jobs = read_json_file(job)
    print(f"Сбор данных закончен! Всего было найдено {len(list_jobs)} вакансий.")
    # while True:
    #     print("Выберите дальнейшее действие:\n"
    #           "1. Вывести топ 10 вакансий с самыми большими зарплатами.\n"
    #           "2. Вывести первые 10 вакансий.\n"
    #           "3. Вывести случайные 10 вакансий.\n"
    #           "4. Выйти.")
    #     user = input(">>> ")


if __name__ == '__main__':
    main()




# url = f"https://russia.superjob.ru/vacancy/search/?keywords=Python&page=1"
# FILE_NAME = "test.txt"
#
# def parse():
#     result_list = []
#     r = requests.get(f"https://russia.superjob.ru/vacancy/search/?keywords=python&page=1")
#     soup = BS(r.text, "html.parser")
#
#     names = soup.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
#     about = soup.find_all('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')
#     salary = soup.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')
#
#
#     for i in range(len(names)):
#         result_dict = {
#             'name': names[i].text,
#             'urls': 'russia.superjob.ru' + names[i].a['href'],
#             'salary': salary[i].text,
#             'description': about[i].text
#         }
#         result_list.append(result_dict)
#
#
#     count = 1
#     for i in result_list:
#         print(f"{count}: {i}")
#         count += 1
