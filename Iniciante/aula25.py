# 44. Interpolação de string com % em Python

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Elizeu'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f %s' % (nome,preco,nome)
print(variavel)
print('O hexadecimal de %d é %0.4x' % (1500 , 1500))