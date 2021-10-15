# -*- coding: utf-8 -*-
# Модель автоматического регулятора возбуждения пропорционального действия с РФ,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1. АРВ: ARVP.xmldev (таблица 47).
# Параметры модели ARVP.xmldev заносятся в таблицу «АРВ (ИД)».
# Типовые значение параметров настройки, приняты согласно информации
# от производителя системы возбуждения. В случае наличия листинга настроек
# для конкретного энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель автоматического регулятора возбуждения пропорционального действия с РФ,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1. АРВ: ARVP.xmldev (таблица 47).
    Параметры модели ARVP.xmldev заносятся в таблицу «АРВ (ИД)».
    Типовые значение параметров настройки, приняты согласно информации от производителя системы возбуждения.
    В случае наличия листинга настроек для конкретного энергообъекта необходимо
    использовать фактические параметры настройки.
    """
    K_la: float = 0.7  # Коэффициент компаундирования по току статора
    Ku: float = 10  # Коэффициент усиления регулятора
    Trv: float = 0.3  # Постоянная времени апериодического звена регулятора
    Urv_max: float = 5.0  # Максимальное ограничение регулятора
    Urv_min: float = -5.0  # Минимальное ограничение регулятора
    Kif1: float = 0  # Коэффициент усиления по току ротора
    U11: float = 0.85  # Напряжение ввода форсировки
    U22: float = 0.86  # Напряжение снятие форсировки
