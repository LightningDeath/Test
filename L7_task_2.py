# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

from Chek_input_vol import ch_num_i


class Mydesk:
    def __init__(self, vol, st):
        self.vol = vol
        self.st = st

    def __set__(self, instance, vol):
        if vol.isdigit():
            instance.__dict__[self.vol] = int(vol)
        else:
            return self.__set__(instance, input(f'Вы ввели не число! попробуйте ещё раз!\n'
                                                f'Введите {self.st} дороги в метрах: '))

    # def __set_name__(self, owner, vol, st):
    #     self.vol = vol
    #     self.st = st


class Road:
    mass = 25
    width_1 = 0.5
    __length = Mydesk('__length', 'длину')
    __width = Mydesk('__width', 'ширину')

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def task(self):
        res = int(self.__length * self.__width * self.mass * self.width_1)
        res_1 = int(res / 1000)
        return f'Масса асфальта, необходимого для покрытия заданного участка дороги равна:\n' \
               f'{self.__length}м*{self.__width}м*{self.mass}кг*{self.width_1}м = {res} кг = {res_1} т'


road = Road(input('Введите длину дороги в метрах: '),
            input('Введите ширину дороги в метрах: '))
print(road.task())
