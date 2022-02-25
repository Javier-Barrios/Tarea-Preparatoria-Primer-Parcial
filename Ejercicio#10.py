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
    Ejercicio 10 Tipo de triangulos
    
    1) Introducir los valores de los 3 lados del triangulo
    2) Mostrar Historial
    0) Apagar consola
   
    """)
 
 opcion = int(input("Elige una opción: ") ) 

 if opcion == 1:
        
            n1 = float(input("Introduce el valor del primer lado: ") )
            n2 = float(input("Introduce el valor del segundo lado: ") )
            n3 = float(input("Introduce el valor del tercer lado: ") )
        

            file = open ("Eje10.txt", "a")
            file.write ('lado 1= %s'% n1 + '\n')
            file.write ('lado 2= %s'% n2 + '\n')
            file.write ('lado 3= %s'% n3 + '\n')

        

            if n1 == n2 and n1 == n3 and n2 == n3:
                tipo="Equilatero"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                SQL = "INSERT INTO Ejercicio10(Lado_1, Lado_2, Lado_3, Triangulo) VALUES( %s,%s,%s,%s)" 
                cursor.execute(SQL,(n1, n2, n3,tipo))
                conexion.commit()
                cursor.close()          
                
            elif n1 != n2 and n1 != n3 and n2 != n3:
                tipo="Escaleno"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                SQL = "INSERT INTO Ejercicio10(Lado_1, Lado_2, Lado_3, Triangulo) VALUES( %s,%s,%s,%s)" 
                cursor.execute(SQL,(n1, n2, n3,tipo))
                conexion.commit()
                cursor.close()

            elif n1 == n2 and n1 != n3 and n2 != n3:
                tipo="Isosceles"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                SQL = "INSERT INTO Ejercicio10(Lado_1, Lado_2, Lado_3, Triangulo) VALUES( %s,%s,%s,%s)" 
                cursor.execute(SQL,(n1, n2, n3,tipo))
                conexion.commit()
                cursor.close()
            
            elif n1 == n3 and n1 != n2 and n3 != n2:
                tipo="Isosceles"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                SQL = "INSERT INTO Ejercicio10(Lado_1, Lado_2, Lado_3, Triangulo) VALUES( %s,%s,%s,%s)" 
                cursor.execute(SQL,(n1, n2, n3,tipo))
                conexion.commit()
                cursor.close()
                
            elif n2 == n3 and n2 != n1 and n3 != n1:
                tipo="Isosceles"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                SQL = "INSERT INTO Ejercicio10(Lado_1, Lado_2, Lado_3, Triangulo) VALUES( %s,%s,%s,%s)" 
                cursor.execute(SQL,(n1, n2, n3,tipo))
                conexion.commit()
                cursor.close() 

 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio10;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 
