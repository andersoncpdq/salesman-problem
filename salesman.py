#!/usr/bin/env/python2

 ##############################################
 #      Trabalho de Teoria dos Grafos         # 
 #     Prof: Valdisio Viana  - 2014.2         #
 #  por Rodrigo Magalhaes, Anderson Couto e   #
 #              Herique Guedes                #
 ##############################################

import random

TAM_M = 12

def gera_ciclo(inicio, fim, tam):
    ciclo = random.sample(range(inicio, fim + 1), tam)
    return ciclo

def matriz_arquivo():
    arquivo = open('entrada.txt' , 'r')
    matriz = [ map(int, linha.split(' ')) for linha in arquivo ]
    return matriz

def pega_pares(lista):
    pares = []
    for i in range(len(lista)-1):
        pares.append([lista[i], lista[i+1]])
    pares.append([lista[-1], lista[0]])
    
    return pares

def custo_total(matriz, lista):
    custo = 0
    
    pares = pega_pares(lista)
    for n in pares:
        a = n[0] - 1
        b = n[1] - 1
        custo = matriz[a][b] + custo

    return custo

def mais_distante(matriz, ciclo_inicial):
    print '\n\n#################### INICIANDO ######################'
    print 'Ciclo inicial: ', ciclo_inicial
    
    while len(ciclo_inicial) < TAM_M:
        distancia_vertice = -1
        custo = 1000000
        vertice = -1

        for linha in range(0, TAM_M):
            if not linha in ciclo_inicial:
                for coluna in range(0, TAM_M):
                    if coluna in ciclo_inicial:
                        if matriz[linha][coluna] > distancia_vertice:
                            distancia_vertice = matriz[linha][coluna]
                            vertice = linha

        print '\nVertice mais distante %d' % (vertice + 1)

        pares = pega_pares(ciclo_inicial)
        for aresta in pares:
            calculo_custo = (matriz[vertice][aresta[0]] + matriz[vertice][aresta[1]] - matriz[aresta[0]][aresta[1]])
            if  calculo_custo < custo:
                novo_ciclo = list(ciclo_inicial)
                custo = calculo_custo
                novo_ciclo.insert((ciclo_inicial.index(aresta[0]) + 1), vertice)

        passos = list(novo_ciclo)
        passos = [x + 1 for x in passos]
        print 'Novo ciclo: ', passos
        ciclo_inicial = list(novo_ciclo)

    ciclo_inicial = [x + 1 for x in ciclo_inicial]

    print '\n\n###################### FINAL ########################'
    ciclo_final = list(ciclo_inicial)
    ciclo_final.append(ciclo_final[0])
    print 'Ciclo: ', ciclo_final

    print 'Custo Total: ', custo_total(matriz, ciclo_inicial)
    print '#####################################################\n'

def mais_proximo(matriz, ciclo_inicial):
    print '\n\n#################### INICIANDO ######################'
    print 'Ciclo inicial: ', ciclo_inicial
    
    while len(ciclo_inicial) < TAM_M:
        distancia_vertice = 1000000
        custo = 1000000
        vertice = -1

        for linha in range(0, TAM_M):
            if not linha in ciclo_inicial:
                for coluna in range(0, TAM_M):
                    if coluna in ciclo_inicial:
                        if matriz[linha][coluna] < distancia_vertice:
                            distancia_vertice = matriz[linha][coluna]
                            vertice = linha

        print '\nVertice mais distante %d' % (vertice + 1)

        pares = pega_pares(ciclo_inicial)
        for aresta in pares:
            calculo_custo = (matriz[vertice][aresta[0]] + matriz[vertice][aresta[1]] - matriz[aresta[0]][aresta[1]])
            if  calculo_custo < custo:
                novo_ciclo = list(ciclo_inicial)
                custo = calculo_custo
                novo_ciclo.insert((ciclo_inicial.index(aresta[0]) + 1), vertice)

        passos = list(novo_ciclo)
        passos = [x + 1 for x in passos]
        print 'Novo ciclo: ', passos
        ciclo_inicial = list(novo_ciclo)

    ciclo_inicial = [x + 1 for x in ciclo_inicial]

    print '\n\n###################### FINAL ########################'
    ciclo_final = list(ciclo_inicial)
    ciclo_final.append(ciclo_final[0])
    print 'Ciclo: ', ciclo_final

    print 'Custo Total: ', custo_total(matriz, ciclo_inicial)
    print '#####################################################\n'
    
# Inicio do programa
print '#####################################################'
print '####        Problema do Caixeiro Viajante        ####'
print '####           Heuristica de Insercao            ####'
print '####         Matriz 12x12 (entrada.txt)          ####'
print '#####################################################\n'

print 'Gerando ciclo inicial aleatorio de tamanho 3...'
ciclo_inicial = gera_ciclo(1, TAM_M, 3)
print ciclo_inicial

# Transformando para o equivalente (ie. Vetor iniciando em 0)
ciclo_inicial = [x - 1 for x in ciclo_inicial]

# Ler matriz do arquivo
matriz = matriz_arquivo()

criterio = -1
while criterio:
    criterio = input('\nQual criterio voce deseja?\n(1) Mais proximo | (2) Mais distante | (0) Sair\n')

    if criterio == 1:
        mais_proximo(matriz, ciclo_inicial)
    elif criterio == 2:
        mais_distante(matriz, ciclo_inicial)
    elif criterio == 0:
        print '\nSaiu.'
    else:
        print '\nInvalido!'
