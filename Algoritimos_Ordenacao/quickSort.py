from time import time
from random import shuffle

# Função para encontrar a posição da partição
def _pegar_particao(vetor, tamanho_minimo_vetor, tamanho_maximo_vetor):
 
    # Último número do vetor virtual
    ultimo_numero_vetor_virtual = vetor[tamanho_maximo_vetor]
 
    # Declaração da partição
    particao = tamanho_minimo_vetor - 1
 

    # Para cada index entre o tamanho minino e o tamanho máximo
    for index in range(tamanho_minimo_vetor, tamanho_maximo_vetor):

        # Se o número analisado for menor ou igual ao último número do vetor virtual atual
        if vetor[index] <= ultimo_numero_vetor_virtual:
 
            # A partição passa a ser incrementado em 1
            particao += 1
 
            (vetor[particao], vetor[index]) = (vetor[index], vetor[particao])
 
    (vetor[particao + 1], vetor[tamanho_maximo_vetor]) = (vetor[tamanho_maximo_vetor], vetor[particao + 1])
 

    # Retornar o valor atual da partição incrementado em 1
    return particao + 1
 
 
# Função QUICK SORT que receba como parametro uma lista, tamanho mínimo do vetor e tamanho máximo do vetor
def _quickSort(vetor, tamanho_minimo_vetor, tamanho_maximo_vetor):


    # Se o tamanho minno do vetor for menor que o tamanho máximo
    if tamanho_minimo_vetor < tamanho_maximo_vetor:
 
        # Pegar partição do vetor virtual
        particao = _pegar_particao(vetor, tamanho_minimo_vetor, tamanho_maximo_vetor)
 
        # Momento em que há recursividade da função
        _quickSort(vetor, tamanho_minimo_vetor, particao - 1)
        _quickSort(vetor, particao + 1, tamanho_maximo_vetor)

