# Declaración de año actual
año_actual = 2024

# Entrada de datos del usuario
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

# Cálculo del año de nacimiento
año_nacimiento = año_actual - edad
año_nacimiento -= 1

# Mensaje inicial
print("¡Genial!")

print("Entonces naciste en el año " + str(año_nacimiento) + ".")

# Pregunta al usuario si el cálculo es correcto
respuesta = input("¿He acertado? (Sí/No) ")

# Condicional para imprimir el mensaje adecuado
if respuesta == "Sí":
    print("Entonces naciste en el año " + str(año_nacimiento) + ".")
else:
    print("Hola " + nombre + ", ¿cuál es tu año de nacimiento correcto?")
    año_nacimiento_correcto = int(input("Por favor, introduce tu año de nacimiento: "))
    print("Gracias, " + nombre + ". Ahora sé que naciste en el año " + str(año_nacimiento_correcto) + ".")