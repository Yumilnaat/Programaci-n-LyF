def preparar_hotcakes():
    return "🥞"

def ordenar_hotcakes(num_piezas):
    hotcakes = [preparar_hotcakes() for _ in range(num_piezas)]
    return hotcakes

hotcakes_familia = ordenar_hotcakes(int(input('Ingresa tu orden: ')))

print(hotcakes_familia)