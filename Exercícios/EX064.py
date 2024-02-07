def temperatura(temp):
    fahrenheit = (temp * 1.8) + 32
    print(f"A temperatura em fahrenheit é {fahrenheit}.")


celsius = int(input("Insira a temperatura em graus Celsius: "))
temperatura(celsius)
