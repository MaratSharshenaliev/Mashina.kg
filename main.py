import time
from typing import List, TypedDict

import requests
from bs4 import BeautifulSoup, Tag


class Car:
    def __init__(self, uuid=None, name=None, price=None, year=None, engine=None, body_type=None, additional_info=None,
                 time_added=None, url_image=None):
        self.__uuid = uuid
        self.__name = name
        self.__price = price
        self.__year = year
        self.__engine = engine
        self.__body_type = body_type
        self.__additional_info = additional_info
        self.__time_added = time_added
        self.__url_image = url_image

    def __str__(self):
        return "Car<id=%s name=%s price=%s>" % (self.__uuid, self.__name, self.__price)

    def get_name(self):
        return self.__name

    def get_image_url(self):
        return self.__url_image

    def get_message(self):
        message = f"""
        {self.__name} | {self.__price}
-----------------------
{self.__year} | {self.__engine}
{self.__additional_info},{self.__body_type}
"""
        return message

    def get_id(self):
        return self.__uuid


class MashinaAPI:
    EVERY = 1
    CHAT_ID = "-4094474720"
    TELEGRAM_PATH = "https://api.telegram.org/bot6787736415:AAHo6wi9mEx4AhM3_VOtiah_5bGsI1F7Tdg/sendPhoto"

    def __init__(self, url, *args, **kwargs):
        self.__show_box: List[Car] = []
        self.url = url
        self.session = requests.Session()

    def send_emal(self, message):
        pass

    def send_telegram(self, instanc: Car):
        message = instanc.get_message()
        photo = instanc.get_image_url()
        data = {
            'chat_id': self.CHAT_ID,
            'photo': photo,
            'caption': message
        }
        self.session.post(self.TELEGRAM_PATH, data=data)

    def main_loop(self):
        while True:
            time.sleep(self.EVERY)
            response = self.session.get(self.url)
            html_wrapper: List[Tag] = self.__get_list_items(response.text)

            for item in html_wrapper:
                instance_car = self.__get_car_by_html(item)
                if instance_car and self.__check_car_in_show_box(instance_car.get_id()):
                    self.send_telegram(instance_car)
                    self.__show_box.append(instance_car)
                    self.__check_show_box()

    def __check_car_in_show_box(self, uuuid):
        for elem in self.__show_box:
            if elem.get_id() == uuuid:
                return False

        return True

    def __check_show_box(self):
        if len(self.__show_box) > 10:
            self.__show_box.pop(0)

    def __get_car_by_html(self, item):
        try:
            name = item.find(name="h2", attrs={"class": "name"}).text.strip()
            price = item.find(name='div', class_='block price').find("strong").find_next("br").next_sibling.text.strip()
            year = item.find('p', class_='year-miles').find('span').text.strip()
            engine = item.find('p', class_='year-miles').text.split(',')[1].strip()
            body_type = item.find('p', class_='body-type').text.strip()
            additional_info = item.find('p', class_='volume').text.strip()
            time_added = item.find('div', class_='block city').find('span', class_='date').text.strip()
            image_url = item.find('div', class_='thumb-item-carousel').find("img", class_="lazy-image-attr").get("src")

            if "сек" not in time_added:
                return None

            uuid = self.__generate_uuid(
                name,
                price,
                year,
                engine
            )
            return Car(uuid, name, price, year, engine, body_type, additional_info, time_added, image_url)
        except Exception as e:
            return None

    @staticmethod
    def __generate_uuid(*args):
        primary_key: str = ""
        for iteration in args:
            primary_key += str(iteration)

        return primary_key.replace(" ", "")

    @staticmethod
    def __get_list_items(text):
        try:
            soup = BeautifulSoup(text, "html.parser")
            return soup.findAll(name="div", attrs={"class": ["list-item", "list-label"]})
        except None:
            return []


if __name__ == "__main__":
    BASE_API = "https://www.mashina.kg/search/all/all/?currency=1&price_from=10000&price_to=260000&sort_by=upped_at+desc&time_created=1&page=1"
    instance = MashinaAPI(BASE_API)
    instance.main_loop()
