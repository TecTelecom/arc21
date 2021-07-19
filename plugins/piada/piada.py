from errbot import BotPlugin, botcmd
from random import randint

class Piadas(BotPlugin):
    """
    Gerar piada de forma aleatória ou por tema
    De acordo com o comando usado pelo usuário
    """

    @botcmd(split_args_with=' ')
    def piada(self, msg, args):
        """
        Informar se deseja uma piada aleatória ou por tema.
        Forma de usar:
        !piada
        onde será retornado:
        Digite [1] para piada aleatória.
        Digite [2] para escolher o tema da piada.
        Digite [3] para sair.

        Se digitado [1] -> retornar piada aleatória
        Se digitado [2] -> apresentar uma lista de temas, para o usuário escolher um.
        Se digitado [3] -> retornar ("TE AGUARDAMOS DE VOLTA!")
        """
        print("Por favor, digite !piada")
        print("Em seguinda escolha o próxio passo")
        print("Sorria!!")
    