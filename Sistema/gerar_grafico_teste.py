# Importações dos algoritmos de ordenação
from Algoritimos_Ordenacao.mergeSort import _mergeSort
from Algoritimos_Ordenacao.InsertionSort import _insertionSort
from Algoritimos_Ordenacao.quickSort import _quickSort
from Algoritimos_Ordenacao.bucketSort import _bucketSort
from Algoritimos_Ordenacao.radixSort import _radixSort

# Importações do Python
import matplotlib.pyplot as plt
from time import time
from random import shuffle


# Classe do Gráfico
class Grafico:

    # Função que chamará todos os algortimos de ordenação e criaráo gráfico
    @staticmethod
    def _Ordenacao(numero):

        # Declarando os vetores para testes
        vetor = list(range(1, (10 ** numero)+1))

        # Tornando o vetor criado em um vetor aleatório
        shuffle(vetor)

        # Declarando variaveis necessarias para o gráfico
        dados_grafico = []
        eixo_horizontal = ['Merge Sort', 'Insertion Sort', 'Quick Sort', 'Bucket Sort', 'Radix Sort']

        # ORDENAÇÃO USANDO 'MERGE-SORT'

        try:

            # Tempo antes do teste
            antes_do_teste_merge = time()

            # Função de MergSort
            _mergeSort(vetor)

            depois_do_teste_merge = time()

            # Tempo total de execução da ordenação em segundos
            total_merge = (depois_do_teste_merge - antes_do_teste_merge)

            # Adicionando esse total de execução aos dados necessarios para o gráfico
            dados_grafico.append(total_merge)

            print(f"MERGE SORT: COMPLETED")
            
        except:

            eixo_horizontal.remove('Merge Sort')

            print(f"MERGE SORT: ERROR")


        # ORDENAÇÃO USANDO 'INSERTION-SORT'

        try:

            if numero >= 8:

                raise ValueError

            else:

                # Tempo antes do teste
                antes_do_teste_insertion = time()
            
                # Função de InsertionSort
                _insertionSort(vetor)

                depois_do_teste_insertion = time()

                # Tempo total de execução da ordenação em segundos
                total_insertion = (depois_do_teste_insertion - antes_do_teste_insertion)

                # Adicionando esse total de execução aos dados necessarios para o gráfico
                dados_grafico.append(total_insertion)

                print(f"INSERTION SORT: COMPLETED")

        except:

            eixo_horizontal.remove('Insertion Sort')

            print(f"INSERTION SORT: ERROR")


        # ORDENAÇÃO USANDO 'QUICK-SORT'

        try:

            
            if numero >= 3:

                raise ValueError

            else:

                # Tempo antes do teste
                antes_do_teste_quick = time()

                # Função de QuickSort
                _quickSort(vetor, 0, len(vetor)-1)

                depois_do_teste_quick = time()

                # Tempo total de execução da ordenação em segundos
                total_quick = (depois_do_teste_quick - antes_do_teste_quick)

                # Adicionando esse total de execução aos dados necessarios para o gráfico
                dados_grafico.append(total_quick)

                print(f"QUICK SORT: COMPLETED")

        except:

            eixo_horizontal.remove('Quick Sort')

            print(f"QUICK SORT: ERROR")


        # ORDENAÇÃO USANDO 'BUCKET-SORT'

        try:

            # Tempo antes do teste
            antes_do_teste_bucket = time()

            # Função de BucketSort
            _bucketSort(vetor)

            depois_do_teste_bucket = time()

            # Tempo total de execução da ordenação em segundos
            total_bucket = (depois_do_teste_bucket - antes_do_teste_bucket)

            # Adicionando esse total de execução aos dados necessarios para o gráfico
            dados_grafico.append(total_bucket)

            print(f"BUCKET SORT: COMPLETED")
        
        except:

            eixo_horizontal.remove('Bucket Sort')

            print(f"BUCKET SORT: ERROR")


        # ORDENAÇÃO USANDO 'RADIX-SORT'

        try:

            if numero >= 8:

                raise ValueError

            else:

                # Tempo antes do teste
                antes_do_teste_radix = time()

                # Função de RadixSort
                _radixSort(vetor)

                depois_do_teste_radix = time()

                # Tempo total de execução da ordenação em segundos
                total_radix = (depois_do_teste_radix - antes_do_teste_radix)

                # Adicionando esse total de execução aos dados necessarios para o gráfico
                dados_grafico.append(total_radix)

                print(f"RADIX SORT: COMPLETED")
        
        except:

            eixo_horizontal.remove('Radix Sort')

            print(f"RADIX SORT: ERROR")


        # Criação do gráfico
        plt.bar(eixo_horizontal, dados_grafico)

        # Mostrar na tela esse grafico
        plt.show()



