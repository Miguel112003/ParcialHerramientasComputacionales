# Parcial 1
# Miguel Bejarano Perdomo

# Defino variables globales

sumaPrecioProducto = 0

# Linea Logica Principal

cedula = int(input("Ingrese su numero de cedula, sin puntos ni comas: "))

print(""" Seleccione
1. Alumno
2. Maestro
""")
rol = int(input())
if rol != 1 and rol != 2:
    print("Opcion no valida, reinicie el programa")

if rol == 1:
    descuento = 0.5
elif rol == 2:
    descuento = 0.2


def productos(sumaPrecioProducto, rol):
    print("""
1. Añadir producto
0. Salir y facturar
""")
    añadir = int(input())
    if añadir != 1 and añadir != 0:
        print("Ocurrio un error, reinicio automatico")
        print("""
1. Añadir producto
0. Salir y facturar """)
        añadir = int(input())
    listaCodigosProducto = []
    listaCantidadProducto = []
    while añadir == 1:
        codigoProducto = int(input("Ingrese el codigo del producto: "))
        cantidadProducto = int(input("Ingrese la cantidad de unidades: "))
        precioProducto = float(input("Ingrese el precio del producto: "))
        sumaPrecioProducto = sumaPrecioProducto + (precioProducto *
                                                   cantidadProducto)
        listaCodigosProducto.append(codigoProducto)
        listaCantidadProducto.append(cantidadProducto)
        print("""
1. Añadir producto
0. Salir y facturar """)
        añadir = int(input())
    if añadir == 0:
        if rol == 1:
            print("El Alumno con cedula", cedula, "debe pagar",
                  sumaPrecioProducto - (sumaPrecioProducto*descuento),
                  "Por los productos",
                  listaCodigosProducto, "En cantidades de",
                  listaCantidadProducto)
        if rol == 2:
            print("El Maestro con cedula", cedula, "debe pagar",
                  sumaPrecioProducto - (sumaPrecioProducto*descuento),
                  "Por los productos",
                  listaCodigosProducto, "En cantidades de",
                  listaCantidadProducto)

productos(sumaPrecioProducto, rol)
