class Temperatura:
    def __init__(self, graus):
        self.__graus = graus

    @property
    def celsius(self):
        return f'Temperatura em Celsius: {self.__graus}ºC'

    def fahrenheit(self):
        fahrenheit = (self.__graus * 1.8) + 32
        print(f"Temperatura em Fahrenheit: {fahrenheit}ºF")

    def kelvin(self):
        kelvin = self.__graus + 273
        print(f"Temperatura em Kelvin: {kelvin}ºK")


celsius = int(input('Insira a temperatura em ºC: '))

temp = Temperatura(celsius)

print(temp.celsius)
temp.fahrenheit()
temp.kelvin()
