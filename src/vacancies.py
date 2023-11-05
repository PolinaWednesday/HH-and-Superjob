
from dotenv import load_dotenv


load_dotenv()


class UrlError(Exception):
    """Класс ошибки в URL адресе"""

    def __init__(self, msg):
        super.__init__(msg)


class Vacancy:
    """Класс для создания экземпляров вакансий и работы с ними"""
    __slots__ = {'title', 'link', 'salary', 'salary_from', 'city', 'company'}

    def __init__(self, title: str, link: str, salary: int, salary_from: int, city: str, company: str):
        self.title = title
        if self.title is None:
            raise AttributeError('Поле не может быть пустым')
        self.link = link
        if self.link is None:
            raise AttributeError('Поле не может быть пустым')
        self.salary = salary
        if self.salary is None or self.salary == 0:
            self.salary = '-'
        self.salary_from = salary_from
        if self.salary_from is None or self.salary_from == 0:
            self.salary_from = '-'
        self.city = city
        if self.city is None:
            raise AttributeError('Поле не может быть пустым')
        self.company = company
        if self.company is None:
            raise AttributeError('Поле не может быть пустым')


    def __str__(self):
        return f'Название вакансии - {self.title}\n' \
               f'Ссылка - {self.link}\n' \
               f'З/п от {self.salary_from} RUB до {self.salary} RUB\n' \
               f'Город - {self.city}\n' \
               f'Компания - {self.company}\n'

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary
