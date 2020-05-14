



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

  venta = float(input("\t Ingresa el monto de la venta: "))
  print("El valor de tu venta es: ", venta)
#  n = int(input("\n¿Hasta que posición de la serie de fibonacci quiere ver? "))
#  c = k = j = 1
#  l = [k]
  cantidad_vtas = 315
  #monto_vtas =
# ------------------------
# Algoritmo que calcula la serie de Fibonacci
  vendo = True
  while vendo:
    #k,j = j, k + j
    #l.append(k) # Almacena el resultado en una lista
    #c = c + 1
    venta = venta + cantidad_vtas
    vendo = ("S" == input("\n¿Desea registrar otra venta? S/n "))
# ------------------------
# Imprime el resultado en pantalla
  #print (l)

  print("El número de ventas realizadas fue de: ", venta)
  continuar = ("s" == input("\nPresione s para registrar una nueva venta "))
