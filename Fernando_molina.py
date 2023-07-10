import os
os.system("cls")

menu = """
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. salir
"""
listaEntrada = []
listaAsiento = []
plati = 0
gold = 0
silver = 0
ubicacionOcu = 0
ubicacionDis = 0
ubicacion = 0
lista_run = 0
ubic  = 0
nomb = input("Ingrese Su Nombre: ")
apel = input("Ingrese Su Apellido: ")

opc = int(input(menu))
def entradas():
    while True:
        try:
                entrada = int(input("Ingrese cantidad de entradas: "))
                if entrada <=3 and entrada >=1:
                        return entrada
                for i in range(1, 101):
                    if i in ubicacionDis:
                        print(f"Asiento {i}: Disponible")
                    elif i in ubicacionOcu:
                        print(f"Asiento {i}: ocupado")
                for i in range(entrada):
                    ubi = int(input("Seleccione una ubicación disponible: "))
                while ubi not in ubicacionDis:
                    print("Ubicación no disponible, seleccione otra ubicacion.")
                    ubi = int(input("Seleccione una ubicación disponible: "))
                    listaEntrada.append(ubic) 
                    ubicacionDis.remove(ubic)
                    ubicacionOcu.append(ubic)
                else:
                 print("La Cantidad Ingresada No Es Valida") 
        except:
            print("Ocurrio una excepcion")


def Mostrar_tabl():
    for i in range(1, 101):
        if i in ubicacionDis:
            print(f"Asiento {i}: Disponible")
        elif i in ubicacion:
            print(f"Asiento {i}: Vendido")

def lista():
    print(lista_run)

def Ganacias():
    pla = 0
    gold = 0
    sil = 0
    for ubicacion in listaEntrada:
        if ubicacion >= 1 or ubicacion <= 20:
            pla += 1
        elif ubicacion >= 21 or ubicacion <= 50:
            gold += 1
        elif ubicacion >= 51 or ubicacion <= 100:
            sil += 1
    run = input("Ingrese su RUN sin guiones ni puntos: ")
    lista_run.append(run)
    print(f"Se han comprado {ubicacionOcu}")
    print(f"""
    Entradas   |       Cantidad     | Precio
    -------------------------------------------------
    Platinum   |       {pla}        | {pla*120000}
    Gold       |       {gold}       | {gold*80000}
    Silver     |       {sil}        | {sil*50000}
    -------------------------------------------------
    """)
    print(f"Su RUN: {run}")
    print("¡Disfrute del evento!")





if opc == 2:
    Mostrar_tabl()
elif opc == 3:
    lista()
elif opc == 1:
    entradas()
    Mostrar_tabl()
elif opc == 4:
    Ganacias()
elif opc == 5:
    print(f"Muchas Gracias {nomb} {apel} ")
    print("10/07/2023") 
else:
    print("Error al ingresar")