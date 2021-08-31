# -*- coding: utf-8 -*-

class Tools:
    separator_noun = '--------------------------------------------------------'
    separator_two = '==================================================================='  # Вывод get
    separator_star = '*******************************************************'  #
    separator_grid = '#########################################################'  # для LoadFile, Save
    separator_slash = '////////////////////////////////////////////////////////'
    separator_space = '                                                         '
    separator_taxi = '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-'

    error_text = 'ERROR: '

    switch_command_line_doc = 'True/False - вывод сообщений в протокол.'
    RastrDoc = 'COM - объект Rastr.Astra (win32com)'


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


if __name__ == "__main__":
    print(changing_number_of_semicolons(number=15315.00515, digits=5))