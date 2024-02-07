from datetime import datetime
SCH = dict()
ano = int(datetime.now().year)

SCH["Nome"] = input("Insira o nome:")
anonasc = int(input("Insira o ano de nascimento:"))
SCH["Idade"] = ano - anonasc
rendimentos = int(input("Insira os rendimentos:"))
SCH["Rendimentos Mensais"] = rendimentos
despesas = int(input("Insira o valor das despesas mensais:"))
remanescente = rendimentos - despesas
SCH["Remanescente"] = remanescente
SCH["Montante de crédito"] = int(input("Insira o montante:"))
SCH["Prazo em Anos"] = int(input("Insira o número de anos:"))

meses = SCH["Prazo em Anos"] * 12
pagarMes = (SCH["Montante de crédito"] / meses)

if remanescente > pagarMes:
        print(SCH)
        print("Crédito aprovado")

else:
        print(SCH)
        print("Crédito recusado")
