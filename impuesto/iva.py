'''
1.- Esta función calcula el IVA (en Chile) a un valor que sería el precio de un producto
2.- Ejemplo: El 19% de $10.000 arroja como resultado 10.000 * 0.19 = 1.900
3.- Esta función se encuentra dentro del archivo iva.py del módulo impuesto.
4.- Para importarla en el archivo use el comando: from impuesto.iva import calcular_iva
'''
# Función para calcular el IVA al 19% (IVA = Impuesto al Valor Agregado)
def calcular_iva(monto):
    return monto * 0.19