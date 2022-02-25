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
    num1= input_numero("Ingrese el primer numero: ")
    num2= input_numero("Ingrese el segundo numero: ")
    if num1 < num2:
        x=list(range(num2, num1-1, -1))
        print(x)

        file = open ("Eje5.txt", "a")
        file.write ('Primer Numero: %s'% num1 + '\n')
        file.write ('Segundo Numero: %s'% num2 + '\n')
        file.write ('De mayor a menor: %s'% x + '\n')
        file.write ('-----------------------------''\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio5(Numero_Mayor, Numero_Menor, Serie) VALUES( %s, %s,%s)" 
        cursor.execute(SQL,(num2, num1, x))
        conexion.commit()
        cursor.close() 

    elif num1 > num2:
        x=list(range(num1, num2-1, -1))
        print(x)

        file = open ("Eje5.txt", "a")
        file.write ('Primer Numero: %s'% num1 + '\n')
        file.write ('Segundo Numero: %s'% num2 + '\n')
        file.write ('Numeros de 2 en 2: %s'% x + '\n')
        file.write ('-----------------------------''\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio5(Numero_Mayor, Numero_Menor, Serie) VALUES( %s, %s,%s)" 
        cursor.execute(SQL,(num1, num2, x))
        conexion.commit()
        cursor.close()

    else :
        print("sus numeros son iguales")

        file = open ("Eje5.txt", "a")
        file.write ('Primer Numero: %s'% num1 + '\n')
        file.write ('Segundo Numero: %s'% num2 + '\n')
        file.write ('Sus numeros son Iguales''\n')
        file.write ('-----------------------------''\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio5(Numero_Mayor, Numero_Menor, Serie) VALUES( %s, %s, 'Numeros iguales')" 
        cursor.execute(SQL,(num1, num2))
        conexion.commit()
        cursor.close()