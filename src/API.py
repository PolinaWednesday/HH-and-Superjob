import requests
from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
from src import vacancies
from src.vacancies import Vacancy

load_dotenv()


class api(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJob(api):
    def get_vacancies(self, vacancies_str):
        api_url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {'X-Api-App-Id': os.getenv('API_SUPERJOB')}
        response = requests.get(api_url, headers=headers)
        vacancies = []
        if response.status_code == 200:
            for item in response.json()['objects']:
                    title = item['profession']
                    link = item['link']
                    salary = item['payment_to']
                    salary_from = item['payment_from']
                    city = item['town']['title']
                    company = item['firm_name']
                    vacancy = Vacancy(title, link, salary, salary_from, city, company)
                    vacancies.append(vacancy)
            vacancies_str = '\n'.join([str(vacancy) for vacancy in vacancies])
            return f"Вакансия SJ:\n{vacancies_str}\n"
        else:
            return 'Подключение к API SJ.ru не удалось!', response.status_code


class HandHut(api):
    def get_vacancies(self, vacancies_str):
        api_url = 'https://api.hh.ru/vacancies'
        headers = {'X-Api-App-Id': os.getenv('API_HANDHUT')}
        response = requests.get(api_url, headers=headers)
        vacancies = []
        if response.status_code == 200:
            for item in response.json()['items']:
                title = item['name']
                company = item['employer']['name']
                link = item['alternate_url']
                salary = item['salary']['to']
                salary_from = item['salary']['from']
                city = item['area']['name']
                vacancy = Vacancy(title, link, salary, salary_from, city, company)
                vacancies.append(vacancy)
            vacancies_str = '\n'.join(str(vacancy) for vacancy in vacancies)
            return f"Вакансия HH.ru:\n{vacancies_str}\n"
        else:
            return 'Подключение к API HH.ru не удалось!', response.status_code


if __name__ == "__main__":
    api1 = HandHut()
    print(api1.get_vacancies(vacancies))
    # api2 = SuperJob()
    # print(api2.get_vacancies(vacancies))