# Função BUCKET SORT que receba como parametro uma lista
def _bucketSort(vetor):

    # Crição do vetor resposta para o algoritmo
    resultado = []

    # Número máximo presente no vetor
    valor_maximo_vetor = max(vetor)

    # Tamanho do vetor
    tamanho_vetor = len(vetor)

    # Valor máximo divido pela quantidade do vetor
    tamanho_auxilio = valor_maximo_vetor/tamanho_vetor
 
    # Crição dos Buckets para o algoritmo ( Matriz com a quantidade de vetores total igual a quantidade de itens no vetor analisado )
    matriz = [[] for _ in range(tamanho_vetor)]
 

    # Para cada index entre 0 e o tamanho do vetor  
    for index in range(tamanho_vetor):

        # CRIAÇÃO DE UM INDEX VIRTUAL
        index_virtual = int(vetor[index]/tamanho_auxilio)

        # Se o index virtual for diferente do tamanho do vetor
        if index_virtual != tamanho_vetor:

            # Adicionar ao vetor da matriz o item do vetor analisado
            matriz[index_virtual].append(vetor[index])

        # Se o index virtual for igual do tamanho do vetor
        else:

            # Adicionar ao vetor anterior da matriz o item do vetor analisado
            matriz[tamanho_vetor - 1].append(vetor[index])
 

    # Para cada index entre 0 e o tamanho do vetor 
    for index in range(tamanho_vetor):

        # Se o vetor tenha algum item dentro
        if matriz[index]:

            # Ordenar cada vetor da matriz ( buckets )
            # O vetor da matriz recebe o mesmo vetor,porém ordenado
            matriz[index] = sorted(matriz[index])


    # Para cada index entre 0 e o tamanho do vetor
    for index in range(tamanho_vetor):

         # Se o vetor tenha algum item dentro
        if matriz[index]:

            # Concatenar os vetores da matriz na lista resposta
            resultado = resultado + matriz[index]
             

