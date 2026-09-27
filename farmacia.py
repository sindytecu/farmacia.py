import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="farmacia"
)

def clientes():
    name = input("INGRESE SU NOMBRE: ")
    year = int(input("INGRESE SU EDAD: "))
    compra = input("INGRESE EL NOMBRE DEL PRODUCTO: ")
    precio = input("INGRESE EL PRECIO: ")
    telefono = input("INGRESE SU NUMERO DE TELEFONO: ")

    if conexion.is_connected():
        cursor = conexion.cursor()
        query = "INSERT INTO cliente(nombre,edad,compra,precio,telefono) VALUES (%s,%s,%s,%s,%s)" 
        cursor.execute (query, (name,year,compra,precio,telefono))
        conexion.commit()
        print ("SUS DATOS SE ALMACENAN CORRECTAMENTE: ")


def consultar():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cliente")
    for fila in cursor.fetchall():
        print(fila)


def actualizar():
    id_actualizar = int(input("INGRESE EL ID A ACTUALIZAR: "))
    name = input("NUEVO NOMBRE: ")
    year = int(input("INGRESE SU EDAD: "))
    compra = input("INGRESA EL NOMBRE DEL PRODUCTO: ")
    precio = input("INGRESE EL PRECIO: ")
    telefono = input("INGRESE SU NUMERO DE TELEFONO: ")

    cursor = conexion.cursor()
    query = "UPDATE cliente SET nombre=%s, edad=%s, compra=%s,precio=%s, telefono=%s WHERE idcliente=%s"
    cursor.execute(query, (name, year, compra, precio, telefono, id_actualizar))
    conexion.commit()
    print("ACTUALIZADO CORRECTAMENTE")


def borrar():
    id_borrar = int(input("INGRESE EL ID PARA BORRAR: "))
    cursor = conexion.cursor()
    query = "DELETE FROM cliente WHERE idcliente = %s"
    cursor.execute(query, (id_borrar,))
    conexion.commit()
    print("EL PRODUCTO SE BORRO CORECTAMENTE")


def menu():
    lista = ["1.INGRESE CLIENTE", "2.CONSULTAR", "3.ACTUALIZAR", "4.BORRAR"]
    for item in lista:
        print(item)
    desis = int(input("INGRESE LA OCPION: "))

    match desis:
        case 1:
            clientes()
        case 2:
            consultar()
        case 3:
            actualizar()
        case 4:
            borrar()
        case _:
            print("INGRESE UN DATO VALIDO")

menu( )
