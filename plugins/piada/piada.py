from errbot import BotPlugin, botcmd
from random import choice


class Piada(BotPlugin):
    """
    Escolha a forma de gerar uma piada.
    """

    @botcmd
    def ajuda(self, msg, args):
        """
        Abre o menu de ajuda para o usuário.
        """

        yield "Este bot conta piadas."
        yield "Pode ser usado da seguinte forma:"
        yield "1) piada"
        yield "2) piada <tema>"
        yield "onde <tema> é um tema de piada a sua escolha!"
        yield "Para saber os temas disponíveis, digite: tema"

    @botcmd(split_args_with=' ')
    def piada(self, msg, args):
        """
        Conta uma piada
        """

        if len(args[0]) > 0: # o usuário definiu um tema em especial
            pass
        else:
            # o usuário não definiu o tema, sortear
            pass

        try:
            aleatorio = int([1])
            tema = int([2])
            sair = int([3])
        except:
            yield "Olá, vamos começar!"
            yield "Digite [1] para piada aleatória."
            yield "Digite [2] para escolher o tema da piada."
            yield "Digite [3] para sair."


        # Informar se deseja uma piada aleatória ou por tema.
        # Forma de usar:
        # !piada
        # onde será retornado:
        # yield "Olá, vamos começar!"
        # yield "Digite [1] para piada aleatória."
        # yield "Digite [2] para escolher o tema da piada."
        # yield "Digite [3] para sair."

        # Se digitado [1] -> retornar piada aleatória
        # Se digitado [2] -> apresentar uma lista de temas, para o usuário escolher um.
        # Se digitado [3] -> retornar ("TE AGUARDAMOS DE VOLTA!")
        