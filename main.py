'''
Este es un ejemplo para trabajar con módulos, funciones y sets
Primero: Crearé un set con productos y su precio sin IVA
Segundo: Crearé una estructura de módulos para alojar la función que calcule el IVA, es decir, 19% de un valor.
Tercero: Llamaré al módulo 'impuesto' para 'calcular_iva'' de cada producto y generar un nuevo
         set de los productos con IVA, luego imprimirlos.
Recorrido: 
(Me falta completar esta parte)

Resultado esperado:
(Me falta completar esta parte)
'''

# Defino este conjunto de periféricos con sus precios
#Clave: producto, valor: precio
perifericos = {
    ("Teclado USB Developer", 45000),
    ("Mouse ergonómico", 25000),
    ("Monitor 24 pulgadas", 120000),
    ("Auriculares inalámbricos", 60000),
    ("Micrófono USB", 35000),
    ("Cámara web HD", 30000),
    ("PAD para mouse", 8000),
    ("Parlantes estéreo", 28000),
    ("Disco duro externo 1TB", 55000),
    ("Conector Hub USB 3.0", 15000)
}


# Imprimo lista de productos periféricos de computador SIN IVA
print()
print("Lista de precios sin IVA: \n")
for producto, precio in perifericos:
    print(f"Producto: {producto}, Precio: ${precio}")
print()
num_productos = len(perifericos)
print(f"Usted tiene: {num_productos} tipos de productos.")  #Agrego esta línea para informar cuántos productos tiene.
print()


agregar_productos = input("¿Desea agregar más productos? (S/N): ")
while agregar_productos != 'n' or agregar_productos == 'N':
    if agregar_productos == 's' or agregar_productos == 'S':
        nombre_nuevo_producto = input("Ingrese el nombre del producto: ")
        precio_nuevo_producto = int(input("Ingrese el precio del producto (sin IVA): "))
        perifericos.add((nombre_nuevo_producto, precio_nuevo_producto))
    print()
    agregar_productos = input("¿Desea agregar más productos? (S/N): ")
    print()

print()
print("Aquí está la ista actualizada de precios sin IVA: \n")
for producto, precio in perifericos:
    print(f"Producto: {producto}, Precio: ${precio}")
print()
num_productos = len(perifericos)
print(f"Usted tiene: {num_productos} tipos de productos.")  #Agrego esta línea para informar cuántos productos tiene.
print()

# Aquí importo la función para calcular el IVA y lo alojaré en un conjunto nuevo
# Recordar que la ruta es impuesto.iva y la función es calcular_iva()
from impuesto.iva import calcular_iva

# Creo vacío el set para guardar los productos con sus precios con el IVA agregado.
productos_con_iva = set()

# Genero un ciclo que va calculando el IVA de cada producto y lo va agregando al nuevo set
for producto, precio in perifericos:
    precio_con_iva = int(precio + calcular_iva(precio))
    productos_con_iva.add((producto, precio_con_iva))

# Genero un ciclo para imprimir el nuevo set con los productos con el IVA ya calculado y el precio ajustado.
print("Aquí está la lista de precios con IVA (19%): \n")
for producto, precio_con_iva in productos_con_iva:
    print(f"Producto: {producto}, Precio con IVA: ${precio_con_iva:.2f}")  # Aquí uso .2f que me permite limitar a 2 la cantidad de decimales
print()
