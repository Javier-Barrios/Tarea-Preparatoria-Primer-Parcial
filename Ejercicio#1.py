def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=input(msj)
            break
        except ValueError:
            print("Error, ingrese un número")  
    return numero

num=input_numero("Ingrese un numero: ")
print(num)