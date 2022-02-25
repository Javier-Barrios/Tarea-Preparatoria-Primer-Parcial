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

while True:
    def obtener_vocales(frase):
        vocales='aeiouAEIOU'

        return[c for c in frase if c in vocales]

    palabra= input("Ingrese una Palabra: ")
    vocal= len(obtener_vocales(palabra))
    print("La palabra tiene", vocal, "vocales")

    file = open ("Eje3.txt", "a")
    file.write ('Palabra: %s'% palabra + '\n')
    file.write ('Numero de vocales: %s'% vocal + '\n')
    
    cursor = conexion.cursor()
    SQL = "INSERT INTO Ejercicio3(Palabra,  Numero_de_vocales) VALUES( %s, %s)" 
    cursor.execute(SQL,(palabra, vocal))
    conexion.commit()
    cursor.close() 
