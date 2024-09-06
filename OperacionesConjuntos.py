from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3


#Funcion para calcular la Union de conjuntos
def union_conjuntos(*conjuntos):
    conjuntoss = conjuntos[0]
    resultado = []
    for conjunto in conjuntoss:
        for elemento in conjunto:
            if elemento not in resultado:
                resultado.append(elemento)
    return resultado

#Funcion para calcular la interseccion entre multiples conjuntos
def interseccion(*conjuntos):
    conjuntoss = conjuntos[0]
    resultado = []
    
    if len(conjuntoss) == 0:
        return resultado
    elif len(conjuntoss) == 2:
        resultado = interseccion2(conjuntoss[0], conjuntoss[1])
        print("La interseccion es " + str(resultado))
        graficar_conjuntos_2(conjuntoss[0], conjuntoss[1], "A", "B")
    elif len(conjuntoss) == 3:
        resultado = interseccion3(conjuntoss[0], conjuntoss[1], conjuntoss[2])
        print(resultado)
        graficar_conjuntos_3(conjuntoss[0], conjuntoss[1], conjuntoss[2], "A", "B", "C")
    else:
        resultado = conjuntoss[0].copy()
        for conjunto in conjuntoss[1:]:
            for elemento in conjuntoss[0]:
                if not elemento in conjunto and elemento in resultado:
                    resultado.remove(elemento)
        print("La intersección general es " + str(resultado))


def interseccion2(a, b):
    
    resultado = a.copy()
    for elemento in a:
        if not elemento in b:
            resultado.remove(elemento)
    return resultado


def interseccion3(a, b, c):
    a_b = interseccion2(a, b)
    a_c = interseccion2(a, c)
    b_c = interseccion2(b, c)
    a_b_c = interseccion2(a, b_c)

    for elemento in a_b_c:
        if elemento in a_b:
            a_b.remove(elemento)
        if elemento in a_c:
            a_c.remove(elemento)
        if elemento in b_c:
            b_c.remove(elemento)

    x = "La intersección general es: " + str(a_b_c) + "\n" + "La intersección entre solo A y B es: "
    y = str(a_b) + "\n" + "La intersección entre solo A y C es: " + str(a_c) + "\n"
    z = "La intersección entre solo B y C es: " + str(b_c) 

    return x + y + z

#Funcion para calcular la diferencia entre varios conjuntos
def diferencia_conjuntos(conjunto_base, *conjuntos):
    conjuntoss = conjuntos[0]
    resultado = [elemento for elemento in conjunto_base if all(elemento not in conjunto for conjunto in conjuntoss)]
    return resultado

#Funcion para calcular la diferencia simetrica entre
def diferencia_simetrica_conjuntos(conjuntoA, conjuntoB):

    inter = interseccion2(conjuntoA, conjuntoB)

    resultado = []

    for elemento in conjuntoA:
        if elemento not in inter:
            resultado.append(elemento)

    for elemento in conjuntoB:
        if elemento not in inter:
            resultado.append(elemento)
        
    return resultado


def es_subconjunto(super, sub):
    for elemento in sub:
        if elemento not in super:
            return False

def graficar_conjuntos_2(a, b, nombre_a, nombre_b):

    #Se crean los set para graficar en matplotlib, set_a y set_b solo se usan para las operaciones de matplotlib
    set_a = set(a)
    set_b = set(b)
    set_intersection = set_a & set_b
    set_solo_a = set_a - set_intersection
    set_solo_b = set_b - set_intersection

    #Se crea el diagrama de Venn, se le asignana ids y nombres a los conjuntos [interseccion incluida]
    venn = venn2(subsets={'10':len(set_solo_a), '01':len(set_solo_b), '11':len(set_intersection)},
                 set_labels=(nombre_a, nombre_b))

    #Por cada conjunto [interseccion incluida] se concatenan sus valores casteados como texto para mostrarlos en la grafica
    if venn.get_label_by_id('10'):
        venn.get_label_by_id('10').set_text(', '.join(str(v) for v in set_solo_a))
    if venn.get_label_by_id('01'):
        venn.get_label_by_id('01').set_text(', '.join(str(v) for v in set_solo_b))
    if venn.get_label_by_id('11'):
        venn.get_label_by_id('11').set_text(', '.join(str(v) for v in set_intersection))

    plt.title("Diagrama de venn")
    plt.show()

