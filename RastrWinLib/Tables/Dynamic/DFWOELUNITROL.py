# -*- coding: utf-8 -*-
# Модуль переменных таблицы  "БОР UNITROL" RastrWin3


class DFWOELUNITROL:
    """

    """
    table: str = 'DFWOELUNITROL'  # название таблицы
    table_name: str = '"БОР UNITROL"'

    sel: str = 'sel'  # Отметка
    sta: str = 'sta'  # Состояние БОР
    Id: str = 'Id'  # N БОР Номер БОР
    Name: str = 'Name'  # Название БОР
    ModelType: str = 'ModelType'  # Модель БОР
    Brand: str = 'Brand'  # Марка БОР
    CustomModel: str = 'CustomModel'  # Модель в конструкторе

    # ток
    IfMax: str = 'IfMax'  # Максимальный ток возбуждения
    Ifth: str = 'Ifth'  # Максимальный ток возбуждения по нагреву

    # Коэффициента
    KexpIf: str = 'KexpIf'  # Показатель степени тепловой характеристики
    KR3: str = 'KR3'  # Коэффициент усиления ограничения
    KR3i: str = 'KR3i'  # Дополнительный коэффициент усиления ограничения
    Kth: str = 'Kth'  # Коэффициент усиления переключателя теплового канала
    KToF: str = 'KToF'  # Постоянная интегрирования
    KcF: str = 'KcF'  # Постоянная охлаждения
    KhF: str = 'KhF'  # Постоянная обратной время-токовой зависимости

    # времена
    Tc13: str = 'Tc13'  # Постоянная времени
    Tc23: str = 'Tc23'  # Постоянная времени
    Tb13: str = 'Tb13'  # Постоянная времени
    Tb23: str = 'Tb23'  # Постоянная времени
    Tdel: str = 'Tdel'  # Tвыд Выдержка времени

    Vamax: str = 'Vamax'  # Максимальное ограничение регулятора
    Vamin: str = 'Vamin'  # Минимальное ограничение регулятора

    TRFout: str = 'TRFout'  # Тип регулятора
    Tr: str = 'Tr'  # Постоянная времени измерительного фильтра
    Output: str = 'Output'  # Выход  Режим выхода


class DFWOELUNITROL_Description:
    """

    """