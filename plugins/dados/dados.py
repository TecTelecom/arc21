from errbot import BotPlugin, botcmd


class Dados(BotPlugin):
    """
    Rolar dados para suporte de jogo RPG
    """

    @botcmd(split_args_with=' ')  # flags a command
    def rolar(self, msg, args):  # a command callable with !tryme
        """
        Informar quantos dados e faces
        """
        dados = args[0]
        faces = args[1]

        return dados + " dados e " +  faces + " faces ".