def graficar_conjuntos_3(a, b, c, nombre_a, nombre_b, nombre_c):
    set_a = set(a)
    set_b = set(b)
    set_c = set(c)

    set_intersection = set_a & set_b & set_c

    set_a_y_b = (set_a & set_b) - set_intersection
    set_b_y_c = (set_b & set_c) - set_intersection
    set_a_y_c = (set_a & set_c) - set_intersection

    set_solo_a = set_a - set_b - set_c
    set_solo_b = set_b - set_a - set_c
    set_solo_c = set_c - set_a - set_b

    venn = venn3(subsets={'100':len(set_solo_a), '010': len(set_solo_b), '110': len(set_a_y_b), '001': len(set_solo_c),
                   '101': len(set_a_y_c), '011':len(set_b_y_c), '111':len(set_intersection)})

    if venn.get_label_by_id('100'):
        venn.get_label_by_id('100').set_text(', '.join(str(v) for v in set_solo_a))
    if venn.get_label_by_id('010'):
        venn.get_label_by_id('010').set_text(', '.join(str(v) for v in set_solo_b))
    if venn.get_label_by_id('110'):
        venn.get_label_by_id('110').set_text(', '.join(str(v) for v in set_a_y_b))
    if venn.get_label_by_id('001'):
        venn.get_label_by_id('001').set_text(', '.join(str(v) for v in set_solo_c))
    if venn.get_label_by_id('101'):
        venn.get_label_by_id('101').set_text(', '.join(str(v) for v in set_a_y_c))
    if venn.get_label_by_id('011'):
        venn.get_label_by_id('011').set_text(', '.join(str(v) for v in set_b_y_c))
    if venn.get_label_by_id('111'):
        venn.get_label_by_id('111').set_text(', '.join(str(v) for v in set_intersection))

    plt.title("Diagrama de venn")
    plt.show()

def ingresar_conjunto(cantidad):
    conjuntos = []
    print("Ingresa los elementos del conjunto (escribe 'fin' para terminar):")
    i = 0
    for i in range(cantidad):
        conjunto = []
        while True:
            elemento = input("Añade el elemento al conjunto #" + str(i+1) + ": ")

            if elemento.lower() == 'fin':  # Termina el ciclo si el usuario escribe 'fin'
                break
            else:
                conjunto.append(int(elemento))  # Agrega el elemento al conjunto
        conjuntos.append(conjunto)
    return conjuntos

def mostrar_menu(cant):

    print("\n--- Menú Principal ---")
    print("1. Realizar la unión de los conjuntos.")
    print("2. Realizar la intersección.")
    print("3. Realizar la diferencia entre los conjuntos.")
    if cant == 2:
        print("4. Realizar la diferencia simetrica.")
        print("5. Verificar subconjunto.")
    print("6. Salir")    


def opcion_1(conjuntos):

    resultado = union_conjuntos(conjuntos)
    print("La unión de los conjuntos es " + str(resultado))

def opcion_2(conjuntos):

    resultado = interseccion(conjuntos)
    print(resultado)

def opcion_3(conjuntos):

    indice = int(input("Dame el numero del conjunto al cual se le restaran el resto: "))
    elemento = conjuntos.pop(indice-1)
    resultado = diferencia_conjuntos(elemento, conjuntos) 
    print("El resultado de la resta es " + str(resultado))

def opcion_4(conjuntos):
     
    resultado = diferencia_simetrica_conjuntos(conjuntos[0], conjuntos[1])
    print("El resultado de la diferencia simetrica es " + str(resultado))

def opcion_5(conjuntos):

    if es_subconjunto(conjuntos[0], conjuntos[1]):
        print("El conjunto #2 es subconjunto del conjunto #2")
    else:
        print("El conjunto #2 no es subconjunto del conjunto #1")


def salir():
    print("\nSaliendo del programa...")
    exit()

def ejecutar_menu():
    cantidad = int(input("Cuantos conjuntos quiere ingresar: "))

    conjuntos = ingresar_conjunto(cantidad)

    while True:
        mostrar_menu(len(conjuntos))
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            opcion_1(conjuntos)
        elif opcion == "2":
            opcion_2(conjuntos)
        elif opcion == "3":
            opcion_3(conjuntos)
        elif opcion == "4":
            opcion_4(conjuntos)
        elif opcion == "5":
            opcion_5(conjuntos)
        elif opcion == "6":
            salir()
        else:
            print("\nOpción no válida. Intenta de nuevo.")

def main():
    ejecutar_menu()

main()