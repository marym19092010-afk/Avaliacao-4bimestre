################################################################
# Descrição: Ler 20 temperaturas em graus Celsius, armazenar em #
#            um vetor e apresentar a menor, a maior e a média. #
# Parâmetros de entrada: 20 valores reais de temperaturas      #
# Valores de saída:      Menor, maior e média das temperaturas #
# Autor:Mariane Alessandra Inacio de Souza                     #
################################################################

temperaturas = []

for i in range(20):
    temp = float(input(f"Digite a temperatura {i+1} (°C): "))
    temperaturas.append(temp)

menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print(f"Menor temperatura: {menor:.2f} °C")
print(f"Maior temperatura: {maior:.2f} °C")
print(f"Média das temperaturas: {media:.2f} °C")
