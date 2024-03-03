import random

entrada1=random.random()
entrada2=random.random()
entrada3=random.random()

peso1=0.91823
peso2=0.190237
peso3=-1.29387
umbral=0.123897

#! Feed Foward
salida=entrada1*peso1+entrada2*peso2+entrada3*peso3
salida+= umbral

print(salida)

#OPTIMIZACION 1
entradas=[random.random(),random.random(),random.random()]
pesos=[random.random(),random.random(),random.random(),random.random()]

salida2=entradas[0]*pesos[0]+entradas[1]*pesos[1]+entradas[2]*pesos[2]
salida2+=pesos[-1]

print(salida2)

#OPTIMIZACION 2
entradas2=[random.random(),random.random(),random.random()]
pesos2=[random.random(),random.random(),random.random(),random.random()]
salida3=0

for i in range(len(entradas2)):
    salida3+=entradas2[i]*pesos2[i]

salida3+=pesos2[-1]
print(salida3)