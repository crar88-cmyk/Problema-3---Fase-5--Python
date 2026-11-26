# _______________________________________________________________

# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programacion
# Fase 5 - Evaluacion Final POA
# Problema 3: Control de inventario y reabastecimiento

# ________________________________________________________________
# Datos iniciales: matriz de inventario (minimo 5 articulos)
# ________________________________________________________________
inventario = [
    ["A001", "Teclado USB",        15, 20],
    ["A002", "Mouse inalambrico",  40, 25],
    ["A003", "Monitor 24 pulgadas", 5, 10],
    ["A004", "Cable HDMI",         30, 30],
    ["A005", "Memoria USB 64GB",    8, 15],
    ["A006", "Impresora laser",     3,  2],
]


# ________________________________________________________________
# Calcula la cantidad exacta a pedir
# ________________________________________________________________
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
   
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0



# ________________________________________________________________
def main():
    print("=" * 50)
    print("   INFORME DE REABASTECIMIENTO DE INVENTARIO")
    print("=" * 50)
    print(f"{'Articulo':<25}{'Cantidad a pedir':>20}")
    print("-" * 50)

    # Estructura repetitiva: recorre cada fila de la matriz
    for fila in inventario:
        codigo = fila[0]
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]

        cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"{nombre:<25}{cantidad:>20}")

    print("=" * 50)


main()

