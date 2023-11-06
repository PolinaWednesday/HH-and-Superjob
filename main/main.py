from src.savers import *
from src.job_api import HeadHunterAPI, SuperJobAPI


def user_terminal():
    """Основная функция"""
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    print("Добро пожаловать!\n")

    while True:
        user_input = input(
            f"1. Поиск вакансий\n"
            f"2. Вывод списка вакансий\n"
            f"3. Удалить вакансию из списка\n"
            f"4. Завершение работы с программой\n"
            f"Ваш выбор: ")
        if user_input == '1':
            print()
            print(f'Вы выбрали раздел поиска вакансий.\n'
                  f'Для поиска вакансий введите ключевое слово:')
            keyword = input()
            print('Введите количество страниц, по которым будет осуществлен поиск:')
            pages = int(input())
            from_hh = hh_api.get_vacancies(keyword, pages)
            from_sj = superjob_api.get_vacancies(keyword, pages)
            print('Найденные вакансии на сайте "HeadHunter": \n')
            for vacancy in from_hh:
                print(vacancy)
            print('Найденные вакансии на сайте "SuperJob": \n')
            for vacancy in from_sj:
                print(vacancy)
            print('Хотите сортировать вакансии? Введите "да" или "нет"')
            user_input = input()
            if user_input == 'да' or user_input == 'yes':
                from_all = JSONSaver()
                from_all.add_vacancies(from_hh)
                from_all.add_vacancies(from_sj)
                from_all.sort_vacancies_by_salary()
                from_all.save_vacancies()
                print()
            elif user_input == 'нет' or user_input == 'no':
                from_all = JSONSaver()
                from_all.add_vacancies(from_hh)
                from_all.add_vacancies(from_sj)
                from_all.save_vacancies()
            else:
                print('Некорректный ввод')

        elif user_input == '2':
            print()
            vacancy_reader = JSONSaver()
            vacancy_reader.read_vacancies()
            print()
        elif user_input == '3':
            try:
                print()
                vacancy_remover = JSONSaver()
                vacancy_remover.remove_vacancies()
            except ValueError:
                print("Некорректный ввод")
                print()
        elif user_input == '4':
            print("Завершение работы с программой")
            break
        else:
            print("Некорректный ввод")
            print()


if __name__ == '__main__':
    user_terminal()
