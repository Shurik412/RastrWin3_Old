# -*- coding: utf-8 -*-
# Модуль переменных таблицы  "Возбудитель IEEE" RastrWin3


class DFWIEEE421:
    """
    Таблица "Возбудитель IEEE"
    """
    table: str = 'DFWIEEE421'
    table_name: str = '"Возбудители IEEE"'

    sel: str = 'sel'  # Отметка
    sta: str = 'sta'  # Состояние возбудителя
    Id: str = 'Id'  # Номер возбудителя
    Name: str = 'Name'  # Название возбудителя
    ModelType: str = 'ModelType'  # Модель возбудителя
    Brand: str = 'Brand'  # Марка возбудителя
    CustomModel: str = 'CustomModel'  # Модель в конструкторе
    UELId: str = 'UELId'  # Номер ОМВ
    UELPos: str = 'UELPos'  # Точка подключения ОМВ
    OELId: str = 'OELId'  # Номер БОР
    OELPos: str = 'OELPos'  # Точка подключения БОР
    PSSId: str = 'PSSId'  # Номер системного стабилизатора
    PSSPos: str = 'PSSPos'  # Точка подключения стабилизатора

    # Времена
    Te: str = 'Te'  # Постоянная времени возбудителя
    Ta: str = 'Ta'  # Постоянная времени регулятора напряжения
    Tk: str = 'Tk'  # Постоянная времени инерционно-форсирующего звена регулятора (AC6A)
    Tj: str = 'Tj'  # Постоянная времени ограничителя тока возбуждения (AC6A)
    Th: str = 'Th'  # Постоянная времени ограничителя тока возбуждения (AC6A)
    Tm: str = 'Tm'  # Постоянная времени внутреннего каскада
    Tc: str = 'Tc'  # Постоянная времени регулятора напряжения
    Tc1: str = 'Tc1'  # Постоянная времени регулятора напряжения
    Tc2: str = 'Tc2'  # Постоянная времени основного канала
    Tb: str = 'Tb'  # Постоянная времени регулятора напряжения
    Tb1: str = 'Tb1'  # Постоянная времени регулятора напряжения
    Tb2: str = 'Tb2'  # Постоянная времени основного канала
    Trh: str = 'Trh'  # Постоянная времени перемещения реостата (DC3A)
    Tdr: str = 'Tdr'  # Постоянная времени дифференциального канала
    Tf: str = 'Tf'  # Постоянная времени обратной связи cтабилизации
    Tf2: str = 'Tf2'  # Постоянная времени звена обратной связи (AC5C)
    Tf3: str = 'Tf3'  # Постоянная времени звена обратной связи (AC5C)
    Tub1: str = 'Tub1'  # Постоянная времени канала UEL
    Tub2: str = 'Tub2'  # Постоянная времени канала UEL
    Tuc1: str = 'Tuc1'  # Постоянная времени канала UEL
    Tob1: str = 'Tob1'  # Постоянная времени канала OEL
    Toc1: str = 'Toc1'  # Постоянная времени канала OEL
    Toc2: str = 'Toc2'  # Постоянная времени канала OEL
    Tob2: str = 'Tob2'  # Постоянная времени канала OEL
    Tr: str = 'Tr'  # Постоянная времени датчика напряжения
    TINT: str = 'TINT'  # Постоянная времени интегратора в канале регулирования по отклонению напряжения генератора

    # Коэффициенты
    Ke: str = 'Ke'  # Коэффициент обратной связи возбудителя
    Ka: str = 'Ka'  # Коэффициент усиления регулятора напряжения
    Kia: str = 'Kia'  # Интегральный коэффициент усиления
    Kf: str = 'Kf'  # Коэффициент обратной связи cтабилизации
    Kf1: str = 'Kf1'  # Коэффициент стабилизирующей обратной связи
    Kf2: str = 'Kf2'  # Коэффициент стабилизирующей обратной связи
    Kof: str = 'Kof'  # Коэффициент усиления в канале по отклонению частоты напряжения генератора
    K1f: str = 'K1f'  # Коэффициент усиления в канале по производной частоты напряжения генератора
    Kfw: str = 'Kfw'  # Коэффициент ШИМ-преобразователя
    Kv: str = 'Kv'  # Интервал переключения контактов (DC3A)
    Kp: str = 'Kp'  # Коэффициент усиления по напряжению на выводах
    Kpa: str = 'Kpa'  # Пропорциональный коэффициент усиления
    Kpr: str = 'Kpr'  # Пропорциональный коэффициент усиления
    Kir: str = 'Kir'  # Интегральный коэффициент усиления
    Kdr: str = 'Kdr'  # Дифференциальный  коэффициент усиления
    Kc: str = 'Kc'  # Коэффициент нагрузки выпрямителя
    Kc1: str = 'Kc1'  # Коэффициент нагрузки системы питания
    Kc2: str = 'Kc2'  # Коэффициент нагрузки системы питания по току
    Kcf: str = 'Kcf'  # Постоянная времени охлаждения
    Kd: str = 'Kd'  # Коэффициент демагнетизации
    Kb: str = 'Kb'  # Коэффициент усиления
    Kh: str = 'Kh'  # Коэффициент ОС по току (AC2C)/Коэффициент усиления ограничителя (AC6A)
    Khf: str = 'Khf'  # Постоянная времени обратной время?токовой характеристики
    Kr: str = 'Kr'  # Коэффициент ОС питания регулятора (AC3A)/Усиления ST5B/Питания (AC7C)
    Kn: str = 'Kn'  # Переключаемый коэффициент стабилизирующей ОС (AC3A)
    Klv: str = 'Klv'  # Коэффициент системы ограничения минмального возбуждения (AC3A)
    Kl: str = 'Kl'  # Коэффициент усиления ограничения по напряжению на выводах (AC7C)
    Klr: str = 'Klr'  # Коэффициент усиления ограничителя возбуждения
    Klo: str = 'Klo'  # Коэффициент регулирования устройства ОМВ
    Ki: str = 'Ki'  # Коэффициент усиления по току статора
    Ki2: str = 'Ki2'  # Коэффициент системы питания по току
    Kif: str = 'Kif'  # Коэффициент усиления контура отрицательной обратной связи (ООС) по току возбуждения
    Kif1: str = 'Kif1'  # Коэффициент регулирования по производной тока ротора
    Kg: str = 'Kg'  # Коэффициент усиления обратной связи
    Km: str = 'Km'  # Коэффициент усиления внутреннего каскада
    Ku: str = 'Ku'  # Коэффициент регулирования по отклонению напряжения
    Ku1: str = 'Ku1'  # Коэффициент регулирования по производной напряжения
    KST: str = 'KST'  # Статизм по реактивной мощности

    # Коэффициенты насыщения
    Se1: str = 'Se1'  # Se первой точки кривой насыщения
    Se2: str = 'Se2'  # Se второй точки кривой насыщения
    Efd1: str = 'Efd1'  # Efd первой точки кривой насыщения
    Efd2: str = 'Efd2'  # Efd второй точки кривой насыщения
    Efdn: str = 'Efdn'  # Порог переключения коэффициентов стабилизирующей ОС (AC3A)
    Ve1: str = 'Ve1'  # Ve первой точки кривой насыщения
    Ve2: str = 'Ve2'  # Ve второй точки кривой насыщения
    Aex: str = 'Aex'  # Коэффициент кривой насыщения вращающегося возбудителя
    Bex: str = 'Bex'  # Коэффициент кривой насыщения вращающегося возбудителя

    SW1: str = 'SW1'  # Переключатель SW1
    SW2: str = 'SW2'  # Переключатель SW2

    # Коэффициенты напряжения
    Vemin: str = 'Vemin'  # Минимальное напряжение возбудителя
    Vrmax: str = 'Vrmax'  # Ограничение регулятора возбуждения
    Vrmin: str = 'Vrmin'  # Ограничение регулятора возбуждения
    Vfemax: str = 'Vfemax'  # Максимальное напряжение возбудителя
    Vimax: str = 'Vimax'  # Максимальное ограничение входа регулятора
    Vimin: str = 'Vimin'  # Минимальное ограничение входа регулятора
    Vamax: str = 'Vamax'  # Максимальное регулятора напряжения
    Vamin: str = 'Vamin'  # Минимальное ограничение регулятора напряжения
    Vlv: str = 'Vlv'  # Порог системы ограничения минмального возбуждения (AC3A)
    Vmmax: str = 'Vmmax'  # Максимальное ограничение усилителя
    Vmmin: str = 'Vmmin'  # Минимальное ограничение усилителя
    Vhmax: str = 'Vhmax'  # Ограничение сигнала обратной связи (AC6A)
    Vfelim: str = 'Vfelim'  # Уставка ограничителя минимального возбуждения
    VBmax: str = 'VBmax'  # Ограничение источника питания
    VGmax: str = 'VGmax'  # Ограничение обратной связи
    VfwMax: str = 'VfwMax'  # Максимальное ограничение ШИМ-преобразователя
    VfwMin: str = 'VfwMin'  # Минимальное ограничение ШИМ-преобразователя
    Vlim1: str = 'Vlim1'  # Порог ШИМ-преобразователя
    Vlim2: str = 'Vlim2'  # Порог ШИМ-преобразователя
    VpidMax: str = 'VpidMax'  # Максимальное ограничение ПИД-регулятора
    VpidMin: str = 'VpidMin'  # Минимальное ограничение ПИД-регулятора

    Ilr: str = 'Ilr'  # Уставка ограничителя перевозбуждения
    Theta: str = 'Theta'  # Коэффициент усиления по току статора
    Ifmax: str = 'Ifmax'  # Уставка максимального тока возбуждения
    Ifth: str = 'Ifth'  # Уставка теплового ограничения по току возбуждения
    VB2max: str = 'VB2max'  # Ограничение источника питания по току

    # Сопротивления
    Xl: str = 'Xl'  # Сопротивление источника питания
    Rc: str = 'Rc'  # R компенсации
    Xc: str = 'Xc'  # X компенсации

    # Параметры
    TRFout: str = 'TRFout'  # Блокировка работы релейной форсировки
    Samovozb: str = 'Samovozb'  # Параметр, определяющий тип системы возбуждения (зависимая/независимая)
    RPQlim: str = 'RPQlim'  # Блокировка работы устройства ОМВ
    RIFlim: str = 'RIFlim'  # Блокировка работы устройства БОР


