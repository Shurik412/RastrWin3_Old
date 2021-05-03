# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения типа КОСУР_БСВ,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.АРВ: Kosur2bsv.xmldev.
# Параметры модели Kosur2bsv.xmldev заносятся в таблицу «АРВ (ИД)».
# Типовые значение параметров настройки, приняты согласно информации
# от производителя системы возбуждения. В случае наличия листинга настроек
# для конкретного энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель автоматического регулятора возбуждения типа КОСУР_БСВ, реализованная в ПК RUSTab,
     состоит из одного макроблока:
    1.АРВ: Kosur2bsv.xmldev.
    Параметры модели Kosur2bsv.xmldev заносятся в таблицу «АРВ (ИД)».
    Типовые значение параметров настройки, приняты согласно информации от производителя системы возбуждения.
    В случае наличия листинга настроек для конкретного энергообъекта необходимо
    использовать фактические параметры настройки.
    """
    K_Q: float = 12.0  # Коэффициент усиления ограничителя минимального возбуждения
    T1f: float = -500.0  # Значение потребляемой реактивной мощности при нулевой выдаче активной мощности для задания в ОМВ
    T2f: float = -200  # Значение потребляемой реактивной мощности при выдаче номинальной активной мощности для задания в ОМВ
    U11: float = 0.85  # Напряжение ввода форсировки
    U22: float = 0.89  # Напряжение снятие форсировки
    Tbch: float = 0.1  # Задержка на снятие форсировки
    TINT: float = 4.4  # Постоянная времени интегратора
    Ku: float = 5.0  # Коэффициент усиления регулятора
    Ku1: float = 2.0  # Коэффициент усиления канала по производной напряжения
    Kif1: float = 1.5  # Коэффициент усиления регулятора по производной по току ротора
    Kf: float = 2.0  # Коэффициент усиления регулятора по частоте
    Kf1: float = 2.0  # Коэффициент усиления регулятора по производной по частоте
    KST: float = 0  # Блокировка (1) PSS при работе ОМВ
