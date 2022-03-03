import time as tempo
from termcolor import colored as cor

print('\n' * 130)
print(cor('JOGO DA MATEMÀTICA', 'blue'))
print('Seja Bem vindo')

tempo.sleep(3)
print('\n' * 130)

opção = 0
while opção != '1':
    print(cor('ESCOLHAR UMA TABUADA PARA ESTUDAR:', 'green'))
    print('''
[ 1 ] Sai do Jogo
[ 2 ] multiplicando x2
[ 3 ] multiplicando x3
[ 4 ] multiplicando x4
[ 5 ] multiplicando x5
[ 6 ] multiplicando x6
[ 7 ] multiplicando x7
[ 8 ] multiplicando x8
[ 9 ] multiplicando x9
[ 10 ] multiplicando x10
    ''')

    print('Qual sua opção?')
    opção = (input('> '))

#TABUADA X2
    if opção == '2':
        print('\n' * 130)
        print('''
Tabuada do 2

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
        ''')
        input('pressione a tecla a tecla enter para continuar')
        print('\n' * 130)
#2 x 5---------------------------------------        
        print('2 x 5 =')
        responda_2x5 = input('> ')
        if responda_2x5 == '10':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 5 = {2 * 5}', 'red'))
            tempo.sleep(2)

#2 x 7---------------------------------------------
        print('\n' * 130)
        print('2 x 7 =')
        responda_2x7 = input('> ')
        if responda_2x7 == '14':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 7 = {2 * 7}', 'red'))
            tempo.sleep(2)

#2 x 3---------------------------------------------
        print('\n' * 130)
        print('2 x 3 =')
        responda_2x3 = input('> ')
        if responda_2x3 == '6':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 3 = {2 * 3}', 'red'))
            tempo.sleep(2)

#2 x 1---------------------------------------------
        print('\n' * 130)
        print('2 x 1 =')
        responda_2x1 = input('> ')
        if responda_2x1 == '2':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(2)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 1 = {2 * 1}', 'red'))
            tempo.sleep(2)

#2 x 8---------------------------------------------
        print('\n' * 130)
        print('2 x 8 =')
        responda_2x8 = input('> ')
        if responda_2x8 == '16':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 8 = {2 * 8}', 'red'))
            tempo.sleep(2)

#2 x 2---------------------------------------------
        print('\n' * 130)
        print('2 x 2 =')
        responda_2x2 = input('> ')
        if responda_2x2 == '4':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 2 = {2 * 2}', 'red'))
            tempo.sleep(2)    

#2 x 6---------------------------------------------
        print('\n' * 130)
        print('2 x 6 =')
        responda_2x6 = input('> ')
        if responda_2x6 == '12':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 6 = {2 * 6}', 'red'))
            tempo.sleep(2) 

#2 x 4---------------------------------------------
        print('\n' * 130)
        print('2 x 4 =')
        responda_2x4 = input('> ')
        if responda_2x4 == '8':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(2)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 4 = {2 * 4}', 'red'))
            tempo.sleep(1)

#2 x 9---------------------------------------------
        print('\n' * 130)
        print('2 x 9 =')
        responda_2x9 = input('> ')
        if responda_2x9 == '18':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 9 = {2 * 9}', 'red'))
            tempo.sleep(2)

#2 x 10---------------------------------------------
        print('\n' * 130)
        print('2 x 10 =')
        responda_2x10 = input('> ')
        if responda_2x10 == '20':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
            print('\n' * 130)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 2 x 10 = {2 * 10}', 'red'))
            tempo.sleep(2)
            print('\n' * 130)  

        print(cor('você chegou ao final da tabuada de 2', 'green'))
        tempo.sleep(3)
        print('\n' * 130)

#TABUADA X3 colocar espaço dos calulos - erro pra ajeita 
    elif opção == '3':
        print('\n' * 130)
        print('''
Tabuada do 3

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
        ''')

        input('pressione a tecla a tecla enter para continuar')
        print('\n' * 130)
#3 x 1---------------------------------------        
        print('3 x 1 =')
        responda_3x1 = input('> ')
        if responda_3x1 == '3':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 1 = {3 * 1}', 'red'))
            tempo.sleep(2)

#3 x 5---------------------------------------        
        print('3 x 5 =')
        responda_3x5 = input('> ')
        if responda_3x5 == '15':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 5 = {3 * 5}', 'red'))
            tempo.sleep(2)

#3 x 7---------------------------------------        
        print('3 x 7 =')
        responda_3x7 = input('> ')
        if responda_3x7 == '21':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 7 = {3 * 7}', 'red'))
            tempo.sleep(2)

#3 x 4---------------------------------------        
        print('3 x 4 =')
        responda_3x4 = input('> ')
        if responda_3x4 == '12':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 4 = {3 * 4}', 'red'))
            tempo.sleep(2)

#3 x 2---------------------------------------        
        print('3 x 2 =')
        responda_3x2 = input('> ')
        if responda_3x2 == '6':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 2 = {3 * 2}', 'red'))
            tempo.sleep(2)

#3 x 9---------------------------------------        
        print('3 x 9 =')
        responda_3x9 = input('> ')
        if responda_3x9 == '27':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 9 = {3 * 9}', 'red'))
            tempo.sleep(2)

#3 x 3---------------------------------------        
        print('3 x 3 =')
        responda_3x3 = input('> ')
        if responda_3x3 == '9':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 3 = {3 * 3}', 'red'))
            tempo.sleep(2)

#3 x 8---------------------------------------        
        print('3 x 8 =')
        responda_3x8 = input('> ')
        if responda_3x8 == '24':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 8 = {3 * 8}', 'red'))
            tempo.sleep(2)

#3 x 6---------------------------------------        
        print('3 x 6 =')
        responda_3x6 = input('> ')
        if responda_3x6 == '18':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 8 = {3 * 6}', 'red'))
            tempo.sleep(2)

#3 x 10---------------------------------------        
        print('3 x 10 =')
        responda_3x10 = input('> ')
        if responda_3x10 == '30':
            print('\n' * 130)
            print(cor('Você acertou', 'green'))
            tempo.sleep(1)
        else:
            print('\n' * 130)
            print(cor(f'Você errou, 3 x 10 = {3 * 10}', 'red'))
            tempo.sleep(2)

        print(cor('você chegou ao final da tabuada de 2', 'green'))
        tempo.sleep(3)
        print('\n' * 130)

#TABUADA X4
    elif opção == '4':
        print('\n' * 130)
        print('''
Tabuada do 4

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
        ''')

#TABUADA X5
    elif opção == '5':
        print('\n' * 130)
        print('''
Tabuada do 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
        ''')

#TABUADA X6
    elif opção == '6':
        print('\n' * 130)
        print('''
Tabuada do 6

6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
        ''')

#TABUADA X7
    elif opção == '7':
        print('\n' * 130)
        print('''
Tabuada do 7

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
        ''')

#TABUADA X8
    elif opção == '8':
        print('\n' * 130)
        print('''
Tabuada do 8

8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
        ''')

#TABUADA X9
    elif opção == '9':
        print('\n' * 130)
        print('''
Tabuada do 9

9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
        ''')

#TABUADA X10
    elif opção == '10':
        print('\n' * 130)
        print('''
Tabuada do 10
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100
        ''')
    else:
        print(cor('COMANDO ERRRADO!', 'red')) 

#Finalização do jogo
print('\n' * 130)
print(cor('FIM DE JOGO, VOLTE SEMPRE!', 'blue'))
tempo.sleep(3)

print('\n' * 130)
print('Escreva (exit)')
tempo.sleep(3)

print('\n' * 130)
