import random

print("bienvenido a adivina el numero!")
name = input("cual es tu nombre:")
print("hola", name)

print("Tabla de posiciones")
archivo = open("datos_juego.txt", "r")
for linea in archivo:
    print(linea.strip())
    archivo.close

# Elegir dificultad
print("Seleccions la dificultad")
print("1. Facil (1-20)")
print("2. normal (1-50)")
print("3. dificil (1-100)")

dificultad = input("Elige una opcion: ")
if dificultad == "1":maximo = 20
elif dificultad == "2":maximo = 50
elif dificultad == "3":maximo = 100
else:print("Opcion no valida.")

print("vamos a jugar")

# Generate a random number between 1 and maximo
secret_number = random.randint(1, maximo)
puntos = 0

print("Estoy pensando en un numero entre 1 y maximo ADIVINALO.")

print("\nCrear listas")
lista1 = []

while True:
    try:
        # Ask the user for a guess
        user_guess = int(input("ingresa tu numero: "))

        # Calculate how close the guess is
        difference = abs(secret_number - user_guess)

        # Check if the guess is correct
        if user_guess == secret_number:
            puntos += 1
            lista1 += [name, puntos]
         
            with open("datos_juego.txt", "a") as archivo:
                archivo.write(str(lista1))
            print("Correcto", name, "adivinaste el numero!")
            print("puntos:", puntos)
            break

        # Give hints based on distance
        elif difference <= 2:
            print("muy, muy cerca!")

        elif difference <= 5:
            print("cerca pero no es el correcto.")

        elif difference <= 10:
            print("muy lejos.")

        elif difference <= 20: 
         print(" demaciado lejos")

        elif difference <= 50:
            print("ni jupiter esta tan lejos")

        elif difference <= 70:
            print ("nonono, que mal instinto, te pasaste por demaciado")

    # Prevent crashes if the user types text
    except ValueError:
        print("porfavor ingresa un numero valido.")