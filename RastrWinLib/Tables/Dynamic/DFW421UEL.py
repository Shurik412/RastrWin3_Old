# -*- coding: utf-8 -*-
# Модуль переменных таблицы  "ОМВ" RastrWin3


class DFW421UEL:
    """

    """

    table: str = 'DFW421UEL'  # название таблицы
    table_name: str = '"ОМВ"'

    sel: str = 'sel'  # Отметка
    sta: str = 'sta'  # Состояние ОМВ
    Id: str = 'Id'  # N ОМВ Номер ОМВ
    Name: str = 'Name'  # Название ОМВ
    ModelType: str = 'ModelType'  # Модель ОМВ
    Brand: str = 'Brand'  # Марка ОМВ
    CustomModel: str = 'CustomModel'  # Модель в конструкторе
    Dependency_F1: str = 'Dependency_F1'  # Номер зависимости Q(P) (UEL-2)
    Output: str = 'Output'  # Режим выхода

    # Коэффициенты
    K1: str = 'K1'  # Показатель степени F1 (UEL-2)
    K2: str = 'K2'  # Показатель степени F2 (UEL-2)
    Kul: str = 'Kul'  # Пропорциональный коэффициент регулятора
    Kui: str = 'Kui'  # Интегральный коэффициент регулятора
    Kuf: str = 'Kuf'  # Коэффициент обратной связи по току возбуждения
    Kur: str = 'Kur'  # Коэффициент радиуса (UEL-1)
    Kuc: str = 'Kuc'  # Коэффициент центра (UEL-1)
    Kl: str = 'Kl'  # Коэффициент усиления в режиме прямого выхода

    # Времена
    Tu1: str = 'Tu1'  # Постоянная времени регулятора
    Tu2: str = 'Tu2'  # Постоянная времени регулятора
    Tu3: str = 'Tu3'  # Постоянная времени регулятора
    Tu4: str = 'Tu4'  # Постоянная времени регулятора

    Tuf: str = 'Tuf'  # Коэффициент обратной связи по току возбуждения
    TuV: str = 'TuV'  # Постоянная времени фильтра напряжения (UEL-2)
    TuP: str = 'TuP'  # Постоянная времени фильтра активной мощности (UEL-2)
    TuQ: str = 'TuQ'  # Постоянная времени фильтра реактивной мощности (UEL-2)

    Vurmax: str = 'Vurmax'  # Ограничение радиуса (UEL-1)
    Vucmax: str = 'Vucmax'  # Ограничение центра (UEL-1)
    Vulmax: str = 'Vulmax'  # Максимальное ограничение ОМВ
    Vulmin: str = 'Vulmin'  # Минимальное ограничение ОМВ
    Vuimin: str = 'Vuimin'  # Минимальное ограничение регулятора
    Vuimax: str = 'Vuimax'  # Максимальное ограничение регулятора


class DFW421UEL_Description:
    """

    """
    dew421uel = DFW421UEL()

    table: str = 'DFW421UEL'  # название таблицы
    table_name: str = 'ОМВ'

    sel: str = f''
    sta: str = f''
    Id: str = f''
    Name: str = f''
    ModelType: str = f''
    Brand: str = f''
    CustomModel: str = f''
    Dependency_F1: str = f''
    Output: str = f''

    # Коэффициенты
    K1: str = f''
    K2: str = f''
    Kul: str = f''
    Kui: str = f''
    Kuf: str = f''
    Kur: str = f''
    Kuc: str = f''
    Kl: str = f''

    # Времена
    Tu1: str = f''
    Tu2: str = f''
    Tu3: str = f''
    Tu4: str = f''

    Tuf: str = f''
    TuV: str = f''
    TuP: str = f''
    TuQ: str = f''

    Vurmax: str = f''
    Vucmax: str = f''
    Vulmax: str = f''
    Vulmin: str = f''
    Vuimin: str = f''
    Vuimax: str = f''

