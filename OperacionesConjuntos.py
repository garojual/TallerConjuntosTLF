
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3


#Funcion para calcular la Union de conjuntos
def union_conjuntos(*conjuntos):
    resultado = []
    for conjunto in conjuntos:
        for elemento in conjunto:
            if elemento not in resultado:
                resultado.append(elemento)
    return resultado

#Funcion para calcular la interseccion entre multiples conjuntos
def interseccion(*conjuntos):
    if len(conjuntos) == 0:
        return []
    resultado = conjuntos[0]

    for conjunto in conjuntos[1:]:
        for elemento in resultado:
            if not elemento in conjunto:
                resultado.remove(elemento)
    return resultado

#Funcion para calcular la diferencia entre varios conjuntos
def diferencia_conjuntos(conjunto_base, *conjuntos):
    resultado = [elemento for elemento in conjunto_base if all(elemento not in conjunto for conjunto in conjuntos)]
    return resultado

#Funcion para calcular la diferencia simetrica entre
def diferencia_simetrica_conjuntos(*conjuntos):
    resultado = []
    historial = []
    for conjunto in conjuntos:
        for elemento in conjunto:
            if elemento not in resultado and elemento not in historial:
                resultado.append(elemento)
            elif elemento not in historial:
                resultado.remove(elemento)
                historial.append(elemento)
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

def main():
    a = [1,2,3,4]
    b = [3,4,5,6,7]
    c = [2,3,8,9]
    #graficar_conjuntos_2(a,b, "A", "B")
    graficar_conjuntos_3(a,b,c, "A", "B", "C")

main()