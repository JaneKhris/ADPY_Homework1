from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from litresapi import LitresApi
# from pprint import pprint


if __name__ == '__main__':

    calculate_salary()
    get_employees()
    print(datetime.now())

    with open('data/litres_login.txt', 'r') as file_object:
        login = file_object.read().strip()

    with open('data/litres_password.txt', 'r') as file_object:
        password = file_object.read().strip()

    api = LitresApi(secret_key=password, partner_id=login)
    genres = api.get_genres()
    print(genres[0])