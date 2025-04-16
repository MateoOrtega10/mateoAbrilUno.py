materia = input("Ingrese el nombre de la materia: ") # Pide al usuario que ingrese el nombre de la materia
notas = []  # Crea una lista vacía para guardar las 3 notas


for i in range(3): # Bucle que se repite 3 veces para ingresar 3 notas
    while True: # Bucle para validar cada nota hasta que sea válida
        try:
            nota = float(input(f"Nota {i+1} (0-10): ")) # Pide al usuario una nota y la convierte a número decimal
            if 0 <= nota <= 10: # Verifica que la nota esté entre 0 y 10
                notas.append(nota) # Si es válida, la agrega a la lista de notas
                break # Sale del bucle 'while' para pasar a la siguiente nota
            else:
                print("La nota debe estar entre 0 y 10.")  # Mensaje si la nota no está en el rango permitido
        except ValueError: # Si el usuario ingresa algo que no se puede convertir a número
            print("Por favor ingresá un número válido.")# Muestra mensaje de error

# Calcular promedio
promedio = sum(notas) / len(notas)

# Mostrar resultados
print("\n--- Resultado Final ---")
print(f"Materia: {materia}")
print(f"Notas: {notas}")
print(f"Promedio: {promedio:.1f}")
print(f"Te sacaste un {promedio:.2f} en {materia}")

# Mostrar si aprobó o no
if promedio >= 7:
    print("Estado: ¡Aprobado! 🎉")
else:
    print("Estado: Desaprobado 😓pipipipi")
