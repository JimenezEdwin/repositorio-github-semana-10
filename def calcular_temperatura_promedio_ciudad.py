def calcular_temperatura_promedio_ciudad(temperaturas, ciudades):
    """
    Calcula la temperatura promedio de cada ciudad durante todo el período.
    
    Args:
        temperaturas (list): Matriz 3D con temperaturas [ciudades][semanas][días].
        ciudades (list): Lista con los nombres de las ciudades.
    
    Returns:
        dict: Diccionario con nombres de ciudades como claves y sus temperaturas
              promedio como valores.
    """
    promedios = {}
    
    for i in range(len(temperaturas)):  # Iterar sobre ciudades
        suma_total = 0
        total_dias = 0
        for j in range(len(temperaturas[i])):  # Iterar sobre semanas
            suma_total += sum(temperaturas[i][j])  # Sumar temperaturas de la semana
            total_dias += len(temperaturas[i][j])  # Contar días en la semana
        if total_dias > 0:  # Evitar división por cero
            promedio = suma_total / total_dias
            promedios[ciudades[i]] = round(promedio, 2)  # Redondear a 2 decimales
        else:
            promedios[ciudades[i]] = 0  # Si no hay datos, asignar 0
    
    return promedios

# Datos de ejemplo (de la tarea anterior)
temperaturas = [
    [  # Quito
        [25, 26, 24, 23, 22, 21, 20],  # Semana 1
        [27, 28, 26, 25, 24, 23, 22]   # Semana 2
    ],
    [  # Cuenca
        [30, 29, 28, 27, 26, 25, 24],  # Semana 1
        [31, 30, 29, 28, 27, 26, 25]   # Semana 2
    ],
    [  # Santo Domingo
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1
        [22, 23, 24, 25, 26, 27, 28]   # Semana 2
    ]
]

ciudades = ["Quito", "Cuenca", "Santo Domingo"]

# Llamada a la función
resultados = calcular_temperatura_promedio_ciudad(temperaturas, ciudades)

# Mostrar resultados
for ciudad, promedio in resultados.items():
    print(f"Temperatura promedio de {ciudad}: {promedio}°C")