fechaIn = input("Ingrese la fecha: dia,dd/mm ")
fecha = fechaIn.split(",")
dia = fecha[0]
numero = int(fecha[1].split("/")[0])
mes = int(fecha[1].split("/")[1])

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
if not dia.lower() in dias or mes > 12 or numero > 31:
    print("Se produjo un error")
elif dia == "lunes" or dia == "martes" or dia == "miercoles":
    examen = input("Ingrese si hay examen: Y/N ")
    if (examen.lower() == "y"):
        aprobados = int(input("Ingrese la cantidad de aprobados: "))
        no_aprobados = int(input("Ingrese la cantidad de No aprobados: "))
        prom = ((aprobados * 100) / (aprobados + no_aprobados))
        print("El porcentaje de alumnos aprobados es de: ", prom, "%")
        print("El programa ha finalizado.")
    else:
        print("El programa ha finalizado.")
elif dia == "jueves":
    asis = int(input("Ingrese el porcentaje de asistencia: "))
    if asis > 50:
        print("Asistió la mayoría")
        print("El programa ha finalizado.")
    else:
        print("No asistió la mayoría")
        print("El programa ha finalizado.")
else: 
    if numero == 1 and (mes == 1 or mes == 7):
        print("Comienzo de nuevo Ciclo")    
        alumnos = int(input("Ingrese la cantidad de alumnos del ciclo: "))
        arancel = int(input("Ingrese el arancel por alumno: $"))
        ingreso_total = alumnos * arancel 
        print("El ingreso total será de: $", ingreso_total)
        print("El programa ha finalizado.")
