'''
Escreva um programa que solicite ao usuario o valor de x 
e a velocidade v como fracao da velocidade da luz, e em 
seguida imprima o tempo em anos que a espaconave leva para 
completar a viagem (a) no referencial de repouso de um 
observador na Terra e (b) como percebido por um passageiro 
a bordo da nave. Use seu programa para calcular respostas 
para um planeta a 10 anos-luz e uma velocidade v = 0.99c
'''
from math import sqrt

x = float( input( "Digite a distancia em anos-luz: " ) )
v = float( input( "Digite a velocidade como fracao de c: " ) )

delta_t1 = x/v
delta_t2 = delta_t1 * sqrt( 1 - v**2)

print( "Tempo de viagem para um observador na Terra: ", delta_t1 )
print( "Tempo de viagem para um passageiro na nave: ", delta_t2 )

