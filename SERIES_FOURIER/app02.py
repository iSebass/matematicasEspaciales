#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importamos todo el modulo sympy
from sympy import *
#ademas importamos las variables simbolicas 'n' y 't'
from sympy.abc import t, n

ao = integrate((pi-t), (t, 0, pi))
#integramos la funcion (2/pi) cuya variable es 't'
#y limites de integracion entre 0 y pi/2

print ("\n"+"a0 = ")
print(ao)
#Usamos la funcion pprint para mostrar ao


an = integrate((pi-t) * cos(2 * n * t), (t, 0, pi))
#integramos la funcion (2/pi)*cos(2nt)
#Su variable es 't' y sus limites de integracion son 0 y pi/2

print("\n"+"an = ")
print(an)
#Usamos la funcion pprint para mostrar an


bn = together(integrate((pi-t) * sin(2 * n * t), (t, 0, pi)))
#integramos la funcion (2/pi*cos(2nt)
#Su variable es 't' y sus limites de integracion
#son 0 y pi/2. Ademas usamos la funcion "together"
#para simplificar la expresion

print("\n"+"bn = ")
print(bn)
#Usamos la funcion pprint para mostrar bn

print("\n"+"f(x) = ")

armonicos = 20
serie = (ao/2)
for i in range(1, armonicos + 1):
    serie = serie + (an*cos(2*n*t)).subs(n, i)
for j in range(1, armonicos + 1):
    serie = serie + (bn*sin(2*n*t)).subs(n, j)

#print(serie)
plotting.plot(serie, ylim=(-1, 10), xlim=(-0.5,5)) #Usando el modulo para graficas de sympy