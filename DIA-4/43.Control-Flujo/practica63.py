habla_ingles = False
sabe_python = False

#Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte"

#"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

#"Para postularte, necesitas tener conocimientos de inglés"

#"Para postularte, necesitas saber programar en Python"

#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
elif sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")