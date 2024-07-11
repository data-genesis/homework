class Vencie:

    def __init__(self, argum):
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
        self.argum = argum
        self.owner = self.argum[0]
        self.__model = self.argum[1]
        self.__engine_power = self.argum[3]
        self.__color = self.argum[2]


    def __str__(self):
        return f"Owner: {self.owner}, model: {self.__model}."

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model() + "\n" +
              self.get_horsepower() + "\n" +
              self.get_color() + "\n" +
              f"Владелец: {self.owner}\n")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Невозможно покрасить в {new_color}\n")


class Sedan(Vencie):

    def __init__(self, *argum):
        self.__PASSENGERS_LIMIT = 5
        self.info_ = argum
        super().__init__(self.info_)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

vehicle1.print_info()