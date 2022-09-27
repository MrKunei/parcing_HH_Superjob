from abc import ABC, abstractmethod
import requests

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, text, num_page=8):
        self._text = text
        self._num_page = num_page

    @property
    def text(self):
        return self._text

    def get_request(self):
        vacancy_hh = []
        for num in range(self._num_page):
            par = {"text": self.text, 'per_page': '100', 'page': self._num_page}
            response = requests.get(f"https://api.hh.ru/vacancies", params=par)
            for i in response.json()["items"]:
                vacancy_hh.extend([{"title": i['name'],
                                   "salary": i['salary'],
                                   "link": i['alternate_url'],
                                   "description": i['snippet']['responsibility']}])
        return vacancy_hh


class Superjob(Engine):

    def get_request(self):
        with open("https://russia.superjob.ru/vacancy/search/?keywords=python") as f:
            contents = f.read()

class Vacancy():

    def __init__(self, name, urls, salary, description):
        self.name = name
        self.urls = urls
        self.salary = salary
        self.description = description

    def __repr__(self):
        return f"Вакансия: {self.name}" \
               f"Описание: {self.description}" \
               f"Уровень дохода: {self.salary}" \
               f"Ссылка: {self.urls}"

