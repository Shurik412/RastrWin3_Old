# -*- coding: utf-8 -*-
# Модель системы возбуждения типа АРВ СГ_БСВ,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: ARVSG_BSV.xmldev.
# Параметры модели ARVSG_BSV.xmldev заносятся в таблицу «ВозбудителиIEEE».
# Типовые значение параметров настройки, приняты согласно информации от
# производителя системы возбуждения. В случае наличия листинга настроек для конкретного
# энергообъекта необходимо использовать фактические параметры настройки.
from RastrWinLib.tables.Dynamic.DFWIEEE421 import DFWIEEE421


class Parameters:
    """
    Модель системы возбуждения типа АРВ СГ_БСВ,
    реализованная в ПК RUSTab, состоит из одного макроблока:
    1.Система возбуждения: ARVSG_BSV.xmldev.
    Параметры модели ARVSG_BSV.xmldev заносятся в таблицу «ВозбудителиIEEE».
    Типовые значение параметров настройки, приняты согласно информации от
    производителя системы возбуждения. В случае наличия листинга настроек для конкретного
    энергообъекта необходимо использовать фактические параметры настройки.
    """
    Ta: float = 0  # Статизм по реактивной мощности генератора
    Kp: float = -0.24  # Смещение характеристики ОМВ (величина реактивного тока при нулевом активном токе статора)
    Kdr: float = 0.21  # Коэффициент «наклона» характеристики ОМВ
    Kd: float = 0.4  # Коэффициент усиления контура ОМВ
    Kc: float = 0.143  # Контурный коэффициент усиления (общий)
    Kv: float = 4.0  # Пропорциональный коэффициент усиления ограничителя напряжения ротора
    Ku: float = 10.0  # Пропорциональный коэффициент усиления регулятора напряжения
    Th: float = 0.1  # Постоянная времени интегратора ограничителя напряжения ротора
    TINT: float = 2.0  # Постоянная времени интегратора регулятора напряжения
    Kf: float = 10.0  # Коэффициент усиления в обратной связи по напряжению ротора
    Tj: float = 0.512  # Постоянная времени инерционно-форсирующего звена (в модели БСВ)
    Vrmax: float = 7.0  # Максимальное ограничение возбудителя
    Vrmin: float = -6.0  # Минимальное ограничение возбудителя
    Kpr: float = 1.64  # Коэффициент усиления возбудителя (в модели БСВ)
    Kir: float = 0.64  # Коэффициент усиления по току ротора (в модели БСВ)
    Tk: float = 3.022  # Постоянная времени апериодического звена возбудителя (в модели БСВ)
    Vemin: float = 0  # Минимальное ограничение ротора
    Tc: float = 2.0  # Уставка ограничителя напряжения ротора
    Kh: float = 0.85  # Напряжение ввода форсировки
    Ka: float = 1.0  # Добавка к уставке по напряжению при вводе релейной форсировки возбуждения
    Tb: float = 0.05  # Гистерезис от уставки на ввод релейной форсировки возбуждения (для задания уставки снятия релейной форсировки возбуждения)
    Ku1: float = 3.0  # Коэффициент усиления канала по производной напряжения
    Kif1: float = 2.0  # Коэффициент усиления канала по производной тока ротора
    Kb: float = 1.5  # Коэффициент масштабирования K1IF при срабатывании ОМВ
    Kof: float = 5.0  # Коэффициент усиления канала по частоте
    Kf1: float = 1.2  # Коэффициент усиления канала по производной частоты
    Klv: float = 0.05  # Уставка по скорости изменения частоты для ввода блокировки PSS
    Vlv: float = 1.0  # Уставка по отклонению частоты для ввода блокировки PSS
    Theta: float = 1.0  # Блокировка (1) PSS при срабатывании ОМВ
    Tf: float = 1.0  # Блокировка (1) канала производной напряжения статора при срабатывании ОМВ
    Tf3: float = 1.2  # Уставка по напряжению для ввода блокировки PSS
    Tf2: float = 5.0  # Уставка по току ротора для ввода блокировки канала по производной тока ротора