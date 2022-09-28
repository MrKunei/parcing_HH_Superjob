import json

def cleaning_json_file(text: str):
    with open(f"{text}.json", "w", encoding="utf-8") as file:
        data = []
        json.dump(data, file, ensure_ascii=False, indent=2)

def update_json_file(text: str, vacancy: list):
    with open(f"{text}.json", encoding="utf-8") as file:
        data = json.load(file)
        data.extend(vacancy)
        with open(f"{text}.json", "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


def parcing_page(text: str, num_page: int, website):
    vacancy_list = []
    for num in range(num_page):
        site = website(text, num)
        vacancies = site.get_request()

        for item in vacancies:
            vacancy_info = {
               "title": item['name'],
               "url": item['alternate_url'],
               "salary": item['salary'],
               "description": item['snippet']['responsibility']
                }
            vacancy_list.append(vacancy_info)
        print(f"Прошел парсинг {num+1} страницы")
    update_json_file(text, vacancy_list)



#
#
#
# def set_vacancy():
#     with open("jobs.txt", "a", encoding="utf-8") as f:
#         res = map(lambda item: item.strip().split(' | '), f)
#
#         for i in range(5):
#             vacancy = Vacancy(res[0],res[1], res[2], res[3])
#             print(vacancy)
#






# hh = HH("Python", 1)
# file_to_convert = hh.get_request()
#
# universal_file = {}
# universal_file_list = []
# for el in file_to_convert:
#     universal_file= {
#                 "name": el["name"],
#                 "salary": el["salary"],
#                 "url": el["alternate_url"],
#                 "description": el["snippet"]
#                  }
#     universal_file_list.append(universal_file)
#
# for i in universal_file_list:
#     print(i)