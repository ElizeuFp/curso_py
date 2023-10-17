

"""
Repetições
62. while + continue - pulando alguma repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0
while contador < 100:
    # contador += 1

    if contador == 6:
        print('Não vou mostrar o 6 otário')
        continue

    if contador >= 10 and contador  <= 50:
        print(f'Nõ vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 40:
        break # Para ele IMEDIATAMENTE
print('Acabou')

