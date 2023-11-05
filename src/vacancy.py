class Vacancy:
    """Класс для хранения информации о вакансии"""

    def __init__(self, job_id, job_url, name, salary_from, salary_to, city):
        self.job_id = job_id
        self.job_url = job_url
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city

    def __eq__(self, other):
        """Функция сравнения двух вакансий"""
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        """Функция сравнения двух вакансий"""
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        """Функция сравнения двух вакансий"""
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """Функция сравнения двух вакансий"""
        return self.salary_from > other.salary_from

    def __le__(self, other):
        """Функция сравнения двух вакансий"""
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        """Функция сравнения двух вакансий"""
        return self.salary_from >= other.salary_from

    def __str__(self):
        """Функция представляющая вакансию в виде строки"""
        return f'id: {self.job_id}\n' \
               f'ссылка: {self.job_url}\n' \
               f'профессия: {self.name}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'зарплата до: {self.salary_to}\n' \
               f'город: {self.city}\n'

    def to_dict(self):
        """Функция представляющая вакансию в виде словаря"""
        return {
            'job_id': self.job_id,
            'job_url': self.job_url,
            'name': self.name,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'city': self.city
        }

    @staticmethod
    def from_dict(vacan_dict):
        """Функция создания вакансии из словаря"""
        return Vacancy(
            vacan_dict['job_id'],
            vacan_dict['job_url'],
            vacan_dict['name'],
            vacan_dict['salary_from'],
            vacan_dict['salary_to'],
            vacan_dict['city']
        )


class Vacancies:
    """Класс для хранения и обработки вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        """Функция добавления новых вакансий"""
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        """Функция удаления вакансий"""
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        """Функция сортировки вакансий по зарплате"""
        self.__all_vacancies.sort()
        self.__all_vacancies.sort(reverse=True)


    @property
    def all_vacancies(self):
        """Функция получения всех вакансий"""
        return self.__all_vacancies

    def to_list_dict(self):
        """Функция представляющая вакансии в виде списка словарей"""
        a = []
        for i in self.__all_vacancies:
            a.append(i.to_dict())
        return a