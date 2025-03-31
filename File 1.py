class TransportCompany:
    totalCount = 0
    def __init__(self, nameCompany, number, engineVolume, speed, typeOfFuel):
        self.__nameCompany = nameCompany
        self.__number = number
        self.__engineVolume = engineVolume
        self.__speed = speed
        self.__typeOfFuel = typeOfFuel
        self.__list = []



    @staticmethod
    def valid_number(number):
        import re
        vNumber = r'^[A-Z]{2}\d{4}[A-Z]{2}$'
        return bool(re.match(vNumber, number))

    @staticmethod
    def valid_param(engineVolume, speed):
        if engineVolume > 0 and speed > 0:
            return True
        return False


    def change_name_company(self, newName):
        self.__nameCompany = newName
        return f"Назву компанії змінено на {newName}"

    @classmethod
    def get_total_count(cls):
        return f"Загальна кількість транспортних засобів: {cls.totalCount}"

    def add_vehicle(self, vehicle):
        self.__list.append(vehicle)
        TransportCompany.totalCount += 1
        return f"Транспортний засіб {vehicle} додано до списку"

    def get_vehicle_info(self, index):
        if index >= 0 and index < len(self.__list):
            return self.__list[index]
        else:
            return f"Транспортний засіб з індексом {index} не знайдено"

    def update_vehicle(self, index, newData):
        if index >= 0 and index < len(self.__list):
            self.__list[index] = newData
            return "Інформацію оновлено"
        else:
            return "Транспортний засіб з таким індексом не знайдено"

    def get_info(self):
        print(f"Назва компанії: {self.__nameCompany} номер: {self.__number}")

company = TransportCompany("TransCity", "KX3274AI", 2.5, 150, "Diesel")


print(TransportCompany.valid_number("KX3274AI"))
print(TransportCompany.valid_param(2.5, 150))
print(company.add_vehicle("Volvo"))
print(company.add_vehicle("Toyota"))
print(company.get_vehicle_info(0))
print(company.get_vehicle_info(1))
print(company.change_name_company("BigTrancCity"))
company.get_info()

print(TransportCompany.get_total_count())




