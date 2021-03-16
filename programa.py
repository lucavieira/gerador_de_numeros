from time import sleep
from gerador import gerandor_de_numeros

print('-' * 35)
print(f'{"GERADOR DE NUMEROS".center(35)}')
print('-' * 35)
print(f'{"DIGITE O INTERVALO".center(35)}')
print('-' * 35)

comeco = int(input('De: '))
fim = int(input('Até: '))
qntd_numeros = int(input('Quantos numeros deseja sortear: '))
resultados = gerandor_de_numeros(comeco, fim, qntd_numeros)

print('-' * 35)
print(f'{"NUMEROS SORTEADOS".center(35)}')
print('-' * 35)

for resultado in resultados:
    sleep(1)
    print(resultado, end=' ')
