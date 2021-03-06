# -*- coding: utf-8 -*-
# Модель системы возбуждения типа Unitrol-F,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: UNITROL_F.xmldev.
# Параметры модели UNITROL_F.xmldev заносятся в таблицу «ВозбудителиIEEE».
# Типовые значение параметров настройки, приняты согласно информации от
# производителя системы возбуждения. В случае наличия листинга настроек для конкретного
# энергообъекта необходимо использовать фактические параметры настройки.

from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа Unitrol-F,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: UNITROL_F.xmldev.
    Параметры модели UNITROL_F.xmldev заносятся в таблицу «ВозбудителиIEEE».
    Типовые значение параметров настройки, приняты согласно информации от
    производителя системы возбуждения. В случае наличия листинга настроек для конкретного
    энергообъекта необходимо использовать фактические параметры настройки.
    """
    Ka: float = 400  # Коэффициент усиления регулятора напряжения
    Kc: float = 6.068  # Коэффициенты усиления в канале тока ротора
    Kd: float = 7.068  # Коэффициенты усиления возбудителя
    Vrmax: float = 7.0  # Максимальное ограничение регулятора
    Vrmin: float = -6.0  # Минимальное ограничение регулятора
    Tj: float = 5.0  # Постоянная времени апериодического звена возбудителя
    Vamax: float = 2.0  # Максимальное ограничение апериодического звена возбудителя
    Th: float = 0.47  # Постоянная времени инерционно-форсирующего звена