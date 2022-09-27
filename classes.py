from abc import ABC, abstractmethod
from bs4 import BeautifulSoup as BS
import requests
import re


class Engine(ABC):
    def __init__(self, text, num_page):
        self._text = text
        self._num_page = num_page

    @property
    def text(self):
        return self._text

    @property
    def num_page(self):
        return

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):

    def get_request(self):
        par = {"text": self.text, 'per_page': '50', 'page': self.num_page}
        response = requests.get(f"https://api.hh.ru/vacancies", params=par)
        return response.json()['items']



class Superjob(Engine):

    def get_request(self):
        result_list = []
        url =  f"https://russia.superjob.ru/vacancy/search/?keywords={self.text}&page={self.num_page}"
        r = requests.get(url)
        soup = BS(r.text, "html.parser")

        names = soup.find_all('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')
        about = soup.find_all('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')
        salary = soup.find_all('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')

        for i in range(len(names)):
            result_dict = {
                'name': names[i].text,
                'urls': 'russia.superjob.ru' + names[i].a['href'],
                'salary': salary[i].text,
                'description': about[i].text
            }
            result_list.append(result_dict)
        return result_list

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
            return f"{self._salary['from']} - {self._salary['to']}"
        else:
            return "не указано"
    @property
    def descriptoin(self):
        # res = re.compile("<highlighttext>|<\/highlighttext>")
        # self._description = re.sub(res, "", self._description)
        return self._description

    def __repr__(self):
        return f"Вакансия: {self.title}.\n" \
               f"Уровень дохода: {self.salary}.\n" \
               f"Ссылка: {self.urls}.\n" \
               f"Описание: {self.descriptoin}.\n"

