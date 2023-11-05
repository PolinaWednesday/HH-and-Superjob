import requests
from src.vacancy import Vacancy
from dotenv import load_dotenv
import os



class JobAPI:
    """Абстрактный класс для хранения информации из API"""
    def __init__(self):
        pass

    def get_vacancies(self, name_job):
        pass


class HeadHunterAPI(JobAPI):
    "Класс для хранения информации из API с сайта HH"

    def __init__(self):
        super().__init__()
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name_job, pages):
        "Хранение вакансий в привычном виде"
        url = self.url
        ans = []
        for i in range(pages):
            par = {'text': name_job, 'per_page': '3', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            for j in e['items']:
                job_id = str(j['id'])
                job_url = j['alternate_url']
                name = j['name']
                if not ((j['salary'] is None) or (j['salary']['from'] is None)):
                    salary_from = j['salary']['from']
                    salary_to = j['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                if not (j['address'] is None):
                    city = j['address']['city']
                else:
                    city = None
                vacanc = Vacancy(job_id, job_url, name, salary_from, salary_to, city)
                ans.append(vacanc)
        return ans


class SuperJobAPI(JobAPI):
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.api_kay = os.getenv('API_SUPERJOB')

    def get_vacancies(self, name_job, pages):
        url = self.url
        ans = []
        head = {'Host': 'api.superjob.ru',
                'X-Api-App-Id': self.api_kay
                }
        for i in range(pages):
            par = {'keyword': name_job, 'count': 3, 'page': i}
            r = requests.get(url, params=par, headers=head)
            e = r.json()
            for j in e['objects']:
                job_id = str(j['id'])
                job_url = j['link']
                name = j['profession']
                salary_from = j['payment_from']
                salary_to = j['payment_to']
                if j['address'] is None:
                    city = None
                else:
                    city = j['address'].split(',')[0]
                vacanc = Vacancy(job_id, job_url, name, salary_from, salary_to, city)
                ans.append(vacanc)
        return ans