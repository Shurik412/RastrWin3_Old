# -*- coding: utf-8 -*-
# Модель системы возбуждения типа Alstom_ControGen V3_lite,
# реализованная в ПК RUSTab, состоит из одного макроблока:
# 1.Система возбуждения: Alstom2 simp.xmldev.
# Параметры модели Alstom2 simp.xmldev заносятся в таблицу «ВозбудителиIEEE».
from RastrWinLib.Tables.Dynamic.DFWIEEE421 import DFWIEEE421


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

    # Значения зависят от параметров системы возбуждения. Фактически – кратность форсировки
    # и расфорсировки в единицах холостого хода
    Vamax: float = None  # Максимальное ограничение регулятора напряжения
    Vamin: float = None  # Минимальное ограничение регулятора напряжения
    Ifth: float = 0.1  # (0,1...0,3) Уставка по току ротора (Индивидуальные значения приведены в листинге)
    Kb: float = 0  # (0...0,5) Пропорциональный коэффициент усиления канала тока ротора в алгоритме ОМВ (Индивидуальные значения приведены в листинге)
    Tk: float = 0.5  # (0,5...5) Постоянная времени канала по напряжению в алгоритме ОМВ (Индивидуальные значения приведены в листинге)
    Trh: float = 0.01  # (0,01...0,2) Постоянная блока формирования сигнала по частоте в алгоритме блокировки ПСС (Индивидуальные значения приведены в листинге)
    Kv: float = 0  # (0...2) Максимальная скорость изменения частоты (блокировка ПСС) (Индивидуальные значения приведены в листинге)
    Kf: float = 1  # (1...0,2) Гистерезис блокировки ПСС (Индивидуальные значения приведены в листинге)
    Ve1: float = 0.7  # (0,7...UEX_MAX) Кратность форсировки (Индивидуальные значения приведены в листинге)
    Ve2: float = None  # Минимальное значение выхода регулятора (Индивидуальные значения приведены в листинге)
    Ifmax: float = None  # Уставка по току ротора (Задается равным 2 о.е. тока ротора номинального режима)
    Khf: float = 1  # (1 ... 10) Пропорциональный коэффициент усиления БОР при работе РФ (Индивидуальные значения приведены в листинге)
    Kcf: float = 0.1  # (0,1 ... 10) Пропорциональный коэффициент усиления БОР (Индивидуальные значения приведены в листинге)

    # Типовые значение параметров настройки и диапазон значений, указанные в таблице 3,
    # приняты согласно информации от производителя системы возбуждения.
    # В случае наличия листинга настроек для конкретного энергообъекта
    # необходимо использовать фактические параметры настройки.

    # Параметры модели Alstom2_PSS.xmldev заносятся в таблицу «Стабилизаторы IEEE 1-3».
    # Таблица 4 – Параметры модели системного стабилизатора Alstom2_PSS.xmldev, задаваемые в ПК RUSTab

    Vsi1max: float = 0.1  # (0... 0,2) Максимальное ограничение входного сигнала по частоте
    Vsi1min: float = -0.1  # (0 ... -0.2) Минимальное ограничение входного сигнала по частоте
    Vsi2max: float = 0.1  # (0.1 ... 2) Максимальное ограничение входного сигнала по мощности
    Vsi2min: float = -0.1  # (0 ... -2) Минимальное ограничение входного сигнала по мощности
    Tw1: float = 1  # (1...10) Постоянная времени фильтра высокой частоты
    Tw2: float = 1  # (1...30) Постоянная времени фильтра высокой частоты
    Tw3: float = 1  # (1...10) Постоянная времени фильтра высокой частоты
    Ks2: float = 0.1  # (0...1) Коэффициент для приращения мощности
    T7: float = 1  # (1...30) Постоянная времени фильтра высокой частоты
    Ks3: float = None  # (0/1) Коэффициент усиления канала мощности
    T8: float = 0.1  # (0...2) Постоянная времени фильтра торсионных колебаний
    T9: float = 0.1  # (0.1...0.5) Постоянная времени фильтра торсионных колебаний
    Ks1: float = 0.1  # (0 ...150) Коэффициент усиления
    T1: float = 0.1  # (0...10) Постоянная времени инерционно-форсирующего звена
    T2: float = 0.015  # (0.015...3) Постоянная времени инерционно-форсирующего звена
    T3: float = 0.1  # (0...10)  Постоянная времени инерционно-форсирующего звена
    T4: float = 0.015  # (0.015 ...3) Постоянная времени инерционно-форсирующего звена
    T11: float = 0.1  # (0...10) Постоянная времени инерционно-форсирующего звена
    A1: float = 0.015  # (0.015 ... 3) Постоянная времени инерционно-форсирующего звена
    A2: float = 0.1  # (0...10) Постоянная времени инерционно-форсирующего звена
    A3: float = 0.015  # (0.015 ... 3) Постоянная времени инерционно-форсирующего звена
    Vstmax: float = 0.1  # (0...0.1) Максимальное ограничение выходного сигнала
    Vstmin: float = 0  # (0...-0.1) Минимальное ограничение выходного сигнала

    # Типовые значение параметров настройки и диапазон значений, указанные в таблице 4,
    # приняты согласно информации от производителя системы возбуждения.
    # В случае наличия листинга настроек для конкретного энергообъекта
    # необходимо использовать фактические параметры настройки.