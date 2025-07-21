# ENUNCIADO del Teorema del Mono Infinito 🐒: 
# El teorema del mono infinito afirma que un mono pulsando teclas al azar sobre 
# un teclado durante un periodo de tiempo indefinido podrá escribir finalmente 
# cualquier texto dado. En el mundo angloparlante, se suele utilizar el Hamlet 
# de Shakespeare como ejemplo, mientras en el mundo hispanohablante se utiliza el Quijote de Cervantes

# El objetivo de este programa es comprobar mediante un sencillo programa
# cúal sería la posibilidad real de escribir distintos textos de forma aleatoria

# 1️⃣ Conseguir medir el tiempo de ejecución de un programa en Python

# La opción más sencilla es utilizar time

import time

# 📰 Aquí realmente lo que se está haciendo es definir una "decorador", que viene a ser una función que tiene
# como argumento una función, y llama a una envoltura o "wrapper" que le añade lógica adicional
def measure_time(function):
  '''
    Aquí se puede escribir documentación sobre la función
  '''
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = function(*args, **kwargs) # Aquí es donde se llama a la función que se pasa como argumento
    end_time = time.time()
    print(f"{function.__name__} ejecutada en: {end_time - start_time:.6f} segundos")
    return result
  return wrapper

# 📓 Ejemplo de ejecución:

@measure_time
def two_sums(nums, target):
  '''
  Esta función recibe una `lista` como primer argumento y un `número` para comprobar qué indices suman ese número
  '''
  for i in range(len(nums)):
    for j in range(len(nums)):
        
      if((nums[i] + nums[j]) == target):
        if(j == i):
          continue
        print([i, j])
        return [i, j]
  print("No results")

# 📓 Lo que va a ocurrir es que la función two_sums está definida con el decorador measure_time, por lo que
# siempre que se vaya a ejecutar, estrá envuelta por ella
# 🧪 Prueba:
# two_sums([1, 2, 3, 4, 5], 9)

# 2️⃣ Crear una función para medir el tiempo en el que tardar en escribirse una cadena de caracteres escogiendo carácteres al azar

# Primero, definimos una secuencia de caracteres sencilla
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# Utilizamos la biblioteca random para escoger carácteres al azar
import random

# Función de prueba para ver qué caracteres escoje al azar
@measure_time
def random_letter(number, chars):
  '''
  Recibe como argumento un `number` que determina el número de letras de una lista al azar que se desean escoger y devuelve por pantalla el resultado
  '''
  chosen_letters = []
  for _ in range(number):
    chosen_letters.append(random.choice(chars))
  print(f"Se han pedido {number} letras, y se han escogido: {chosen_letters}")
  return chosen_letters

# 🧪 Prueba:
# random_letter(30, chars)

# Una vez comprobada la lógica, definir una función para medir cáunto se tarda en escibir la palabra "banana"

@measure_time
def infinite_monkey(word, characters):
  '''
  Función que permite medir el tiempo en que, escogiendo una letra al azar de un conjunto de caracteres dado, se tarda en
  escribir una palabra
  '''
  shadow_word = "" # Guardamos una cadena vacía que será el lugar donde se irá construyendo
  attempt = 0 # Guardamos el número de intentos
  # total = 1e8
  counter = 0 # Establecemos un contador para recorrer el índice de las palabras
  
  # Iniciamos un bucle que se jecutará hasta que las palabras sean iguales
  while shadow_word != word:
    attempt += 1
    shadow_word += random.choice(characters) # Se escoge un carcacter al azar

    # print(f"{attempt/total:5.5f}%", end="\r") # Por si se quiere establecer un porcentaje en función de los intentos

    # if attempt >= total:
    #   print("Se ha excedido el número de intentos")
    #   break

    # Si la letra del contador es distinta, reinicia
    if shadow_word[counter] != word[counter]:
      shadow_word = ""
      counter = 0
      continue
    counter += 1

infinite_monkey("eduardo", chars)