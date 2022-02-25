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
    menu = int(input_numero("Base de Datos de Taxis: \n 1- Ingresar datos \n 2- Historial \n 0- Salir \n"))
    if menu == 1:
        ano=input_numero("Ingrese el año del Taxi: ")
        kilo=input_numero("Ingrese el kilometraje del Taxi (Km): ")

        if ano<=2006 and kilo>=20001:
            x="Necesita Renovarse"
            print(x, "\n")

            file = open ("Eje14.txt", "a")
            file.write ('Modelo del Taxi: %s'% ano + '\n')
            file.write ('Kilometraje del Taxi: %s'% kilo + '\n')
            file.write ('Situacion del Taxi: %s'% x + '\n')
            file.write ('-------------------------------' + '\n')

            cursor = conexion.cursor()
            SQL = "INSERT INTO Ejercicio14(Modelo, Kilometraje, Situacion) VALUES( %s,%s,%s)" 
            cursor.execute(SQL,(ano, kilo, x))
            conexion.commit()
            cursor.close() 
            

        elif ano>=2007 and ano<=2012 and kilo>=20000:
            x="Necesita Mantenimiento"
            print(x, " \n")

            file = open ("Eje14.txt", "a")
            file.write ('Modelo del Taxi: %s'% ano + '\n')
            file.write ('Kilometraje del Taxi: %s'% kilo + '\n')
            file.write ('Situacion del Taxi: %s'% x + '\n')
            file.write ('-------------------------------' + '\n')

            cursor = conexion.cursor()
            SQL = "INSERT INTO Ejercicio14(Modelo, Kilometraje, Situacion) VALUES( %s,%s,%s)" 
            cursor.execute(SQL,(ano, kilo, x))
            conexion.commit()
            cursor.close() 

        elif ano>=2013 and kilo<=10000:
            x="Optimas Condiciones"
            print(x, " \n")

            file = open ("Eje14.txt", "a")
            file.write ('Modelo del Taxi: %s'% ano + '\n')
            file.write ('Kilometraje del Taxi: %s'% kilo + '\n')
            file.write ('Situacion del Taxi: %s'% x + '\n')
            file.write ('-------------------------------' + '\n')

            cursor = conexion.cursor()
            SQL = "INSERT INTO Ejercicio14(Modelo, Kilometraje, Situacion) VALUES( %s,%s,%s)" 
            cursor.execute(SQL,(ano, kilo, x))
            conexion.commit()
            cursor.close() 

        else :
            print("Mecanico \n")
    if menu == 2:
        cursor = conexion.cursor()
        SQL = "SELECT*FROM Ejercicio14" 
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
    if menu == 0:
        break  

