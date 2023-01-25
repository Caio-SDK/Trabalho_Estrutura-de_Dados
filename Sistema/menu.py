# Importações do sistema
from Sistema.validacao import Validacao
from Sistema.gerar_grafico_teste import Grafico

# Importações do Python
import sys
import os


# Classe do Menu
class Menu:


    # Mensagem de Bem-Vindo ao Usuário
    mensagem_bem_vindo = """
OLÁ!
SEJA BEM-VINDO(A) AO PROGRAMA DE TESTE PARA ALGORITMOS DE ORDENAÇÃO V.1
ESPERO QUE SUA EXPERIENCIA SEJA AGRÁDAVEL
"""

    # Opções do Usuario
    opcoes = """
[ 1  ] - Visualizar teste para entradas na ordem de 10 elevado a 1 ( 10^1 )
[ 2  ] - Visualizar teste para entradas na ordem de 10 elevado a 2 ( 10^2 )
[ 3  ] - Visualizar teste para entradas na ordem de 10 elevado a 3 ( 10^3 )
[ 4  ] - Visualizar teste para entradas na ordem de 10 elevado a 4 ( 10^4 )
[ 5  ] - Visualizar teste para entradas na ordem de 10 elevado a 5 ( 10^5 )
[ 6  ] - Visualizar teste para entradas na ordem de 10 elevado a 6 ( 10^6 )
[ 7  ] - Visualizar teste para entradas na ordem de 10 elevado a 7 ( 10^7 )
[ 8  ] - Visualizar teste para entradas na ordem de 10 elevado a 8 ( 10^8 )
[ 9  ] - Visualizar teste para entradas na ordem de 10 elevado a 9 ( 10^9 )
[ 10 ] - Visualizar teste para entradas na ordem de 10 elevado a 10 ( 10^10 )
[ 11 ] - Sair do programa
"""


    # Função que criará o menu principal para o usuário
    @staticmethod
    def menu_principal():

        # Exibir a mensagem de bem-vindo ao usuário
        print(Menu.mensagem_bem_vindo)

        while True:

            # Limpando o terminal para não haver poluição visual
            os.system("cls")
            
            # Exibir as Opções
            print(Menu.opcoes)

            # Entrada do Usuário
            opcao_usuario = Validacao._ValidacaoOpcoes("Digite sua opção: ", 1, 11)

            # Se a opção do usuário for sair do programa
            if opcao_usuario == 11:

                # Sair do programa
                sys.exit()

            # Chamando a função de geração de testes e gráfico
            Grafico._Ordenacao(opcao_usuario)
