# Función para calcular el descuento en una compra
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento basado en el monto total de la compra y un porcentaje de descuento.
    
    Args:
        monto_total (float): El monto total de la compra
        porcentaje_descuento (float, optional): Porcentaje de descuento. Por defecto es 10%.
    
    Returns:
        tuple: (monto_descuento, monto_final) donde monto_descuento es el valor del descuento
               y monto_final es el monto a pagar tras aplicar el descuento
    """
    monto_descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - monto_descuento
    return monto_descuento, monto_final

# Programa principal
def main():
    # Primera llamada a la función con el porcentaje por defecto (10%)
    monto1 = 1000
    descuento1, final1 = calcular_descuento(monto1)
    print(f"Compra 1: Monto total = ${monto1:.2f}")
    print(f"Descuento (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${final1:.2f}\n")

    # Segunda llamada a la función con un porcentaje personalizado (15%)
    monto2 = 2000
    porcentaje2 = 15
    descuento2, final2 = calcular_descuento(monto2, porcentaje2)
    print(f"Compra 2: Monto total = ${monto2:.2f}")
    print(f"Descuento ({porcentaje2}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${final2:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()