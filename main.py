# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre la serie Game of Thrones")
[Demo](https://replit.com/@Mirella02/Trivia-GO)
##
print ("Pondremos a prueba tus conocimientos")

nombre = input ("Ingresa tu nombre:  ")
# Es importante dar instrucciones sobre cómo jugar:
print ("\nHola", nombre, "responder las siguientes preguntas escribiendo la letra de la alternativa correcta y presionando 'Entrer' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1)",nombre,"¿Cuántos reinos existen en la serie Game of Thrones?")
print (" a.3")
print (" b.4")
print (" c.5")
print (" d.6")
print (" e.7")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input ("\nTu respuesta:  ")
while respuesta_1 not in ("a","b","c","d","e"):
  respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_1 == "e" : print ("Muy bien!")
else:
  print ("Incorecto!")

print("\n 2)", nombre, "en 'Game of Thrones' ¿En qué temporada nacen los Dragones 'Fire and Blood'?\n")
print (" a.Primera temporada")
print (" b.Segunda temporada")
print (" c.Tercera temporada")
print (" d.Cuarta temporada")
print (" e.Quinta temporada")
respuesta_2 = input("\nTu respuesta:  ")
while respuesta_2 not in ("a","b","c","d","e"):
  respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_2 == "a" :
   print("Muy bien!")
else:
  print ("Incorecto!")
  
print("\n 3)", nombre, "en 'Game of Thrones' ¿Cuál es el nombre del Lobo que tiene Jon Snow?\n")
print (" a. Lady")
print (" b. Ghost")
print (" c. Nymeria")
print (" d. Grey wind")
print (" e. Furry")
respuesta_3 = input("\nTu respuesta:  ")
if respuesta_3 == "b" : 
  print ("Muy bien!")
else:
  print ("Incorecto!")
while respuesta_3 not in ("a","b","c","d","e"):
  respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_3 == "b" : 
  print ("Muy bien!")

