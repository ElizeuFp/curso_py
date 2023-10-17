# 43. Operadores in e not in
# Operadores in?(Está entre) e not in(Não está entre)
# Strings são iteráveis
#  0 1 2 3 4 5
#  E l i z e u
# -6-5-4-3-2-1

#nome = 'Elizeu'
#print(nome [2])
#print(nome [-4])

#print('zeu' in nome)
#print('seu' in nome)
#print(10 * '-')
#print('zeu' not in nome)
#print('seu' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está entre {nome}')
else:
    print(f'{encontrar} não está entre {nome}')