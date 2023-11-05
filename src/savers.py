from abc import ABC, abstractmethod
from src.vacancy import Vacancy, Vacancies
import json


class Saver(ABC):
    """Абстрактный класс для редактирования и обработки списка вакансий"""

    @abstractmethod
    def save_vacancies(self):
        pass

    def read_vacancies(self):
        pass


class JSONSaver(Vacancies, Saver):
    """Класс для обработки списка вакансий в JSON формате"""

    def save_vacancies(self):
        """Сохранение вакансий в JSON формате"""
        with open('vacancies.json', 'w', encoding='utf-8') as fh:
            json.dump(self.to_list_dict(), fh, indent=4, ensure_ascii=False)

    def read_file(self):
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def read_vacancies(self):
        data = self.read_file()
        for i, item in enumerate(data):
            print(f"{i + 1}. {item['name']}")
        print()

    def remove_vacancies(self):
        """Удаление вакансий из JSON фойла"""
        # Открываем файл JSON
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Выводим список job_id для выбора пользователем
        for i, item in enumerate(data):
            print(f"{i + 1}. {item['job_id']}")

        # Получаем от пользователя индекс словаря для удаления
        index_to_remove = int(input("Введите номер словаря для удаления: ")) - 1

        # Проверяем введенный индекс на корректность
        if index_to_remove < 0 or index_to_remove >= len(data):
            print("Некорректный номер словаря.")
            return

        # Удаляем выбранный словарь
        removed_dict = data.pop(index_to_remove)
        print("Удаленный словарь:")
        print(removed_dict)

        # Записываем обновленные данные обратно в файл JSON
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
