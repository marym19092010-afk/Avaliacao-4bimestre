################################################################
# Descrição: Calcular a área total de uma residência com base  #
#            nos cômodos informados, solicitando nome,         #
#            largura e comprimento até a resposta ser 'NÃO'.   #
# Parâmetros de entrada: Nome, largura, comprimento e opção    #
#                        de continuação (SIM/NÃO)              #
# Valores de saída:      Área de cada cômodo e área total      #
# Autor: Mariane Alessandra inacio de Souza                    #
################################################################

area_total = 0

while True:
    nome_commodo = input("Digite o nome do cômodo: ")
    largura = float(input(f"Digite a largura do(a) {nome_commodo} (em metros): "))
    comprimento = float(input(f"Digite o comprimento do(a) {nome_commodo} (em metros): "))
    
    area_commodo = largura * comprimento
    area_total += area_commodo
    
    print(f"A área do(a) {nome_commodo} é: {area_commodo:.2f} m²")
    
    continuar = input("Deseja continuar calculando novos cômodos? (Digite SIM ou NÃO): ").strip().upper()
    if continuar == "NÃO" or continuar == "NAO":
        break

print(f"\nO valor total acumulado da área residencial é: {area_total:.2f} m²")
