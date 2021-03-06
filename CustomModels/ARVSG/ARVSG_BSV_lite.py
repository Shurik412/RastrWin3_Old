# -*- coding: utf-8 -*-
# Модель системы возбуждения типа АРВ СГ_БСВ_lite,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1. Система возбуждения: ARVSG_BSV simp.xmldev (таблица 76).
# Параметры модели ARVSG_BSV simp.xmldev заносятся в таблицу «ВозбудителиIEEE».
# Типовые значение параметров настройки, приняты согласно информации от
# производителя системы возбуждения. В случае наличия листинга настроек для конкретного
# энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа АРВ СГ_БСВ_lite,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1. Система возбуждения: ARVSG_BSV simp.xmldev (таблица 76).
    Параметры модели ARVSG_BSV simp.xmldev заносятся в таблицу «ВозбудителиIEEE».
    Типовые значение параметров настройки, приняты согласно информации от
    производителя системы возбуждения. В случае наличия листинга настроек для конкретного
    энергообъекта необходимо использовать фактические параметры настройки.
    """
    Ta: float = 0  # Статизм по реактивной мощности генератора
    Kc: float = 0.143  # Контурный коэффициент усиления (общий)
    Kv: float = 4.0  # Пропорциональный коэффициент усиления ограничителя напряжения ротора
    Ku: float = 10  # Пропорциональный коэффициент усиления регулятора напряжения
    Th: float = 0.1  # Постоянная времени интегратора ограничителя напряжения ротора
    TINT: float = 2.0  # Постоянная времени интегратора регулятора напряжения
    Kf: float = 10  # Коэффициент усиления в обратной связи по напряжению ротора
    Tj: float = 0.512  # Постоянная времени инерционно-форсирующего звена (в модели БСВ)
    Vrmax: float = 7  # Максимальное ограничение возбудителя
    Vrmin: float = -6  # Минимальное ограничение возбудителя
    Kpr: float = 1.64  # Коэффициент усиления возбудителя (в модели БСВ)
    Kir: float = 0.64  # Коэффициент усиления по току ротора (в модели БСВ)
    Tk: float = 3.022  # Постоянная времени апериодического звена возбудителя (в модели БСВ)
    Vemin: float = 0  # Минимальное ограничение ротора
    Tc: float = 2.0  # Уставка ограничителя напряжения ротора
    Kh: float = 0.85  # Напряжение ввода форсировки
    Ka: float = 1  # Добавка к уставке по напряжению при вводе релейной форсировки возбуждения
    Tb: float = 0.05  # Гистерезис от уставки на ввод релейной форсировки возбуждения (для задания уставки снятия релейной форсировки возбуждения)
    Ku1: float = 3.0  # Коэффициент усиления канала по производной напряжения
    Kif1: float = 2.0  # Коэффициент усиления канала по производной тока ротора
    Kb: float = 1.5  # Коэффициент масштабирования K1IF при срабатывании ОМВ
    Kof: float = 5.0  # Коэффициент усиления канала по частоте
    Kf1: float = 1.2  # Коэффициент усиления канала по производной частоты
    Tc1: float = 0.1  # Задержка на снятие релейной форсировки возбуждения
