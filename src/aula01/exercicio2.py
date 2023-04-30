'''
    Uma bola e abandonada do repouso do alto de
    uma torre. Escreva um programa que peca ao
    usuario para digitar a altura da torre em metros e
    entao calcule o tempo que a bola leva para atingir
    o solo, ignorando a resistencia do ar. Utilize o
    programa para calcular esse tempo para uma
    altura de 100 metros.
'''
h = float( input( "Digite a altura inicial: " ) )

# Aceleracao da gravidade
g = 9.81

# Calculando a resposta
t = ( 2*h/g )**( 1/2 )
print( "O tempo de queda e : ", t )
