class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def get_raio(self):
        return self.__raio

    def set_raio(self, valor):
        self.__raio = valor

    def get_area(self):
        print(f"A area do circulo é:", 3.14159 * (self.__raio * self.__raio))


circulo = Circulo(5)
print(f"Valor inicial do raio: {circulo.get_raio()}")
circulo.get_area()
r = int(input("Qual o raio do círculo: "))
circulo.set_raio(r)
print(f"Novo valor do raio: {circulo.get_raio()}")
circulo.get_area()
