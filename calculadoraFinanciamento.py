pv = float(input("Digite o valor do empréstimo desejado: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
renda = float(input("Informe sua renda mensal: "))

i = 0.021

pmt = pv * ((1 + i) ** parcelas * i) / ((1 + i) ** parcelas - 1)

if pmt > (renda * 0.3):
    print("O valor da parcela ultrapassa a margem permitida! ")
else:
    print("O empréstimo pode ser realizado!")
    continuar = str(input("Deseja enviar a proposta? [S/N] ")).strip()[0]
    if continuar == "s":
        print("Proposta enviada para análise!")
    else:
        print("Processo encerrado.")