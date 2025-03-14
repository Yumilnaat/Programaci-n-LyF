def preparar_cafe_am():
    return "Cafe Americano"

def preparar_cafe_olla():
    return "Cafe de Olla"

def ordenar_cafe(preparar_cafe, num_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(num_tazas)]
    return tazas_cafe

cafe_g_a = ordenar_cafe(preparar_cafe_olla, (int(input("Ingrese su orden: "))))

cafe_g_b = ordenar_cafe(preparar_cafe_am, (int(input("Ingrese su orden: "))))

print(cafe_g_a)
print(cafe_g_b)