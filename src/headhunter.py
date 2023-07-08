import requests
from src.abstract_classes import JobParser
from http import HTTPStatus


class HeadHunterAPI(JobParser):
    def get_vacancies(self, params: str):
        """Метод для получения вакансий в формате JSON"""

        response = requests.get(f'https://api.hh.ru/vacancies?text={params}')
        if not response.status_code == HTTPStatus.OK:
            return f'Ошибка! Статус-код: {response.status_code}'
        return response.json()['items']

    def get_formatted_vacancies(self):
        vacancies = []
        for vacancy in self.get_vacancies('Python'):
            vacancies.append({
                'name': vacancy.get('name'),
                'url:': vacancy.get('alternate_url'),
                'salary': vacancy.get('salary'),
                'requirements': vacancy.get('experience')['name']
            })

        return vacancies