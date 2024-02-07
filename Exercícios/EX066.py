def fatorial(num, mostrar):
    resultado = 1
    count = 1
    show = num
    if mostrar == False:
        while count <= num:
            resultado *= count
            count += 1

        return resultado

    elif mostrar == True:
        while count <= num:
            resultado *= count
            if count == num:
                print(f"{show} = ", end="")
            else:
                print(f"{show} x ", end="")
            show -= 1
            count += 1
        return resultado


numero = int(input("Insira uma número para calcular o seu fatorial: "))
ver = str(input("Quer ver o processo de calculo? [S/N]")).strip().upper()

if ver == "S":
    ver = True

else:
    ver = False

print(fatorial(numero, ver))
