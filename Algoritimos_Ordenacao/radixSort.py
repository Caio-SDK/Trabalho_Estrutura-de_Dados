# Função RADIX SORT que receba como parametro uma lista
def _radixSort(vetor):

    # Pegar o número máximo dentro do vetor
    maior_numero_vetor = max(vetor)

    # Quantidade máxima de digitos necessários para o algoritmo
    quantidade_maxima_digitos = len(str(maior_numero_vetor))


    # Para cada digito entre 0 e a quantidade maxima de digitos
    for digito in range(0, quantidade_maxima_digitos):

        # Criação da matriz que armazenará a filtragem dos números
        matriz = [[] for _ in range(10)]


        # Para cada número dentro do vetor
        for numero in vetor:

            # Pegango o index da matriz para saber em qual vetor o número será adicionado
            index_matriz = (numero // (10 ** digito)) % 10

            # Adicionar no vetor da matriz o número do vetor analisado 
            matriz[index_matriz].append(numero)


        # Crição do vetor resposta para o algoritmo
        resultado = []


        # Para cada index entre 0 e 10
        for index in range(10):

            # Se o vetor tenha algum item dentro
            if matriz[index]:

                # Concatenar os vetores da matriz na lista resposta
                resultado = resultado + matriz[index]


        # Vetor receberá a matriz concatenada
        vetor = resultado

