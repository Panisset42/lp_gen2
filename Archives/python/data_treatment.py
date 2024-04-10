# data_treatment.py
import unicodedata
import re


class City:
    month_dict = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio',
                  '06': 'Junho',
                  '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro',
                  '12': 'Dezembro'}
    actual_cities = []

    @classmethod
    def ini(cls):
        with open("Archives/Assets/Data/city.csv", "r", encoding="utf-8") as f:
            tmp_cities = f.readlines()
        for city in tmp_cities:
            if city.replace(",\n", "") != "":
                cls.actual_cities.append(city)

    @classmethod
    def city_cleaning(cls):
        pass

    @classmethod
    def active_generator(cls):
        pass

    @classmethod
    def city_register(cls, city, date):
        # starting the class
        cls.ini()
        # fixing date

        m, d, y = map(str, date.split("/"))
        if int(m) < 10:
            m = f"0{m}"
        if int(d) < 10:
            d = f"0{d}"
        y = f"20{y}"
        # generating the active campaign tag name
        cls.actual_cities.append(f"\n{city.strip()},{d}/{m}/{y},{d}/{m}/{y} - {city} - PALESTRA ABERTA")
        # writing the data
        with open("Archives/Assets/Data/city.csv", "w", encoding="utf-8") as f:
            f.writelines(cls.actual_cities)
        # reseting the variable
        cls.actual_cities.clear()

    @classmethod
    def remove_accents(cls, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

    @classmethod
    def input_generator(cls):
        header = "link,model,page_name,city,date,link_tk,active_name\n"
        data = [header]

        with open("Archives/Assets/Data/city.csv", "r", encoding="utf-8") as f:
            tmp = f.readlines()[1:]  # Skip the header line

        for line in tmp:
            city, date, model, link = map(str.strip, line.split(','))
            month, day, year = date.split('-')
            page_name = f"[{cls.month_dict[month][:3]}/{year}] [{model}] [{city}] PALESTRA ABERTA - AUTO".upper()
            link_tk = f"https://palestra.polozi.com.br/obg-{cls.remove_accents(city[:-5].strip().lower().replace(' ', '-').replace('/', '-'))}-{cls.month_dict[month][:3].lower()}"
            active_name = f"{day}/{month}/{year} - {city.lower()} - palestra aberta"
            content = f"{link},{model},{page_name},{city},{date},{link_tk},{active_name}\n"
            data.append(content)

        with open("Archives/Assets/Data/input.csv", "w", encoding="utf-8") as f:
            f.writelines(data)


class Model:
    @classmethod
    def ini(cls):
        pass


class Content:
    @classmethod
    def ini(cls):
        pass

    @classmethod
    def is_empty(cls, value):
        return not value or str(value).strip() == ""

    @classmethod
    def sanitize_input(cls, user_input):
        try:
            sanitized_input = re.sub(r"[\"'`,;]", "", str(user_input))
            sanitized_input = re.sub(r"[\\/]", "-", sanitized_input)
            return sanitized_input

        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
            return None
