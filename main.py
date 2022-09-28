from classes import *
from utils import *
from random import choices

def main():
    print("Привет! Найдем подходящую вакансию вместе на сайтах HH и Superjob!")
    job = input("Введите название профессии:\n>>> ")
    print("Отлично, начинаем поиск. Можем вместе наблюдать как обрабатываются данные")
    cleaning_json_file(job)
    print("Начинаем парсить сайт HH")
    parcing_page(job, 17, HH)
    print("Начинаем парсить сайт Superjob")
    parcing_page(job, 3, Superjob)
    print(f"Сбор данных закончен!\nВсего было найдено {len(read_json_file(job))} вакансий.\n")
    while True:
        print("Выберите № дальнейшего действия:\n"
              "1. Вывести топ 10 вакансий с самыми большими зарплатами.\n"
              "2. Вывести первые 10 вакансий.\n"
              "3. Вывести случайные 10 вакансий.\n"
              "4. Выйти.")
        user = int(input(">>> "))
        if user == 1:
            list = sorted(read_json_file(job), key=lambda v: v['salary'][0], reverse=True)
            res = list[:10]
            for r in res:
                vacancy = Vacancy(r['title'], r['url'], r['salary'], r['description'])
                print(vacancy)
        if user == 2:
            res = read_json_file(job)[:10]
            for r in res:
                print(Vacancy(r['title'], r['url'], r['salary'],
                              r['description']))
        if user == 3:
            res = choices(read_json_file(job), k=10)
            for r in res:
                print(Vacancy(r['title'], r['url'], r['salary'],
                              r['description']))
        if user == 4:
            break


if __name__ == '__main__':
    main()




