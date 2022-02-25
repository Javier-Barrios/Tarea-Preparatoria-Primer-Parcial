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
 print("""
    Ejercicio 8
    
    1) Mostrar los numeros impares del 1 al 100
    2) Ver historial
    0) Apagar consola
   
    """)
 try:
            opcion = int(input("Elige una opción: ") ) 

            if opcion == 1:
                
                serie=list(range(1, 100, 2 ))
                print(serie)
                impares = len((serie))
                print("los numeros impares son: ", impares)

                file = open ("Eje8.txt", "a")
                file.write ('Los numeros impares del 1 al 100 son: %s'% serie + '\n')
                file.write ('Los numeros impares son en total: %s'% impares + '\n')
                
                cursor = conexion.cursor()
                SQL = "INSERT INTO Ejercicio8(Listado, Numeros_impares) VALUES( %s,%s)" 
                cursor.execute(SQL,(serie,impares))
                conexion.commit()
                cursor.close()

            if opcion == 2:

                cursor = conexion.cursor()
                SQL = 'SELECT*FROM Ejercicio8;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
                cursor.close()
                

            if opcion == 0:
                break

 except :
  print("Ingrese solo numeros") 