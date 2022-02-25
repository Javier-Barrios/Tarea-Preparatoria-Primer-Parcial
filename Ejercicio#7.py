import psycopg2

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "javier",
        password = "javier",
        dbname = "Preparatoria_Primer_Parcial"
    )
    print("conexion exitosa")
except psycopg2.Error as e:
    print("Error en la conexión \nverificar parametros \n")


def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, ingrese un número")  
    return numero

while True:
    menu= input_numero("Suma de 0-n \n 1- Ingrese un numero: \n 0- Salir \n")
    if menu == 1:
        n=input_numero("Ingrese un numero: ")
        suma = (n*(n+1))/2
        print(suma, "\n")

        file = open ("Eje7.txt", "a")
        file.write ('Numero que ingreso: %s'% n + '\n')
        file.write ('Serie: %s'% suma + '\n')
        file.write ('-------------------------------' + '\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio7(Numero, Serie) VALUES( %s,%s)" 
        cursor.execute(SQL,(n,suma))
        conexion.commit()
        cursor.close() 

    elif menu == 0:
        break
    else:
        print("Ingrese una opcion correcta")