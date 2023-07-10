import requests
import time
from src.abstract_classes import JobParser
from src.config import API_SECRET_KEY
from http import HTTPStatus


class SuperJobAPI(JobParser):
    def get_vacancies(self, params):
        """Метод для получения вакансий в формате JSON"""

        headers = {
            "X-Api-App-Id": API_SECRET_KEY
        }
        for page in range(10):
            time.sleep(1)
            params = {
                "keyword": str(input()),
                "page": page,
                "per_page": "100"
            }
        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                params=params,
                                headers=headers)
        if not response.status_code == HTTPStatus.OK:
            return f'Ошибка! Статус-код: {response.status_code}'
        return response.json()['objects']

    def get_formatted_vacancies(self):
        vacancies = []
        for vacancy in self.get_vacancies('Python'):
            vacancies.append({
                'name': vacancy.get('profession'),
                'url': vacancy.get('link'),
                'salary': f'от {vacancy.get("payment_from")} до {vacancy.get("payment_to")}',
                'requirements': vacancy.get('experience')['title']
            }
            )
        return vacancies