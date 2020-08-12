tipo=int(input("Elija el tipo de poligono:\n1. RECTANGULO\n2. CUADRADO\n"))
lado=float(input("Ingrese el tamaño del lado del Poligono:"))
if tipo==1:
    calculo=4*lado
    print(f"El perimetro del  cuadrado es: {calculo}")
elif tipo==2:
    calculo=lado*lado
    print(f"El area del rectangulo es: {calculo}")
