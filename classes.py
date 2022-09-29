from abc import ABC, abstractmethod
from bs4 import BeautifulSoup as BS
import requests
import re


class Engine(ABC):
    def __init__(self, text: str, num_page: int):
        self._text = text
        self._num_page = num_page

    @property
    def text(self):
        return self._text

    @property
    def num_page(self):
        return self._num_page

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):

    def get_request(self) -> list:
        """
        Получает данные с API и возвращает нужные поля.
        """
        par = {"text": self.text, 'area': '113', 'per_page': '50', 'page': self.num_page}
        response = requests.get(f"https://api.hh.ru/vacancies", params=par)
        res = response.json()['items']

        vacancies: list = []
        for item in res:
            description = f"{item['snippet']['responsibility']} " \
                          f"{item['snippet']['requirement']}"
            vacancy_info = {
                "title": item['name'],
                "url": item['alternate_url'],
                "salary": self.formate_salary(item['salary']),
                "description": self.formate_description(description)
            }
            vacancies.append(vacancy_info)
        return vacancies

    def formate_salary(self, salary: dict) ->list:
        """
        Форматирует данные по з.п. в список | переводит USD~RUR
        """
        if salary is None:
            return [0, '']
        if salary['from'] is None:
            return [0, '']
        if salary['currency'] == "USD":
            return [salary['from']*60, 'RUR']

        return [salary['from'], salary['currency']]

    def formate_description(self, description: str):
        """
        Форматирует описание
        """
        res = re.compile("<highlighttext>|<\/highlighttext>")
        return re.sub(res, "", description)


class Superjob(Engine):

    def get_request(self) -> list:
        """
        Парсит страницу через BS
        """
        par = {'keywords': self.text, 'page': self.num_page }
        url =  f"https://russia.superjob.ru/vacancy/search/"
        r = requests.get(url, params=par)
        soup = BS(r.text, "html.parser")

        names = soup.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
        about = soup.find_all('div', class_='_2d_Of _2J-3z _3B5DQ')
        salary = soup.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')

        result_list = []
        for i in range(len(names)):
            result_dict = {
                'title': names[i].text,
                'url': 'russia.superjob.ru' + names[i].a['href'],
                'salary': self.formate_salary(salary[i].text),
                'description': about[i].text
            }
            if result_dict is None:
                break
            result_list.append(result_dict)
        return result_list

    def formate_salary(self, salary: str) -> list:
        """
        Форматирует данные по з.п. в список
        """
        res = re.compile("от | | до|до |руб.")
        salary = re.sub(res, "",  salary)

        if "По договорённости" in salary:
            return [0, '']
        elif "—" in salary:
            salary = salary.split("—")
            return [int(salary[0]), 'RUR']
        else:
            return [int(salary), 'RUR']



class Vacancy():

    def __init__(self, title: str, urls: str, salary: list, description: str):
        self._title = title
        self._urls = urls
        self._salary = salary
        self._description = description

    @property
    def title(self) -> str:
        return self._title

    @property
    def urls(self) -> str:
        return self._urls

    @property
    def salary(self) -> str:
        if self._salary == [0, '']:
            return "По договорённости"
        else:
            return f"{self._salary[0]} {self._salary[1]}"

    @property
    def descriptoin(self) -> str:
        return self._description

    def __repr__(self) -> str:
        return f"Вакансия: {self.title}.\n" \
               f"Уровень дохода: {self.salary}.\n" \
               f"Ссылка: {self.urls}.\n" \
               f"Описание: {self.descriptoin}.\n"

