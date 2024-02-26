#data_treatment.py

class City:
    actual_cities = []
    @classmethod
    def ini(cls):
        with open("Archives/Assets/Data/city.csv","r", encoding="utf-8") as f:
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
        #starting the class
        cls.ini()
        #fixing date

        m, d, y = map(str, date.split("/"))
        if int(m) < 10:
            m = f"0{m}"
        if int(d) < 10:
            d = f"0{d}"
        y = f"20{y}"
        #generating the active campaign tag name
        cls.actual_cities.append(f"\n{city.strip()},{d}/{m}/{y},{d}/{m}/{y} - {city} - PALESTRA ABERTA")
        print(cls.actual_cities)
        #writing the data
        with open("Archives/Assets/Data/city.csv","w", encoding="utf-8") as f:
            f.writelines(cls.actual_cities)
        #reseting the variable
        cls.actual_cities.clear()


class Model:
    @classmethod
    def ini(cls):
        pass

class Content:
    @classmethod
    def ini(cls):
        pass

class EventPublisher:
    observers = {}

    @classmethod
    def subscribe(cls, event, observer):
        if event not in cls.observers:
            cls.observers[event] = []
        cls.observers[event].append(observer)

    @classmethod
    def publish(cls, event, *args):
        if event in cls.observers:
            for observer in cls.observers[event]:
                observer(*args)
    @classmethod
    def unsubscribe(cls, event, observer):
        if event in cls.observers and observer in cls.observers[event]:
            cls.observers[event].remove(observer)