# -*- coding: utf-8 -*-
# Модель системы возбуждения типа THYRIPOL_lite, реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: STyr simp.xmldev.
# Параметры модели STyr simp.xmldev заносятся в таблицу «ВозбудителиIEEE».

from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа THYRIPOL_lite, реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: STyr simp.xmldev.
    Параметры модели STyr simp.xmldev заносятся в таблицу «ВозбудителиIEEE».
    """
    Ta: float = 0.02  # Постоянная времени фильтра входного сигнала по напряжению
    Tb: float = 0.0025  # Постоянная времени фильтра входного сигнала по напряжению
    Kg: float = 0  # Статизм по реактивной мощности генератора
    Kb: float = 30.0  # Коэффициент усиления регулятора напряжения
    RPQlim: float = 1.0  # Блокировка сигнала PSS
    Kv: float = 3.0  # Постоянная времени интегратора ПИ-регулятора
    Vamax: float = 7.48  # Максимальное ограничение регулятора
    Vamin: float = -5.98  # Минимальное ограничение регулятора
    Vrmax: float = 7.48  # Максимальное ограничение возбудителя
    Vrmin: float = -5.98  # Минимальное ограничение возбудителя
    Klr: float = 6.53  # Уставка ограничителя тока ротора
    Kl: float = 65.29  # Пропорциональный коэффициент усиления ограничителя тока ротора
    Ka: float = 1.0  # Коэффициент усиления регулятора напряжения
    Samovozb: float = 1.0  # Режим самовозбуждения
    Tf: float = 0.02  # Коэффициент усиления обратной связи возбудителя
    Tc2: float = 0.85  # Напряжение ввода форсировки
    Tb2: float = 0.85  # Напряжение снятие форсировки
    Tb1: float = 0.002  # Задержка на ввод форсировки
    Tc1: float = 0.03  # Задержка на снятие форсировки
