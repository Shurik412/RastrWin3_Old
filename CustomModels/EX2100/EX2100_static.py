# -*- coding: utf-8 -*-
# Модель системы возбуждения типа EX2100 (EX2100e) _статика,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: EX2100.xmldev.
# Параметры модели EX2100.xmldev заносятся в таблицу «ВозбудителиIEEE».
from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа EX2100 (EX2100e) _статика,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: EX2100.xmldev (таблица 21).
    Параметры модели EX2100.xmldev заносятся в таблицу «ВозбудителиIEEE».

    Типовые значение параметров настройки, приняты согласно информации от
    производителя системы возбуждения. В случае наличия листинга настроек для
    конкретного энергообъекта необходимо использовать фактические параметры настройки.
    """
    Kpr: float = 2.21  # Пропорциональный коэффициент усиления ПИ-регулятора
    Kir: float = 2.21  # Интегральный коэффициент усиления ПИ-регулятора
    Vrmax: float = 1.0  # Максимальное ограничение регулятора напряжения
    Vrmin: float = -0.8  # Минимальное ограничение регулятора напряжения
    Kpa: float = 1.0  # Пропорциональный коэффициент усиления ПИ-регулятора
    Kia: float = 0  # Интегральный коэффициент усиления ПИ-регулятора
    Vmmax: float = 1.0  # Максимальное ограничение регулятора напряжения
    Vmmin: float = -0.8  # Минимальное ограничение регулятора напряжения
    Kp: float = 9.05  # Кратность форсировки по напряжению
    Vamax: float = 11.32  # Максимальное ограничение напряжения возбудителя
    Vamin: float = 0  # Минимальное ограничение напряжения возбудителя
    Kc: float = 0.12  # Коэффициент нагрузки выпрямителя, определяемый сопротивлением коммутации выпрямителя
    Ifmax: float = 5.0  # Уставка по току ротора
    Khf: float = 1.0  # Пропорциональный коэффициент усиления ПИ-регулятора БОР
    Kcf: float = 1.0  # Интегральный коэффициент усиления ПИ-регулятора БОР
