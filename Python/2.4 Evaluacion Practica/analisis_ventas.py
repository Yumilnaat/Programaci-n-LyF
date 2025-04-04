from functools import reduce


ventas = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

promedio = reduce(lambda acumulador, venta: acumulador + venta, ventas, 0) / len(ventas)

covercion_cambios = list(map(lambda venta: venta * 0.049, ventas))

filtrar_ventas = list(filter(lambda venta: venta > 150, covercion_cambios))

suma_ventas_filtradas = reduce(lambda acumulador, venta: acumulador + venta, filtrar_ventas)

print("Promedio de ventas: ", promedio)
print("Conversion a dolar: ",covercion_cambios)
print("Ventas filtradas: ",filtrar_ventas)
print("Suma de ventas filtradas: ",suma_ventas_filtradas)
