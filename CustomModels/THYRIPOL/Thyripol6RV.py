# -*- coding: utf-8 -*-
# Модель системы возбуждения типа THYRIPOL 6RV80, реализованная в ПК RUSTab, состоит из следующих макроблоков:
# 1.Система возбуждения: Thyripol6RV.xmldev (таблица 36);
# 2.Системный стабилизатор: ThyrPSS6RV.xmldev (таблица 37).
# Параметры модели Thyripol6RV.xmldev заносятся в таблицу «ВозбудителиIEEE».


class Parameters:
    """
    Модель системы возбуждения типа THYRIPOL 6RV80, реализованная в ПК RUSTab, состоит из следующих макроблоков:
    1.Система возбуждения: Thyripol6RV.xmldev (таблица 36);
    2.Системный стабилизатор: ThyrPSS6RV.xmldev (таблица 37).
    Параметры модели Thyripol6RV.xmldev заносятся в таблицу «ВозбудителиIEEE».
    Параметры модели ThyrPSS6RV.xmldev заносятся в таблицу «Стабилизаторы IEEE 1-3».
    Типовые значение параметров настройки, приняты согласно информации от
    производителя системы возбуждения. В случае наличия листинга настроек для
    конкретного энергообъекта необходимо использовать фактические параметры настройки.
    """
    Ke: float = 0  # Статизм по реактивной мощности генератора
    Kb: float = 3.75  # Коэффициент усиления регулятора напряжения
    Kv: float = 2  # Постоянная времени интегратора ПИ-регулятора
    Vamax: float = 6.94  # Максимальное ограничение регулятора
    Vamin: float = -5.56  # Минимальное ограничение регулятора
    Vrmax: float = 6.94  # Максимальное ограничение возбудителя
    Vrmin: float = -5.56  # Минимальное ограничение возбудителя
    Samovozb: float = 0  # Режим самовозбуждения
    Kl: float = 17.33  # Пропорциональный коэффициент усиления ограничителя тока ротора
    Klr: float = 4.164  # Уставка ограничителя тока ротора
    Kc: float = 1.0577  # Корректировка уставки ограничителя тока ротора
    Kf1: float = 0.0005  # Параметры реле с гистерезисом для срабатывания ограничителя тока
    Kf2: float = 0.15  # Параметры реле с гистерезисом для срабатывания ограничителя тока
    Tj: float = 0.2  # Задержка на ввод ограничителя тока ротора
    Tm: float = 0  # Выбор входного сигнала канала частоты (компенсированная частота (1) / частота напряжения (0))
    Kpa: float = 0.1  # Постоянные времени фильтра сигнала частоты в алгоритме блокировки PSS
    Kia: float = 1  # Постоянные времени фильтра сигнала частоты в алгоритме блокировки PSS
    Se1: float = 0.0002  # Параметры реле с гистерезисом для срабатывания блокировки PSS
    Se2: float = 0.001  # Параметры реле с гистерезисом для срабатывания блокировки PSS
    Tk: float = 0.05  # Задержка на ввод блокировки PSS
    Tf2: float = 2  # Задержка на вывод блокировки PSS
    Ta: float = 0.01  # Постоянная времени апериодического звена блокировки ПСС
    Tb: float = 0.01  # Постоянная времени апериодического звена блокировки ПСС
    TRFout: float = 0  # Запрет ввода блокировки ПСС
    Tc2: float = 0.85  # Напряжение ввода форсировки
    Tb2: float = 0.89  # Напряжение снятие форсировки
    Tb1: float = 0.002  # Задержка на ввод форсировки
    Tc1: float = 0.1  # Задержка на снятие форсировки
    Klo: float = 1  # Пропорциональный коэффициент усиления в ОМВ
    Vimax: float = 1  # Ограничение максимального значения ОМВ
    Vimin: float = -1  # Ограничение минимального значения ОМВ
    Te: float = 0.01  # Дополнительное смещение сигнала об активации ОМВ (обеспечивает срабатывание ограничителя несколько раньше)
    Kif: float = 2  # Задержка на активацию ОМВ
    Khf: float = -0.01  # Параметры реле с гистерезисом для срабатывания блокировки PSS в ОМВ
    Ku: float = 0.01  # Параметры реле с гистерезисом для срабатывания блокировки PSS в ОМВ

    # Параметры модели ThyrPSS6RV.xmldev заносятся в таблицу «Стабилизаторы IEEE 1-3»
    Vsi2max: float = 2  # Максимальное ограничение входного сигнала по мощности
    Vsi2min: float = -1  # Минимальное ограничение входного сигнала по мощности
    Tw3: float = 2  # Постоянная времени фильтра высокой частоты
    Tw4: float = 2  # Постоянная времени фильтра высокой частоты
    Ks2: float = 0.143  # Коэффициент для приращения мощности
    T7: float = 2  # Постоянная времени фильтра высокой частоты
    Ks3: float = 1  # Коэффициент усиления канала
    T5: float = 0  # Выбор входного сигнала канала частоты (компенсированная частота (1) / частота напряжения (0))
    A7: float = None  # Xd генератора
    Vsi1max: float = 1  # Максимальное ограничение входного сигнала по частоте
    Vsi1min: float = -1  # Минимальное ограничение входного сигнала по частоте
    Tw1: float = 2  # Постоянная времени фильтра высокой частоты
    Tw2: float = 2  # Постоянная времени фильтра высокой частоты
    T6: float = 0  # Постоянная времени фильтра высокой частоты
    T8: float = 0.7  # Постоянная времени фильтра торсионных колебаний
    T9: float = 0.35  # Постоянная времени фильтра торсионных колебаний
    M: float = 2  # Порядок фильтра
    N: float = 4  # Порядок фильтра
    Ks1: float = 6.25  # Коэффициент усиления
    T1: float = 0.24  # Постоянная времени инерционно-форсирующего звена
    T2: float = 0.06  # Постоянная времени инерционно-форсирующего звена
    T3: float = 0.24  # Постоянная времени инерционно-форсирующего звена
    T4: float = 0.06  # Постоянная времени инерционно-форсирующего звена
    T10: float = 5  # Постоянная времени инерционно-форсирующего звена
    T11: float = 5  # Постоянная времени инерционно-форсирующего звена
    Vstmax: float = 0.05  # Максимальное ограничение выходного сигнала
    Vstmin: float = -0.05  # Минимальное ограничение выходного сигнала
