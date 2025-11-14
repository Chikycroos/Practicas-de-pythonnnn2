correos = ["Gmail", "Hotmail", "Yahoo"]
print(correos[2])                               #imprimir la variable de la lista asignada en el numero 2

cantidad = len(correos)                             #imprime la cantidad de "Variables" que ahiga en la lista
print(cantidad)

correos.append("Outlook")                       #agrega la variable ala lista
print(correos)

correos.pop(2)                                      #elimina la variable con respecto al numero que tenga asignado
print(correos)

correos.remove("Gmail")                         #elimina la varieble con respecto al nombre que tenga 
print(correos)