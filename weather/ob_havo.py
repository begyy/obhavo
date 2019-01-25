import requests
from bs4 import BeautifulSoup
__author__ = 'begyy'


class Obhavo:
    def __init__(self,city=None):
        self.input = city
        self.main_url = 'http://obhavo.uz/'
        self.urls = [
            'http://obhavo.uz/',
            'http://obhavo.uz/andijan',
            'http://obhavo.uz/bukhara',
            'http://obhavo.uz/jizzakh',
            'http://obhavo.uz/karshi',
            'http://obhavo.uz/navoi',
            'http://obhavo.uz/namangan',
            'http://obhavo.uz/nukus',
            'http://obhavo.uz/samarkand',
            'http://obhavo.uz/termez',
            'http://obhavo.uz/urgench',
            'http://obhavo.uz/ferghana',
            'http://obhavo.uz/khiva'
        ]

    def main(self):
        if self.input =='toshkent' or self.input == 'Toshkent':
            self.url = self.main_url
            return self.parsing()
        elif self.input == 'samarqand' or self.input == 'Samarqand':
            self.url = self.main_url + 'samarkand'
            return self.parsing()
        elif self.input == 'andijon' or self.input == 'Andijon':
            self.url = self.main_url + 'andijan'
            return self.parsing()
        elif self.input == 'buxoro' or self.input == 'Buxoro':
            self.url = self.main_url + 'bukhara'
            return self.parsing()
        elif self.input == 'jizzax' or self.input == 'Jizzax':
            self.url = self.main_url + 'jizzakh'
            return self.parsing()
        elif self.input == 'qarshi' or self.input == 'Qarshi':
            self.url = self.main_url + 'karshi'
            return self.parsing()
        elif self.input == 'navoi' or self.input == 'Navoi':
            self.url = self.main_url + 'navoi'
            return self.parsing()
        elif self.input == 'namangan' or self.input == 'Namangan':
            self.url = self.main_url + 'namangan'
            return self.parsing()
        elif self.input == 'nukus' or self.input == 'Nukus':
            self.url = self.main_url + 'nukus'
            return self.parsing()
        elif self.input == 'termiz' or self.input == 'Termiz':
            self.url = self.main_url + 'termez'
            return self.parsing()
        elif self.input == 'urganch' or self.input == 'Urganch':
            self.url = self.main_url + 'urgench'
            return self.parsing()
        elif self.input == 'fargona' or self.input == 'Fargona':
            self.url = self.main_url + 'ferghana'
            return self.parsing()
        elif self.input == 'xiva' or self.input == 'Xiva':
            self.url = self.main_url + 'khiva'
            return self.parsing()
        else:
            print("Bunday shahar yoq! Qayta urinib koring ")

    def parsing(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        day = soup.find('div', 'current-day')
        degree = soup.find('div', 'current-forecast')
        weather_info = soup.find('div', 'current-forecast-desc')
        city = soup.find('h2')
        description = soup.find('div', 'current-forecast-details')
        data = {
                "city": str(city.text),
                "day": str(day.text),
                "info": str(weather_info.text),
                "description": str(description.text),
                "degree": str(degree.text).replace('\n', '')
            }
        return data

    def all(self):
        array = []
        for i in self.urls:
            r = requests.get(i)
            soup = BeautifulSoup(r.text, 'html.parser')
            day = soup.find('div', 'current-day')
            degree = soup.find('div', 'current-forecast')
            weather_info = soup.find('div', 'current-forecast-desc')
            city = soup.find('h2')
            description = soup.find('div', 'current-forecast-details')
            array.append(
                {
                    "city": str(city.text),
                    "day": str(day.text),
                    "info": str(weather_info.text),
                    "description": str(description.text),
                    "degree": str(degree.text).replace('\n', '')
                }
            )
        return array