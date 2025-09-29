
# 1. Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Antonio Vaca",
    "edad": 25,
    "ciudad": "Argentina",
    "profesion": "Ingeniero de Sistemas"
}

# 2. Acceder y modificar el valor de la clave "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])  # Mostrar la ciudad actual
informacion_personal["ciudad"] = "Ecuador"  # Modificar la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])  # Mostrar la ciudad actualizada

# 3. Verificar existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 939 576 465"  # Agregar número ficticio
    print("Teléfono agregado:", informacion_personal["telefono"])
else:
    print("La clave 'telefono' ya existe")

# 4. Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]  # Eliminar la clave "edad"
print("Clave 'edad' eliminada")

# 5. Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)