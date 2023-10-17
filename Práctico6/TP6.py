# 6.	Solicitar al usuario que ingrese los nombres de pila de
# los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’.
# A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
# a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
# b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

secondary_school_students=[]
primary_school_students=[]

while True:
    name_primary=input("Ingrese el nombre de cada estudiante de nivel primario (para finalizar escriba 'x'): ")
    if name_primary == "x":
        break
    primary_school_students.append(name_primary)
    

while True:
    name_secondary=input("Ingrese el nombre de cada estudiante de nivel secundario (para finalizar escriba 'x'): ")
    if name_secondary == "x":
        break
    secondary_school_students.append(name_secondary)
    
print("Los nombres de los alumnos del nivel primario son: ")
for element in primary_school_students:
    print(element)

print("Los nombres de los alumnos del nivel secundario son: ")
for element in secondary_school_students:
    print(element)

elements_repeat_primary = [item for item in primary_school_students if primary_school_students.count(item) > 1]
elements_repeat_primary = list(set(elements_repeat_primary))
print("Nombres de alumnos de nivel primario repetidos: ", elements_repeat_primary)

elements_repeat_secondary = [item for item in secondary_school_students if secondary_school_students.count(item) > 1]
elements_repeat_secondary = list(set(elements_repeat_secondary))
print("Nombres de alumnos de nivel secundario repetidos:", elements_repeat_secondary)

