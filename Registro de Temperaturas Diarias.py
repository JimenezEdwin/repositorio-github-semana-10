
# Definimos la matriz 3D: ciudades, días de la semana, semanas
# Ejemplo con 3 ciudades, 7 días, 2 semanas
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

# Nombres para mostrar resultados más claros
ciudades = ["Quito", "Cuenca", "Santo Domingo"]
semanas = ["Semana 1", "Semana 2"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i in range(len(temperaturas)):  # Iterar sobre ciudades
    print(f"\nPromedios para {ciudades[i]}:")
    for j in range(len(temperaturas[i])):  # Iterar sobre semanas
        suma_temperaturas = 0
        for k in range(len(temperaturas[i][j])):  # Iterar sobre días
            suma_temperaturas += temperaturas[i][j][k]
        promedio = suma_temperaturas / len(temperaturas[i][j])
        print(f"  {semanas[j]}: {promedio:.2f}°C")