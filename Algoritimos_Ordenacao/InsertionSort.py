# Função INSERTION SORT que receba como parametro uma lista
def _insertionSort(vetor):
  
  # Verificando se o vetor possui mais de um elemento
  if len(vetor) > 1: 


    # Rodando a partir do segundo elemento da lista até o ultimo index da mesma
    for index in range(1, len(vetor)):

      # Marcando o elemento que será comparado com os anteriores a ele
      marcador = vetor[index]

      # Elemento que será comparado com o marcador
      comparacao = index -1


      # Enquanto o index da comparação for maior ou igual a 0 e o marcador for menor que  a comparação
      while comparacao >= 0 and marcador < vetor[comparacao]:

        # Afastando a comparação para o proximo index
        vetor[comparacao+1] = vetor[comparacao]

        # Atualizando o valor da comparação
        comparacao -= 1


      # Quando a comparação for menor que o marcador, o marcador será inserido depois da comparação
      vetor[comparacao+1] = marcador
  

