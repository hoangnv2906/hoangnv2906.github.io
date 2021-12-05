import re
import json
from tqdm import tqdm
import codecs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Get path file input')
parser.add_argument('output', help='Get path file output')
args = parser.parse_args()


class Training_Data:

    def check_telephone(self: str) -> bool:
        """
        Выполняет проверку корректности номера телефона.

        Если формат телефонного номера отличается от "+7-(111)-222-33-44", то будет возвращено False

        Parameters
        ----------
        self : str
            Строка с проверяемым формата телефонного номера

        Returns
        -------
         bool:
            Булевый результат проверки на корректность
        """
        pattern = r"\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}"
        if re.match(pattern, self):
            return True
        else:
            return False

    def check_weight(self: int) -> bool:
        """
        Выполняет проверку корректности веса человека.

        если весы выходят за пределы разумного, то будет возвращено False

        Parameters
        ----------
        self : int
            Строка с проверяемым веса

        Returns
        -------
        bool:
            Булевый результат проверки на корректность
        """
        if self > 150 or self < 20:
            return False
        else:
            return True

    def check_inn(self: str) -> bool:
        """
        Выполняет проверку корректности СНИЛСа.

        если длина СНИЛС не соответсвует формату, то будет возвращено False

        Parameters
        ----------
        self : str
            Строка с проверяемым СНИЛС

        Returns
        -------
        bool:
            Булевый результат проверки на корректность
        """
        if len(self) != 12:
            return False
        else:
            return True

    def check_passport_number(self: str) -> bool:
        """
    Выполняет проверку корректности номера паспорта.

    если длина паспорта не соответсвует формату, то будет возвращено False

    Parameters
    ----------
      self : str
        Строка с проверяемым номера паспорта

    Returns
    -------
      bool:
        Булевый результат проверки на корректность
    """
        if len(self) != 6:
            return False
        else:
            return True

    def check_university(self: str) -> bool:
        """
        Выполняет проверку корректности университета.

        если университеты указаны неподходящие данные, то будет возвращено False

        Parameters
        ----------
        self : str
            Строка с проверяемым университета

        Returns
        -------
        bool:
            Булевый результат проверки на корректность
        """
        pattern = "^.+(?:[Уу]ниверситет)|([Уу]ниверситет)|^.+([Аа]кадеми[ия])|^.+(институт)|МГУ|^.+(" \
                  "политех)|^.+(" \
                  "МГТУ)|САУ|МФТИ|СПбГУ"
        if re.match(pattern, self):
            return True
        else:
            return False

    def check_age(self: int) -> bool:
        """
        Выполняет проверку корректности возраста.

        если возрасты выходят за пределы разумного, то будет возвращено False

        Parameters
        ----------
        self : int
            Строка с проверяемым возраста

        Returns
        -------
        bool:
            Булевый результат проверки на корректность
        """
        if self > 110 or self < 15:
            return False
        else:
            return True

    def check_academic_degree(self: str) -> bool:
        """
        Выполняет проверку корректности профессии.

        если профессии указаны неподходящие данные, то будет возвращено False

        Parameters
        ----------
        self : str
            Строка с проверяемым профессии

        Returns
        -------
        bool:
            Булевый результат проверки на корректность
        """

        pattern = "Бакалавр|Кандидат наук|Специалист|Магистр|Доктор наук"
        if re.match(pattern, self):
            return True
        else:
            return False

    def check_worldview(self: str) -> bool:
        """
        Выполняет проверку корректности мировоззрения.

        если мировоззрения указаны неподходящие данные, то будет возвращено False

        Parameters
        ----------
        self : str
            Строка с проверяемым мировоззрения

        Returns
        -------
        bool:
            Булевый результат проверки на корректность
        """
        pattern = "^.+(?:изм|анство)$"
        if re.match(pattern, self):
            return True
        else:
            return False

    def check_address(self: str) -> bool:
        """
        Выполняет проверку корректности адреса проживания.

         если адрес проживания указан не в формате "улица пробел номер дома", то будет возвращено False

        Parameters
        ----------
        self : str
            Строка с проверяемым университета

        Returns
        -------
        bool:
            Булевый результат проверки на корректность
        """
        pattern = r"[-а-яА-Я.]{1,15}\s|\d{1,5}"
        if re.match(pattern, self):
            return True
        else:
            return False


class work_with_file:
    """класс работает с файлами"""
    path: str

    def __init__(self, link: str) -> None:
        self.path = link

    def read(self: str) -> list:
        """функция читает файл"""
        with open(self, encoding="windows-1251") as file:
            text = json.load(file)
        return text

    def write(self: str, lst: list) -> list:
        """функция записывает данные в файл"""
        with codecs.open(self, "w", "utf-8") as myFile:
            json.dump(lst, myFile, ensure_ascii=False, indent=4)
        return myFile


mistake_address = 0
mistake_university = 0
mistake_age = 0
mistake_phone_number = 0
mistake_inn = 0
mistake_passport_number = 0
mistake_world_view = 0
mistake_academic_degree = 0
mistake_weight = 0

a = work_with_file
path = "14.txt"
data = a.read(path)
b = Training_Data

for i in data:
    if not b.check_telephone(i["telephone"]):
        mistake_phone_number += 1

for i in data:
    if type(i["weight"]) is not int:
        mistake_weight += 1
    else:
        if not b.check_weight(i["weight"]):
            mistake_weight += 1

for i in data:
    if not b.check_inn(i["inn"]):
        mistake_inn += 1

for i in data:
    if type(i["passport_number"]) != int:
        mistake_passport_number += 1
    else:
        string = str(i["passport_number"])
        if not b.check_passport_number(string):
            mistake_passport_number += 1

for i in data:
    if type(i["age"]) is not int:
        mistake_age += 1
    else:
        if not b.check_age(i["age"]):
            mistake_age += 1

for i in data:
    if not b.check_academic_degree(i["academic_degree"]):
        mistake_academic_degree += 1
    if not b.check_university(i["university"]):
        mistake_university += 1
    if not b.check_worldview(i["worldview"]):
        mistake_world_view += 1

for i in data:
    if not b.check_address(i["address"]):
        mistake_address += 1

myList = []
count = 0
for i in data:
    if (b.check_telephone(i["telephone"]) == True and b.check_inn(i["inn"]) == True
            and type(i["weight"]) is int and b.check_weight(i["weight"]) == True
            and type(i["age"]) is int and b.check_age(i["age"]) == True
            and b.check_academic_degree(i["academic_degree"]) == True
            and b.check_address(i["address"]) == True and b.check_university(i["university"]) == True
            and b.check_worldview(i["worldview"]) == True):
        if type(i["passport_number"]) is int:
            i["passport_number"] = str(i["passport_number"])
            if b.check_passport_number(i["passport_number"]):
                myList.append(i)
                count += 1
with tqdm(total=100) as progressbar:
    for j in range(5):
        a.write("output.txt", myList)
        progressbar.update(20)

print("Число валидных записей: ", count)
print("Общее число невалидных записей: ", len(data) - count)
print("Число невалидных записей по номерам телефоны:", mistake_phone_number)
print("Число невалидных записей по весам:", mistake_weight)
print("Число невалидных записей по СНИЛам:", mistake_inn)
print("Число невалидных записей по номерам паспорта:", mistake_passport_number)
print("Число невалидных записей по возрастам:", mistake_age)
print("Число невалидных записей по университетам:", mistake_university)
print("Число невалидных записей по мировоззрении:", mistake_world_view)
print("Число невалидных записей по учетным степеням:", mistake_academic_degree)
print("Число невалидных записей по адресам:", mistake_address)
