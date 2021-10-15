# -*- coding: utf-8 -*-
# Модель возбудителя типа BESSCH, реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Возбудитель: BESSCH.xmldev.
# Параметры модели BESSCH.xmldev заносятся в таблицу «Возбудитель (ИД)».

from RastrWinLib.Tables.Dynamic.Exciter import Exciter


class Parameters:
    """
    Модель возбудителя типа BESSCH, реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Возбудитель: BESSCH.xmldev.
    Параметры модели BESSCH.xmldev заносятся в таблицу «Возбудитель (ИД)».
    Все параметры индивидуальны и определяются расчетным путем по исходным данным:
    электрические параметры генератора и возбудителя
    """
    # Все параметры индивидуальны и определяются расчетным путем по исходным данным:
    # электрические параметры генератора и возбудителя
    Karv: float = None  # Коэффициент усиления возбудителя
    Kif: float = None  # Коэффициент усиления канала по току ротора
    Texc: float = None  # Постоянная времени возбудителя
    T3exc: float = None  # Постоянная времени канала по току ротора
    Uf_max: float = None  # Максимальное значение выходного напряжения возбудителя
    Uf_min: float = None  # Минимальное значение выходного напряжения возбудителя
    If_max: float = None  # Максимальное значение выходного напряжения возбуждения возбудителя
    If_min: float = None  # Минимальное значение выходного напряжения возбуждения возбудителя
