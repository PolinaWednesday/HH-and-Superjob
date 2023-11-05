from src.savers import *
from src.job_api import HeadHunterAPI, SuperJobAPI


def user_terminal():
    """Основная функция"""
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    print("Добро пожаловать!\n")

    while True:
        user_input = input(
            f"1. Поиск вакансий по профессии\n"
            f"2. Вывод списка вакансий\n"
            f"3. Удалить вакансию\n"
            f"4. Выход\n"
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
            print('Хотите сортировать вакансии? Введите "да"')
            ans = input()
            if ans == 'да':
                from_all = JSONSaver()
                from_all.add_vacancies(from_hh)
                from_all.add_vacancies(from_sj)
                from_all.sort_vacancies_by_salary()
                from_all.save_vacancies()

        elif user_input == '2':
            print()
            vacancy_reader = JSONSaver()
            vacancy_reader.read_vacancies()
            print()
        elif user_input == '3':
            print("Хотите удалить вакансию?")
            userinput = input()
            if userinput == 'да':
                vacancy_remover = JSONSaver()
                vacancy_remover.remove_vacancies()
            else:
                exit()
        elif user_input == '4':
            print("Спасибо за использование!")


if __name__ == '__main__':
    user_terminal()
