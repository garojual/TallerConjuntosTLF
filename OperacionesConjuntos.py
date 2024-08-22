
class OperacionesConjuntos:

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
