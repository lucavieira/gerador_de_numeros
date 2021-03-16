from random import randint


def gerandor_de_numeros(comeco, fim, qntd_numeros):
    if qntd_numeros == 1:
        return randint(comeco, fim)
    else:
        resultados = list()
        for resultado in range(0, qntd_numeros):
            numero = randint(comeco, fim)
            if numero not in resultados:
                resultados.append(numero)
        return resultados
