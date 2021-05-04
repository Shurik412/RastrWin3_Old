# -*- coding: utf-8 -*-
# Модель системы возбуждения типа Alstom_ControGen V3_lite,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: Alstom2 simp.xmldev.
# Параметры модели Alstom2 simp.xmldev заносятся в таблицу «ВозбудителиIEEE».
from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа Alstom_ControGen V3_lite,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: Alstom2 simp.xmldev.
    Параметры модели Alstom2 simp.xmldev заносятся в таблицу «ВозбудителиIEEE».
    """
    RPQlim: float = 1  # Блокировка ОМВ
    TRFout: float = 1  # Блокировка РФ
    Se1: float = 1.05  # (1.05 ... 1.1) Максимальное ограничение уставки но напряжению
    Ka: float = 10  # (10...100) Коэффициент усиления регулятора напряжения
    Vamax: float = None  # Максимальное ограничение регулятора напряжения
    Vamin: float = None  # Минимальное ограничение регулятора напряжения
