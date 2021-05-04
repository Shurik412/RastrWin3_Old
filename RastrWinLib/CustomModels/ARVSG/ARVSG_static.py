# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения типа АРВ СГ_статика,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1. АРВ: ARVSG_sts.xmldev.
# Параметры модели ARVSG_sts.xmldev заносятся в таблицу «АРВ (ИД)».
# Типовые значение параметров настройки, приняты согласно информации от
# производителя системы возбуждения. В случае наличия листинга настроек для
# конкретного энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.tables.Dynamic.ExcControl import ExcControl


class Parameters:
    """
    Модель автоматического регулятора возбуждения типа АРВ СГ_статика,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1. АРВ: ARVSG_sts.xmldev.
    Параметры модели ARVSG_sts.xmldev заносятся в таблицу «АРВ (ИД)».
    Типовые значение параметров настройки, приняты согласно информации от
    производителя системы возбуждения. В случае наличия листинга настроек для
    конкретного энергообъекта необходимо использовать фактические параметры настройки.
    """
    U11: float = 0.85  # Напряжение ввода форсировки
    U22: float = 0.85 + 0.01  # Напряжение снятия форсировки
    Kuf: float = 1.0  # Контурный коэффициент усиления регулятора (общий)
    Ku: float = 15.0  # Коэффициент усиления регулятора
    TINT: float = 4.0  # Постоянная времени интегратора регулятора
    Ku1: float = 3.0  # Коэффициент усиления канала по производной напряжения
    Kif1: float = 1.5  # Коэффициент усиления канала по производной тока ротора
    Kf: float = 3.0  # Коэффициент усиления канала по частоте
    Kf1: float = 2.0  # Коэффициент усиления канала по производной частоты
    T1f1: float = 0.15  # Задержка на ввод ОТР при действии релейной форсировки возбуждения
    T1f: float = 2.0  # Уставка ограничителя максимального тока ротора
    KST: float = -0.24  # Смещение характеристики ОМВ (величина реактивного тока при нулевом активном токе статора)
    Kpi: float = 0.2  # Коэффициент «наклона» характеристики ОМВ
    Kiu: float = 0.6  # Коэффициент усиления выходного сигнала ОМВ
    Tbch: float = 1.0  # Постоянная времени для расчета сигнала частоты в алгоритме блокировки PSS
