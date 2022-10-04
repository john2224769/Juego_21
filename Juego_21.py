# Programa N. 3. aleatorios: Juego de la 21 vs computadora 

import random
from os import system

print("------------------------------------------")
print("\nEscoja su opcion de juego, sume numeros hasta llegar a 21 o lo mas cercano: ")
print("\ns para seguir y pedir una carta ")
print("\np. para plantar y detener el juego ")
print("-----------------------------------------\n")

c1=random.randint(1,12)
c2=random.randint(1,12)
c1_com=random.randint(1,12)
c2_com=random.randint(1,12)
print(str(c1) + " " +str(c2)+ " "+str(c1_com)+" "+str(c2_com))

while c1 == c2:
    c2=random.randint(1,12)
    print(str(c1) + " " +str(c2)+ " "+str(c1_com)+" "+str(c2_com))
    print(" ")
    system("pause")
while c1_com == c1 or c1_com == c2:
    c1_com=random.randint(1,12)
    print(str(c1) + " " +str(c2)+ " "+str(c1_com)+" "+str(c2_com))
    print(" ")
    system("pause")
while c2_com == c1 or c2_com == c2 or c2_com == c1_com:
    c2_com=random.randint(1,12)
    print(str(c1) + " " +str(c2)+ " "+str(c1_com)+" "+str(c2_com))
    print(" ")
    system("pause")

print("Sus cartas son: "+ str(c1) + " " +str(c2))
print(" ")
opcion=input("Si desea seguir y pedir otra carta escriba s, si desea plantar y finalizar su jugada escriba p ")
if opcion=="s":
    c3=random.randint(1,12)
    while c3==c1 or c3==c2 or c3==c1_com or c3==c2_com:
        c3=random.randint(1,12)
        print(str(c1) + " " +str(c2)+ " "+str(c1_com)+" "+str(c2_com))
        print(" ")
        system("pause")
    print("Sus cartas son: "+ str(c1) + " " +str(c2)+" "+str(c3))
print(str(c1) + " " +str(c2)+ " "+str(c1_com)+" "+str(c2_com))
print(" ")