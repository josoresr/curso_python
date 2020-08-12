# Definir funcion
def divisible(n,d1,d2):
    if int(n)%int(d1)==0:
        if int(n)%int(d2)==0:
            print(f"El numero {n} es divisible con {d1} y {d2}")
    else:
        print(f"El numero {n} no es divisible con ambos numeros: {d1} y {d2}")


# Invocar funcion
divisible(15,45,3)