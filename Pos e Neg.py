import os 

os.system("cls || clear")

contadorpos = 0
contadorneg = 0 

while True:
 numero = int(input("Digite um número:"))
 opcao = str(input("Deseja digitar mais algo:"))

 opcao = opcao.upper() 

 if opcao == "N":
   break
 if numero < 0: 
    contadorneg
 elif numero < 0:
    contadorpos
    soma= contadorpos + 1


print(f"Contador de números positivos = {contadorpos}")
print(f"Contador de números negativos = {contadorneg}")
print(f"Total de números positivos = {soma}")

