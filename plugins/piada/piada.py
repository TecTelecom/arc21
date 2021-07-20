from errbot import BotPlugin, botcmd
from random import randint

class Piadas(BotPlugin):
    """
    Gerar piada de forma aleatória ou por tema
    De acordo com o comando usado pelo usuário
    """

    @botcmd(split_args_with=' ')
    def piada(self, msg, args):
        
        try:
            aleatorio = int(args[1])
            tema = int(args[2])
            sair = int(args[3])

        except:

            yield "Olá, vamos começar!"
            yield "Digite [1] para piada aleatória."
            yield "Digite [2] para escolher o tema da piada."
            yield "Digite [3] para sair."

        if aleatorio == 1:
            foo = ['Piada 1', 'Piada 2', 'Piada 3', 'Piada 4', 'Piada 5']
            print(random.choice(foo))
        if tema == 2:
            print(list['tema1', 'tema2', 'tema3'])
        if sair == 3:
            print(fim)

    def fim():       
        try:
            raise KeyboardInterrupt

        finally:
            print('Goodbye, world!')



        """
        Informar se deseja uma piada aleatória ou por tema.
        Forma de usar:
        !piada
        onde será retornado:
        yield "Olá, vamos começar!"
        yield "Digite [1] para piada aleatória."
        yield "Digite [2] para escolher o tema da piada."
        yield "Digite [3] para sair."

        Se digitado [1] -> retornar piada aleatória
        Se digitado [2] -> apresentar uma lista de temas, para o usuário escolher um.
        Se digitado [3] -> retornar ("TE AGUARDAMOS DE VOLTA!")
        """
    