materia = input("Ingrese el nombre de la materia: ")
notas = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Nota {i+1} (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor ingresá un número válido.")

# Calcular promedio
promedio = sum(notas) / len(notas)

# Mostrar resultados
print("\n--- Resultado Final ---")
print(f"Materia: {materia}")
print(f"Notas: {notas}")
print(f"Promedio: {promedio:.2f}")
print(f"Te sacaste un {promedio:.2f} en {materia}")

# Mostrar si aprobó o no
if promedio >= 7:
    print("Estado: ¡Aprobado! 🎉")
else:
    print("Estado: Desaprobado 😓")
