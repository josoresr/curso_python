#Declarar funcion
def hello(name):
    if str(name) == "":
        print("Hola Mundo")
    else:
        print (f"Hola {name}!")

# Invocar funcion con un valor
hello("JIMMY")
# Invocar funcion sin un valor
hello("")