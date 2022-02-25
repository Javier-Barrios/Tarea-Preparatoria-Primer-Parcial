from cmath import pi
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
    Ejercicio 9 Areas de figuras
    
    1) Area de un Circulo
    2) Area de un Triangulo
    3) Area de un Cuadrado
    4) Area de un Rectangulo
    5) Ver historial de operaciones
    0) Apagar Consola  

    """)
  
    opcion = int(input("Elige una opción: ") )       
    
    if opcion == 1:
        
        operacion="Circulo"   
        r = float(input("Ingrese el valor del radio del circulo: ") )
        area = 3.1416*r*r
        print(" ")
        print("RESULTADO:",area)
            

        file = open ("Eje9.txt", "a")
        file.write ('Figura= %s'% operacion + '\n')
        file.write ('Area= %s'% area + '\n')
        file.write ('------------------------------' + '\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio9(Figura, Area) VALUES( %s,%s)" 
        cursor.execute(SQL,(operacion,area))
        conexion.commit()
        cursor.close()

    elif opcion == 2:
        
        operacion="Triangulo"   
        b = float(input("Ingrese el valor la base del triangulo: ") )
        h = float(input("Ingrese el valor la altura del triangulo: ") )
        area = (b*h)/2
        print(" ")
        print("RESULTADO:",area)
            

        file = open ("Eje9.txt", "a")
        file.write ('Figura= %s'% operacion + '\n')
        file.write ('Area= %s'% area + '\n')
        file.write ('------------------------------' + '\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio9(Figura, Area) VALUES( %s,%s)" 
        cursor.execute(SQL,(operacion, area))
        conexion.commit()
        cursor.close()
    
    elif opcion == 3:
        
        operacion="Cuadrado"   
        l = float(input("Ingrese el valor de un lado del cuadrado: ") )
        area = l*l
        print(" ")
        print("RESULTADO:",area)
            

        file = open ("Eje9.txt", "a")
        file.write ('Figura= %s'% operacion + '\n')
        file.write ('Area= %s'% area + '\n')
        file.write ('------------------------------' + '\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio9(Figura, Area) VALUES( %s,%s)" 
        cursor.execute(SQL,(operacion, area))
        conexion.commit()
        cursor.close()

    elif opcion == 4:
        
        operacion="Rectangulo"   
        b = float(input("Ingrese el valor de la base del rectangulo: ") )
        h = float(input("Ingrese el valor de la altura del rectangulo: ") )
        area = l*l
        print(" ")
        print("RESULTADO:",area)
            

        file = open ("Eje9.txt", "a")
        file.write ('Figura= %s'% operacion + '\n')
        file.write ('Area= %s'% area + '\n')
        file.write ('------------------------------' + '\n')

        cursor = conexion.cursor()
        SQL = "INSERT INTO Ejercicio8(Listado, Numeros_impares) VALUES( %s,%s)" 
        cursor.execute(SQL,(operacion, area))
        conexion.commit()
        cursor.close()

    elif opcion == 5:
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM ejercicio9;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()

    elif opcion == 0:
        break

    else:
        print("--------")
    


