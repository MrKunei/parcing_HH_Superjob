from abc import ABC, abstractmethod
import requests
import re

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, text, num_page=16):
        self._text = text
        self._num_page = num_page

    @property
    def text(self):
        return self._text

    def num_page(self):
        return self._num_page

    def get_request(self):
        vacancy_hh = []
        for num in range(self._num_page):
            par = {"text": self.text, 'per_page': '50', 'page': self._num_page}
            response = requests.get(f"https://api.hh.ru/vacancies", params=par)

            for i in response.json()['items']:
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

    def __init__(self, title, urls, salary, description):
        self._title = title
        self._urls = urls
        self._salary = salary
        self._description = description

    @property
    def title(self):
        return self._title

    @property
    def urls(self):
        return self._urls
    @property
    def salary(self):
        if self._salary:
            return f" {self._salary['from']} - {self._salary['to']}"
        else:
            return "не указано"
    @property
    def descriptoin(self):
        res = re.compile("<highlighttext>|<\/highlighttext>")
        description = re.sub(res, "", self._description)
        return description

    def __repr__(self):
        return f"Вакансия: {self.title}.\n" \
               f"Уровень дохода: от{self.salary}.\n" \
               f"Ссылка: {self.urls}.\n" \
               f"Описание: {self.descriptoin}.\n"

