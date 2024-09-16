import os 
os.system ("cls || clear")
numeros = []

# Solicitando os números para o usúario
for i in range (1,6):
    num = int(input(f"Informe o {i}º número: "))
    numeros.append(num)

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
maior_numero = 0
menor_numero = 0

for numero in numeros:    # TRADUÇÃO= PARA CADA NUMERO EM NÚMEROS:
# Definindo pares e impares
    if numero %2 == 0:
        quantidade_pares += 1
        soma_pares +=1
    else:
        quantidade_impares += 1
        soma_impares +=1

# Definindo positivos e negativos
    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        quantidade_positivos += 1

# Definindo maior e menor número
    if numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

# Mostrando números na ordem inversa
print("\n=== Exibindo ordem inversa ===")
for i, numero in enumerate(reversed(numeros)):
    print(f"{i + 1}º - {numero}")
    
# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")