def preparar_hotdog():
    return "🌭"

def preparar_hamborguesa():
    return "🍔"

def preparar_pizza():
    return "🍕"

def calc_bonus(num_porciones):
    if (num_porciones > 2):
        return "🥤gratis"
    else:
        return ""

def ordenar_alm(preparar_alm, num_porciones):
    alimentos = [preparar_alm() for _ in range(num_porciones)]
    bonus = calc_bonus(num_porciones)
    return alimentos, bonus

orden_g_a = ordenar_alm(preparar_hotdog, (int(input("Ingrese su orden: "))))

orden_g_b = ordenar_alm(preparar_hamborguesa, (int(input("Ingrese su orden: "))))

orden_g_c = ordenar_alm(preparar_pizza, (int(input("Ingrese su orden: "))))


print(orden_g_a)
print(orden_g_b)
print(orden_g_c)