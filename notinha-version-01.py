#RECEBIMENTO DE IFORMAÇOES
item1 = input("Digite o nome do produto: ")
pre1 = float(input("Digite o valor do produto: "))

item2 = input("Digite o nome do produto: ")
pre2 = float(input("Digite o valor do produto: "))

item3 = input("Digite o nome do produto: ")
pre3 = float(input("Digite o valor do produto: "))
soma = pre1 + pre2 + pre3
imposto = 10 / 100.0 * soma
total = soma + imposto

print("Sua compra deu: ", total)
pgmto = int(input("Insira a quantidade que deseja cobrar: "))
troco = pgmto - total

#NOTINHA
print("============SUPER=MERCADO=LAOR=========")
print(item1,"..........................", pre1)
print(item2,"..........................", pre2)
print(item3,"..........................", pre3)
print("----------------------------------------")
print("valores de impostos 10%: ", imposto)
print("              TOTAL R$: ", soma, "Reais")
print("              Troco R$:", troco, "Reais")
print("=======OBRIGADO PELA PREFENRENCIA=======")
