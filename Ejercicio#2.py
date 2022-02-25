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
    num=input_numero("Ingrese un numero: ")
    def divisiores(num):
        resultado = [i for i in range(1, num +1) if num %i == 0]
        return resultado
    num2=divisiores(num)
    print(num2)

    file = open ("Eje2.txt", "a")
    file.write ('num= %s'% num + '\n')
    file.write ('num2= %s'% num2  + '\n')

    cursor = conexion.cursor()
    SQL = "INSERT INTO Ejercicio2(Numero,  Divisores) VALUES( %s, %s)" 
    cursor.execute(SQL,(num, num2))
    conexion.commit()
    cursor.close() 

   

