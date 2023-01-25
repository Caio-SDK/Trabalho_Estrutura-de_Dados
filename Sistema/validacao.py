# Importações do Python
import sys


# Classe de Validação
class Validacao:


    # Definição de um método estático para validação de números inteiros
    @staticmethod
    def _ValidacaoNumeroInteiro(mensagem):

        while True:

            try:

                numero_inteiro = int(input(mensagem))
                return numero_inteiro

            except (KeyboardInterrupt):
                
                print("\nObrigado por testar!!!")
                sys.exit()

            except:

                print("Por favor digite um número válido!!!")

    
    # Definição de um método estático para validação de números decimais
    @staticmethod
    def _ValidacaoNumeroDecimal(mensagem, casas_decimais, nota = False):

        while True:

            try:

                numero_decimal = float(input(mensagem))

                if nota and numero_decimal >= 0 and numero_decimal <= 10:
                    
                    return round(numero_decimal, casas_decimais)
                
                else:

                    raise TypeError

            except (KeyboardInterrupt):

                print("\nObrigado por testar!!!")
                sys.exit()

            except:

                print("Por favor digite um número válido!!!")


    # Definição de um método estático para validação de strings válidas
    @staticmethod
    def _ValidacaoNome(mensagem):

        while True:

            nome = input(mensagem)

            if nome.isnumeric():

                print("Por favor digite um nome válido!!!")

            else:
                return nome
    

    # Definição de um método estático para validação de opções válidas no menu interativo
    @staticmethod
    def _ValidacaoOpcoes(mensagem, limite_minino, limite_maximo):

        while True:

            try:

                opcao_desejada = Validacao._ValidacaoNumeroInteiro(mensagem)

                if opcao_desejada >= limite_minino and opcao_desejada <= limite_maximo:

                    return opcao_desejada
                
                else:

                    print("Digite uma opção válida!!!")
            
            except KeyboardInterrupt:

                print("\nObrigado por testar!!!")
                sys.exit()