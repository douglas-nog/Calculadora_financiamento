pv = float(input("Digite o valor do empréstimo desejado: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
renda = float(input("Informe sua renda mensal: "))

i = 0.021

pmt = pv * ((1 + i) ** parcelas * i) / ((1 + i) ** parcelas - 1)