class DFWIEEE421_Description:
    """
    Таблица "Возбудитель IEEE"
    """
    dfwieee421 = DFWIEEE421()

    table: str = 'DFWIEEE421'
    table_name: str = '"Возбудители IEEE"'

    sel: str = f'Отметка [O]-[{dfwieee421.sel}]'
    sta: str = f'Состояние возбудителя [S]-[{dfwieee421.sta}]'
    Id: str = f'Номер возбудителя [N взб]-[{dfwieee421.Id}]'
    Name: str = f'Название возбудителя [Название]-[{dfwieee421.Name}]'
    ModelType: str = f'Модель возбудителя [Модель]-[{dfwieee421.ModelType}]'
    Brand: str = f'Марка возбудителя [Марка]-[{dfwieee421.Brand}]'
    CustomModel: str = f'Модель в конструкторе [Конструктор]-[{dfwieee421.CustomModel}]'
    UELId: str = f'Номер ОМВ [N ОМВ]-[{dfwieee421.UELId}]'
    UELPos: str = f'Точка подключения ОМВ [Точка ОМВ]-[{dfwieee421.UELPos}]'
    OELId: str = f'Номер БОР [N БОР]-[{dfwieee421.OELId}]'
    OELPos: str = f'Точка подключения БОР [Точка БОР]-[{dfwieee421.OELPos}]'
    PSSId: str = f'Номер системного стабилизатора [N стаб]-[{dfwieee421.PSSId}]'
    PSSPos: str = f'Точка подключения стабилизатора [Точка стаб]-[{dfwieee421.PSSPos}]'

    # Времена
    Te: str = f'Постоянная времени возбудителя [Te]-[{dfwieee421.Te}]'
    Ta: str = f'Постоянная времени регулятора напряжения [Ta]-[{dfwieee421.Ta}]'
    Tk: str = f'Постоянная времени инерционно-форсирующего звена регулятора (AC6A) [Tk]-[{dfwieee421.Tk}]'
    Tj: str = f'Постоянная времени ограничителя тока возбуждения (AC6A) [Tj]-[{dfwieee421.Tj}]'
    Th: str = f'Постоянная времени ограничителя тока возбуждения (AC6A) [Th]-[{dfwieee421.Th}]'
    Tm: str = f'Постоянная времени внутреннего каскада [Tm]-[{dfwieee421.Tm}]'
    Tc: str = f'Постоянная времени регулятора напряжения [Tc]-[{dfwieee421.Tc}]'
    Tc1: str = f'Постоянная времени регулятора напряжения [Tc1]-[{dfwieee421.Tc1}]'
    Tc2: str = f'Постоянная времени основного канала [Tc2]-[{dfwieee421.Tc2}]'
    Tb: str = f'Постоянная времени регулятора напряжения [Tb]-[{dfwieee421.Tb}]'
    Tb1: str = f'Постоянная времени регулятора напряжения [Tb1]-[{dfwieee421.Tb1}]'
    Tb2: str = f'Постоянная времени основного канала [Tb2]-[{dfwieee421.Tb2}]'
    Trh: str = f'Постоянная времени перемещения реостата (DC3A) [Trh]-[{dfwieee421.Trh}]'
    Tdr: str = f'Постоянная времени дифференциального канала [Tdr]-[{dfwieee421.Tdr}]'
    Tf: str = f'Постоянная времени обратной связи cтабилизации [Tf]-[{dfwieee421.Tf}]'
    Tf2: str = f'Постоянная времени звена обратной связи (AC5C) [Tf2]-[{dfwieee421.Tf2}]'
    Tf3: str = f'Постоянная времени звена обратной связи (AC5C) [Tf3]-[{dfwieee421.Tf3}]'
    Tub1: str = f'Постоянная времени канала UEL [Tub1]-[{dfwieee421.Tub1}]'
    Tub2: str = f'Постоянная времени канала UEL [Tub2]-[{dfwieee421.Tub2}]'
    Tuc1: str = f'Постоянная времени канала UEL [Tuc1]-[{dfwieee421.Tuc1}]'
    Tob1: str = f'Постоянная времени канала OEL [Tob1]-[{dfwieee421.Tob1}]'
    Toc1: str = f'Постоянная времени канала OEL [Toc1]-[{dfwieee421.Toc1}]'
    Toc2: str = f'Постоянная времени канала OEL [Toc2]-[{dfwieee421.Toc2}]'
    Tob2: str = f'Постоянная времени канала OEL [Tob2]-[{dfwieee421.Tob2}]'
    Tr: str = f'Постоянная времени датчика напряжения [Tr]-[{dfwieee421.Tr}]'
    TINT: str = f'Постоянная времени интегратора в канале регулирования по отклонению напряжения генератора [TINT]-[{dfwieee421.TINT}]'

    # Коэффициенты
    Ke: str = f'Коэффициент обратной связи возбудителя [Ke]-[{dfwieee421.Ke}]'
    Ka: str = f'Коэффициент усиления регулятора напряжения [Ka]-[{dfwieee421.Ka}]'
    Kia: str = f'Интегральный коэффициент усиления [Kia]-[{dfwieee421.Kia}]'
    Kf: str = f'Коэффициент обратной связи cтабилизации [Kf]-[{dfwieee421.Kf}]'
    Kf1: str = f'Коэффициент стабилизирующей обратной связи [Kf1]-[{dfwieee421.Kf1}]'
    Kf2: str = f'Коэффициент стабилизирующей обратной связи [Kf2]-[{dfwieee421.Kf2}]'
    Kof: str = f'Коэффициент усиления в канале по отклонению частоты напряжения генератора [K0f]-[{dfwieee421.Kof}]'
    K1f: str = f''
    Kfw: str = f'Коэффициент ШИМ-преобразователя [Kfw]-[{dfwieee421.Kfw}]'
    Kv: str = f'Интервал переключения контактов (DC3A) [Kv]-[{dfwieee421.Kv}]'
    Kp: str = f'Коэффициент усиления по напряжению на выводах [Kp]-[{dfwieee421.Kp}]'
    Kpa: str = f'Пропорциональный коэффициент усиления [Kpa]-[{dfwieee421.Kpa}]'
    Kpr: str = f'Пропорциональный коэффициент усиления [Kpr]-[{dfwieee421.Kpr}]'
    Kir: str = f'Интегральный коэффициент усиления [Kir]-[{dfwieee421.Kir}]'
    Kdr: str = f'Дифференциальный  коэффициент усиления [Kdr]-[{dfwieee421.Kdr}]'
    Kc: str = f'Коэффициент нагрузки выпрямителя [Kc]-[{dfwieee421.Kc}]'
    Kc1: str = f'Коэффициент нагрузки системы питания [Kc1]-[{dfwieee421.Kc1}]'
    Kc2: str = f'Коэффициент нагрузки системы питания по току [Kc2]-[{dfwieee421.Kc2}]'
    Kcf: str = f'Постоянная времени охлаждения [Kcf]-[{dfwieee421.Kcf}]'
    Kd: str = f'Коэффициент демагнетизации [Kd]-[{dfwieee421.Kd}]'
    Kb: str = f'Коэффициент усиления [Kb]-[{dfwieee421.Kb}]'
    Kh: str = f'Коэффициент ОС по току (AC2C)/Коэффициент усиления ограничителя (AC6A) [Kh]-[{dfwieee421.Kh}]'
    Khf: str = f'Постоянная времени обратной время?токовой характеристики [Khf]-[{dfwieee421.Khf}]'
    Kr: str = f'Коэффициент ОС питания регулятора (AC3A)/Усиления ST5B/Питания (AC7C) [Kr]-[{dfwieee421.Kr}]'
    Kn: str = f'Переключаемый коэффициент стабилизирующей ОС (AC3A) [Kn]-[{dfwieee421.Kn}]'
    Klv: str = f'Коэффициент системы ограничения минмального возбуждения (AC3A) [Klv]-[{dfwieee421.Klv}]'
    Kl: str = f'Коэффициент усиления ограничения по напряжению на выводах (AC7C) [Kl]-[{dfwieee421.Kl}]'
    Klr: str = f'Коэффициент усиления ограничителя возбуждения [Klr]-[{dfwieee421.Klr}]'
    Klo: str = f'Коэффициент регулирования устройства ОМВ [Klo]-[{dfwieee421.Klo}]'
    Ki: str = f'Коэффициент усиления по току статора [Ki]-[{dfwieee421.Ki}]'
    Ki2: str = f'Коэффициент системы питания по току [Ki2]-[{dfwieee421.Ki2}]'
    Kif: str = f'Коэффициент усиления контура отрицательной обратной связи (ООС) по току возбуждения [Kif]-[{dfwieee421.Kif}]'
    Kif1: str = f'Коэффициент регулирования по производной тока ротора [Kif1]-[{dfwieee421.Kif1}]'
    Kg: str = f'Коэффициент усиления обратной связи [Kg]-[{dfwieee421.Kg}]'
    Km: str = f'Коэффициент усиления внутреннего каскада [Km]-[{dfwieee421.Km}]'
    Ku: str = f'Коэффициент регулирования по отклонению напряжения [Ku]-[{dfwieee421.Ku}]'
    Ku1: str = f'Коэффициент регулирования по производной напряжения [Ku1]-[{dfwieee421.Ku1}]'
    KST: str = f'Статизм по реактивной мощности [KST]-[{dfwieee421.KST}]'

    # Коэффициенты насыщения
    Se1: str = f'Se первой точки кривой насыщения [Se1]-[{dfwieee421.Se1}]'
    Se2: str = f'Se второй точки кривой насыщения [Se2]-[{dfwieee421.Se2}]'
    Efd1: str = f'Efd первой точки кривой насыщения [Efd1]-[{dfwieee421.Efd1}]'
    Efd2: str = f'Efd второй точки кривой насыщения [Efd2]-[{dfwieee421.Efd2}]'
    Efdn: str = f'Порог переключения коэффициентов стабилизирующей ОС (AC3A) [Efdn]-[{dfwieee421.Efdn}]'
    Ve1: str = f'Ve первой точки кривой насыщения [Ve1]-[{dfwieee421.Ve1}]'
    Ve2: str = f'Ve второй точки кривой насыщения [Ve2]-[{dfwieee421.Ve2}]'
    Aex: str = f'Коэффициент кривой насыщения вращающегося возбудителя [Aex]-[{dfwieee421.Aex}]'
    Bex: str = f'Коэффициент кривой насыщения вращающегося возбудителя [Bex]-[{dfwieee421.Bex}]'

    SW1: str = f'Переключатель SW1 [SW1]-[{dfwieee421.SW1}]'
    SW2: str = f'Переключатель SW2 [SW2]-[{dfwieee421.SW2}]'

    # Коэффициенты напряжения
    Vemin: str = f'Минимальное напряжение возбудителя [Vemin]-[{dfwieee421.Vemin}]'
    Vrmax: str = f'Ограничение регулятора возбуждения [Vrmax]-[{dfwieee421.Vrmax}]'
    Vrmin: str = f'Ограничение регулятора возбуждения [Vrmin]-[{dfwieee421.Vrmin}]'
    Vfemax: str = f'Максимальное напряжение возбудителя [Vfemax]-[{dfwieee421.Vfemax}]'
    Vimax: str = f'Максимальное ограничение входа регулятора [Vimax]-[{dfwieee421.Vimax}]'
    Vimin: str = f'Минимальное ограничение входа регулятора [Vimin]-[{dfwieee421.Vimin}]'
    Vamax: str = f'Максимальное регулятора напряжения [Vamax]-[{dfwieee421.Vamax}]'
    Vamin: str = f'Минимальное ограничение регулятора напряжения [Vamin]-[{dfwieee421.Vamin}]'
    Vlv: str = f'Порог системы ограничения минмального возбуждения (AC3A) [Vlv]-[{dfwieee421.Vlv}]'
    Vmmax: str = f'Максимальное ограничение усилителя [Vmmax]-[{dfwieee421.Vmmax}]'
    Vmmin: str = f'Минимальное ограничение усилителя [Vmmin]-[{dfwieee421.Vmmin}]'
    Vhmax: str = f'Ограничение сигнала обратной связи (AC6A) [Vhmax]-[{dfwieee421.Vhmax}]'
    Vfelim: str = f'Уставка ограничителя минимального возбуждения [Vfelim]-[{dfwieee421.Vfelim}]'
    VBmax: str = f'Ограничение источника питания [VBmax]-[{dfwieee421.VBmax}]'
    VGmax: str = f'Ограничение обратной связи [VGmax]-[{dfwieee421.VGmax}]'
    VfwMax: str = f'Максимальное ограничение ШИМ-преобразователя [VfwMax]-[{dfwieee421.VfwMax}]'
    VfwMin: str = f'Минимальное ограничение ШИМ-преобразователя [VfwMin]-[{dfwieee421.VfwMin}]'
    Vlim1: str = f'Порог ШИМ-преобразователя [Vlim1]-[{dfwieee421.Vlim1}]'
    Vlim2: str = f'Порог ШИМ-преобразователя [Vlim2]-[{dfwieee421.Vlim2}]'
    VpidMax: str = f'Максимальное ограничение ПИД-регулятора [VpidMax]-[{dfwieee421.VpidMax}]'
    VpidMin: str = f'Минимальное ограничение ПИД-регулятора [VpidMin]-[{dfwieee421.VpidMin}]'

    Ilr: str = f'Уставка ограничителя перевозбуждения [Ilr]-[{dfwieee421.Ilr}]'
    Theta: str = f'Коэффициент усиления по току статора [Theta]-[{dfwieee421.Theta}]'
    Ifmax: str = f'Уставка максимального тока возбуждения [Ifmax]-[{dfwieee421.Ifmax}]'
    Ifth: str = f'Уставка теплового ограничения по току возбуждения [Ifth]-[{dfwieee421.Ifth}]'
    VB2max: str = f'Ограничение источника питания по току [VB2max]-[{dfwieee421.VB2max}]'

    # Сопротивления
    Xl: str = f'Сопротивление источника питания [Xl]-[{dfwieee421.Xl}]'
    Rc: str = f'R компенсации [Rc]-[{dfwieee421.Rc}]'
    Xc: str = f'X компенсации [Xc]-[{dfwieee421.Xc}]'

    # Параметры
    TRFout: str = f'Блокировка работы релейной форсировки [TRFout]-[{dfwieee421.TRFout}]'
    Samovozb: str = f'Параметр, определяющий тип системы возбуждения (зависимая/независимая) [Samovozb]-[{dfwieee421.Samovozb}]'
    RPQlim: str = f'Блокировка работы устройства ОМВ [RPQlim]-[{dfwieee421.RPQlim}]'
    RIFlim: str = f'Блокировка работы устройства БОР [RIFlim]-[{dfwieee421.RIFlim}]'





