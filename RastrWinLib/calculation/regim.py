# -*- coding: utf-8 -*-
from time import time, localtime, strftime

from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.tools.tools import Tools


class SteadyState:
    """
    Расчет режима, par – строка дополнительных параметров. Параметры могут быть следующими:
    "" – c параметрами по умолчанию;
    "p" – расчет с плоского старта;
    "z" – отключение стартового алгоритма;
    "c" – отключение контроля данных;
    "r" – отключение подготовки данных (можно использовать при повторном расчете режима
    с измененными значениями узловых мощностей и модулей напряжения).
    """

    def __init__(self,
                 rastr_win=RASTR,
                 par='',
                 switch_command_line=False):
        """

        :param rastr_win: COM - объект Rastr.Astra (win32com);
        :param par:
        :param switch_command_line:
        """
        self.rastr_win = rastr_win
        self.par = par
        self.switch_command_line = switch_command_line

    def __bool__(self):
        return self.switch_command_line

    def rgm(self):
        if self.switch_command_line is not False:
            start_time = time()
        else:
            start_time = 0
        kod = self.rastr_win.Rgm(self.par)
        if self.switch_command_line is not False:
            print(f'{Tools.separator_noun}\n'
                  f'Запуск "Расчет режима":\n'
                  f'\tСообщение о результатх расчета УР: {kod}\n')
            if kod != 0:
                print('\t\tРежим не сбалансирован!')
            elif kod == 0:
                print('\t\tРасчет УР завершен успешно!')
        if self.switch_command_line is not False:
            time_calc = time() - start_time
            print(
                f'\tВремя расчета режима: {strftime("M: %M [минут] S: %S [секунд]", localtime(time_calc))} '
                f'(Seconds: {"%.2f" % time_calc} [секунд])')
        print(Tools.separator_noun)
        return kod
