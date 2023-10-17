
"""
54. Exercícios - Enunciados
55. Solução 1 dos Exercícios - Enunciados
56. Solução 2 dos Exercícios - Enunciados
57. Solução 3 dos Exercícios - Enunciados


Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
 

usuario = (input('Digite um número inteiro: '))

try:
    numero_int = (int(usuario))
    divisao = numero_int % 2 == 0
    
    if divisao:
        print(f'O número {usuario} é par')
    else:
        print(f'O {usuario} é impar')
except:
    print('Isso não é um número inteiro')

    

#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#descrito, exiba a saudação apropriada. Ex. 
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

entrada = input('Digite Que horas são em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print(f'bom dia')
    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite')
    else:
        print('Não conheço essa hora')
    

except:
    print('')

#
#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
#"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 


nome = input('Digite seu nome: ')

tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

