from datetime import datetime, time, os
import locale

from errbot import BotPlugin, botcmd


class Datetime(BotPlugin):
    """Funções relacionadas a datas e horas"""

    def activate(self):
        super().activate()

        os.environ['TZ'] = '+3'
        time.tzset()
        pass

    @staticmethod
    def _get_date_time(fmt):
        dt = datetime.now()
        return dt.strftime(fmt)

    @botcmd
    def datetime(self, message, args):
        """Mostra a data e a hora no local atual"""
        return "A data e hora são {}".format(self._get_date_time('%x %X'))

    @botcmd
    def date(self, message, args):
        """Mostra a data atual no local atual"""
        return "A data é {}".format(self._get_date_time('%x'))

    @botcmd
    def time(self, message, args):
        """Mostra a hora atual no local atual"""
        return "O tempo é {}".format(self._get_date_time('%X'))

    @botcmd
    def strftime(self, message, args):
        """Data e / ou hora formatada usando strftime"""
        if not args:
            return "**Uso**: !datetime strftime <format>"
        return "A data e hora são {}".format(self._get_date_time(args))
