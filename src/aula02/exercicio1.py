'''
Escreva um programa que calcule e imprima em
ordem crescente todos os numeros de Catalan
menores ou iguais a um bilhao
'''
n, c = 0, 1

while ( c <= 10**9 ):
    print( c )
    c = ( 4*n + 2) * c // ( n+2 )
    n += 1