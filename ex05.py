from math import  sqrt
 
A = float (input("Insira o valor de x1: "))

B = float(input("insira o valor de y1: "))

C = float  (input("insira o valor de x2: "))

D = float  (input ("insira o valor de y2: "))

cal1 = (C - A)

pot1 = cal1 ** 2

cal2 = (D - B)

pot2 = cal2 ** 2


soma  = pot1 + pot2

print(" o valor da soma", soma)

somaf = soma ** 0.5 
  

print(f"o valor final da distancia e ={somaf: .2f}")
