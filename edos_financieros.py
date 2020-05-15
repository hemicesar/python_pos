# ------------------------
# Nuevos objetivos
# Hacer variable y ajustar enmemoria el capital inicial.
# Comenzar a generar base de datos para diferenciar los productos que se trabajan.
# Capturar los datos directamete del lector de código de barras.
# Pasar el algoritmo a que trabaje con tecnologías web.
# Hacer visible el programa desde una terminal móvil.

suma_ventas = 0
# ------------------------
# Ciclo principal del Programa
continuar = True
while continuar:
# ------------------------
# Introducción al Programa
  print ("""\nBienvenido a Keep Money!
  \n\t Le ayudamos a diagnosticar las finanzas de su negocio
  \t y tomar acciones para mejorar su flujo de caja.""")


# ------------------------
# Definición de variables
  capital_inicial = 500
  num_articulo = 0
  num_venta = 0
  venta = 0
#  n = int(input("\n¿Hasta que posición de la serie de fibonacci quiere ver? "))
#  c = k = j = 1
#  l = [k]

# ------------------------
# Algoritmo que calcula el monto de una venta
  print ("\nSu capital inicial es: ", capital_inicial)

  vendo = True
  while vendo:
    articulo = float(input("\t\n Ingrese el valor del artículo: "))
    print("Valor del producto: ", articulo)
    num_articulo += 1
    #k,j = j, k + j
    #l.append(k) # Almacena el resultado en una lista
    #c = c + 1
    venta = articulo + venta
    vendo = ("s" == input("\nPresione s para registrar artículo adicional "))
    num_venta += 1
    print("\nArtículos vendidos: ", num_articulo)
    print("\nMonto de la venta: ", venta)
# ------------------------
# Imprime el resultado en pantalla


  suma_ventas = venta + suma_ventas
  capital_total = capital_inicial + suma_ventas
  print ("\nVentas realizadas: ", num_venta)
  print ("\nMonto ventas: ", suma_ventas)
  print ("\nSu nuevo capital es:", capital_total)

  continuar = ("s" == input("\nPresione s para registrar una nueva venta "))

print ("\n\tExelente trabajo!  Nos vemos mañana.")
