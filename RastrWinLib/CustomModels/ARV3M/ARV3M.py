# -*- coding: utf-8 -*-
#  ---------------- Модель ARV-3M ----------------
# Модель автоматического регулятора возбуждения типа ARV3M,
# реализованная в ПК RUSTab, состоит из макроблоков.
# Параметры модели AVR-3M_res.xmldev заносятся в таблицу «АРВ (ИД)».

import RastrWinLib.CustomModels.ARV3M.Parameters_ARV3M as Parameters_ARV3M
import RastrWinLib.tables.Dynamic.ExcControl as ExcControl
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.log_tools.tools import separator_grid
from RastrWinLib.variables.variable_parametrs import Variable


def change_parameters(
        Id: int = None,
        row_id: int = None,
        Ku: float = Parameters_ARV3M.Ku,
        K_Q: float = Parameters_ARV3M.K_Q,
        Kif1: float = Parameters_ARV3M.Kif1,
        T1if: float = Parameters_ARV3M.T1if,
        Ku1: float = Parameters_ARV3M.Ku1,
        T1u1: float = Parameters_ARV3M.T1u1,
        K_P: float = Parameters_ARV3M.K_P,
        K_Ia: float = Parameters_ARV3M.K_Ia,
        Tf: float = Parameters_ARV3M.Tf,
        Kf: float = Parameters_ARV3M.Kf,
        Kf1: float = Parameters_ARV3M.Kf1,
        TINT: float = Parameters_ARV3M.TINT,
        rastr_win=RASTR,
        switch_command_line: bool = False):
    """
    Функция change_parameters -
    :param switch_command_line:
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param Id: Номер возбудителя;
    :param row_id: порядковый номер в таблице (от 0 до [max.count]);
    :param Ku: Коэффициент усиления пропорционального канала регулятора напряжения;
    :param K_Q: Коэффициент усиления канала по производной тока ротора;
    :param Kif1: Коэффициент усиления канала по производной тока ротора;
    :param T1if: Постоянная времени дифференциру-ющего звена в канале по производной тока ротора;
    :param Ku1: Коэффициент усиления канала по производной напряжения;
    :param T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения;
    :param K_P: Коэффициент усиления выходного сигнала ОМВ;
    :param K_Ia: Уставка ограничителя максимального тока ротора;
    :param Tf: Постоянная времени дифференцирующего звена в канале по частоте;
    :param Kf: Коэффициент усиления в канале по частоте;
    :param Kf1: Коэффициент усиления в канале по производной частоты;
    :param TINT: Постоянная времени интегратора
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)
    get_ = GettingParameter(rastr_win=rastr_win)

    if Id is not None and row_id is None:
        # Ku
        if switch_command_line is not None:
            ku_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Ku,
                                         Id=Id)
        else:
            ku_before = None

        variable_.make_changes_row(table=ExcControl.table,
                                   column=ExcControl.Ku,
                                   row_id=row_id,
                                   value=Ku)

        if switch_command_line is not None:
            ku_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Ku,
                                        Id=Id)
        else:
            ku_after = None

        # K_Q
        if switch_command_line is not None:
            k_q_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.K_Q,
                                          Id=Id)
        else:
            k_q_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Q,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Q)

        if switch_command_line is not None:
            k_q_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.K_Q,
                                         Id=Id)
        else:
            k_q_after = None

        # Kif1
        if switch_command_line is not None:
            kif1_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.Kif1,
                                           Id=Id)
        else:
            kif1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kif1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kif1)

        if switch_command_line is not None:
            kif1_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Kif1,
                                          Id=Id)
        else:
            kif1_after = None

        # T1if
        if switch_command_line is not None:
            t1if_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.T1if,
                                           Id=Id)
        else:
            t1if_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1if,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1if)

        if switch_command_line is not None:
            t1if_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.T1if,
                                          Id=Id)
        else:
            t1if_after = None

        # Ku1
        if switch_command_line is not None:
            ku1_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Ku1,
                                          Id=Id)
        else:
            ku1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku1)

        if switch_command_line is not None:
            ku1_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Ku1,
                                         Id=Id)
        else:
            ku1_after = None

        # T1u1
        if switch_command_line is not None:
            t1u1_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.T1u1,
                                           Id=Id)
        else:
            t1u1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1u1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1u1)

        if switch_command_line is not None:
            t1u1_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.T1u1,
                                          Id=Id)
        else:
            t1u1_after = None

        # K_P
        if switch_command_line is not None:
            kp_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.K_P,
                                         Id=Id)
        else:
            kp_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_P,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_P)

        if switch_command_line is not None:
            kp_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.K_P,
                                        Id=Id)
        else:
            kp_after = None

        # K_Ia
        if switch_command_line is not None:
            k_ia_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.K_Ia,
                                           Id=Id)
        else:
            k_ia_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Ia,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Ia)

        if switch_command_line is not None:
            k_ia_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.K_Ia,
                                          Id=Id)
        else:
            k_ia_after = None

        # Tf
        if switch_command_line is not None:
            tf_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Tf,
                                         Id=Id)
        else:
            tf_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Tf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Tf)

        if switch_command_line is not None:
            tf_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Tf,
                                        Id=Id)
        else:
            tf_after = None

        # Kf
        if switch_command_line is not None:
            kf_before = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Kf,
                                         Id=Id)
        else:
            kf_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf)

        if switch_command_line is not None:
            kf_after = get_.get_cell_id(table=ExcControl.table,
                                        column=ExcControl.Kf,
                                        Id=Id)
        else:
            kf_after = None

        # Kf1
        if switch_command_line is not None:
            kf1_before = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.Kf1,
                                          Id=Id)
        else:
            kf1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf1)

        if switch_command_line is not None:
            kf1_after = get_.get_cell_id(table=ExcControl.table,
                                         column=ExcControl.Kf1,
                                         Id=Id)
        else:
            kf1_after = None

        # TINT
        if switch_command_line is not None:
            tint_before = get_.get_cell_id(table=ExcControl.table,
                                           column=ExcControl.TINT,
                                           Id=Id)
        else:
            tint_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.TINT,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=TINT)

        if switch_command_line is not None:
            tint_after = get_.get_cell_id(table=ExcControl.table,
                                          column=ExcControl.TINT,
                                          Id=Id)
        else:
            tint_after = None

        if switch_command_line is not False:
            print(
                f'{separator_grid}\n'
                f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
                f'- Id: Номер возбудителя: {Id}\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: до {ku_before}; после {ku_after};\n'
                f'- K_Q: Коэффициент усиления канала по производной тока ротора: до {k_q_before}; после {k_q_after};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора: до {kif1_before}; после {kif1_after};\n'
                f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: до {t1if_before}; после {t1if_after};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения: до {ku1_before}; после {ku1_after};\n'
                f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: до {t1u1_before}; после {t1u1_after};\n'
                f'- K_P: Коэффициент усиления выходного сигнала ОМВ: до {kp_before}; после {kp_after};\n'
                f'- K_Ia: Уставка ограничителя максимального тока ротора: до {k_ia_before}; после {k_ia_after};\n'
                f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: до {tf_before}; после {tf_after};\n'
                f'- Kf: Коэффициент усиления в канале по частоте: до {kf_before}; после {kf_after};\n'
                f'- Kf1: Коэффициент усиления в канале по производной частоты: до {kf1_before}; после {kf1_after};\n'
                f'- TINT: Постоянная времени интегратора: до {tint_before}; после {tint_after};\n'
                f'{separator_grid}\n'
            )

    if row_id is not None and Id is None:
        # Ku
        if switch_command_line is not False:
            ku_before = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Ku,
                                          row_id=row_id)
        else:
            ku_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku)

        if switch_command_line is not False:
            ku_after = get_.get_cell_row(table=ExcControl.table,
                                         column=ExcControl.Ku,
                                         row_id=row_id)
        else:
            ku_after = None

        # K_Q
        if switch_command_line is not False:
            k_q_before = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.K_Q,
                                           row_id=row_id)
        else:
            k_q_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Q,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Q)

        if switch_command_line is not False:
            k_q_after = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.K_Q,
                                          row_id=row_id)
        else:
            k_q_after = None

        # Kif1
        if switch_command_line is not False:
            kif1_before = get_.get_cell_row(table=ExcControl.table,
                                            column=ExcControl.Kif1,
                                            row_id=row_id)
        else:
            kif1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kif1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kif1)

        if switch_command_line is not False:
            kif1_after = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.Kif1,
                                           row_id=row_id)
        else:
            kif1_after = None

        # T1if
        if switch_command_line is not False:
            t1if_before = get_.get_cell_row(table=ExcControl.table,
                                            column=ExcControl.T1if,
                                            row_id=row_id)
        else:
            t1if_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1if,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1if)

        if switch_command_line is not False:
            t1if_after = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.T1if,
                                           row_id=row_id)
        else:
            t1if_after = None

        # Ku1
        if switch_command_line is not False:
            ku1_before = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.Ku1,
                                           row_id=row_id)
        else:
            ku1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Ku1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Ku1)

        if switch_command_line is not False:
            ku1_after = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Ku1,
                                          row_id=row_id)
        else:
            ku1_after = None

        # T1u1
        if switch_command_line is not False:
            t1u1_before = get_.get_cell_row(table=ExcControl.table,
                                            column=ExcControl.T1u1,
                                            row_id=row_id)
        else:
            t1u1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.T1u1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=T1u1)

        if switch_command_line is not False:
            t1u1_after = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.T1u1,
                                           row_id=row_id)
        else:
            t1u1_after = None

        # K_P
        if switch_command_line is not False:
            kp_before = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.K_P,
                                          row_id=row_id)
        else:
            kp_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_P,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_P)

        if switch_command_line is not False:
            kp_after = get_.get_cell_row(table=ExcControl.table,
                                         column=ExcControl.K_P,
                                         row_id=row_id)
        else:
            kp_after = None

        # K_Ia
        if switch_command_line is not False:
            k_ia_before = get_.get_cell_row(table=ExcControl.table,
                                            column=ExcControl.K_Ia,
                                            row_id=row_id)
        else:
            k_ia_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.K_Ia,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=K_Ia)

        if switch_command_line is not False:
            k_ia_after = get_.get_cell_row(table=ExcControl.table,
                                           column=ExcControl.K_Ia,
                                           row_id=row_id)
        else:
            k_ia_after = None

        # Tf
        if switch_command_line is not False:
            tf_before = get_.get_cell_row(table=ExcControl.table,
                                          column=ExcControl.Tf,
                                          row_id=row_id)
        else:
            tf_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Tf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Tf)

        if switch_command_line is not False:
            tf_after = get_.get_param(table=ExcControl.table,
                                      column=ExcControl.Tf,
                                      row_id=row_id)
        else:
            tf_after = None

        # Kf
        if switch_command_line is not False:
            kf_before = get_.get_param(table=ExcControl.table,
                                       column=ExcControl.Kf,
                                       row_id=row_id)
        else:
            kf_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf)
        if switch_command_line is not False:
            kf_after = get_.get_param(table=ExcControl.table,
                                      column=ExcControl.Kf,
                                      row_id=row_id)
        else:
            kf_after = None

        # Kf1
        if switch_command_line is not False:
            kf1_before = get_.get_param(table=ExcControl.table,
                                        column=ExcControl.Kf1,
                                        row_id=row_id)
        else:
            kf1_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.Kf1,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=Kf1)

        if switch_command_line is not False:
            kf1_after = get_.get_param(table=ExcControl.table,
                                       column=ExcControl.Kf1,
                                       row_id=row_id)
        else:
            kf1_after = None

        # TINT
        if switch_command_line is not False:
            tint_before = get_.get_param(table=ExcControl.table,
                                         column=ExcControl.TINT,
                                         row_id=row_id)
        else:
            tint_before = None

        variable_.make_changes_setsel(table=ExcControl.table,
                                      column=ExcControl.TINT,
                                      key=f'{ExcControl.Id}={Id}',
                                      value=TINT)

        if switch_command_line is not False:
            tint_after = get_.get_param(table=ExcControl.table,
                                        column=ExcControl.TINT,
                                        row_id=row_id)
        else:
            tint_after = None

        if switch_command_line is not False:
            print(
                f'{separator_grid}\n'
                f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
                f'- row_id: порядковый номер в таблице (от 0 до [max.count]);: {row_id}\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: до {ku_before}; после {ku_after};\n'
                f'- K_Q: Коэффициент усиления канала по производной тока ротора: до {k_q_before}; после {k_q_after};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора: до {kif1_before}; после {kif1_after};\n'
                f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: до {t1if_before}; после {t1if_after};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения: до {ku1_before}; после {ku1_after};\n'
                f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: до {t1u1_before}; после {t1u1_after};\n'
                f'- K_P: Коэффициент усиления выходного сигнала ОМВ: до {kp_before}; после {kp_after};\n'
                f'- K_Ia: Уставка ограничителя максимального тока ротора: до {k_ia_before}; после {k_ia_after};\n'
                f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: до {tf_before}; после {tf_after};\n'
                f'- Kf: Коэффициент усиления в канале по частоте: до {kf_before}; после {kf_after};\n'
                f'- Kf1: Коэффициент усиления в канале по производной частоты: до {kf1_before}; после {kf1_after};\n'
                f'- TINT: Постоянная времени интегратора: до {tint_before}; после {tint_after};\n'
                f'{separator_grid}\n'
            )


def get_parameters(
        Id: int = None,
        row_id: int = None,
        rastr_win=RASTR,
        switch_command_line: bool = False):
    """

    :param Id: Номер возбудителя;
    :param row_id: порядковый номер в таблице (от 0 до [max.count]);
    :param rastr_win: COM - объект Rastr.Astra (win32com);
    :param switch_command_line:
    :return:
    """
    get_ = GettingParameter(rastr_win=rastr_win)

    if Id is not None and row_id is None:
        # Ku
        if switch_command_line is not None:
            ku = get_.get_cell_id(table=ExcControl.table,
                                  column=ExcControl.Ku,
                                  Id=Id)
        else:
            ku = None

        # K_Q
        if switch_command_line is not None:
            k_q = get_.get_cell_id(table=ExcControl.table,
                                   column=ExcControl.K_Q,
                                   Id=Id)
        else:
            k_q = None

        # Kif1
        if switch_command_line is not None:
            kif1 = get_.get_cell_id(table=ExcControl.table,
                                    column=ExcControl.Kif1,
                                    Id=Id)
        else:
            kif1 = None

        # T1if
        if switch_command_line is not None:
            t1if = get_.get_cell_id(table=ExcControl.table,
                                    column=ExcControl.T1if,
                                    Id=Id)
        else:
            t1if = None

        # Ku1
        if switch_command_line is not None:
            ku1 = get_.get_cell_id(table=ExcControl.table,
                                   column=ExcControl.Ku1,
                                   Id=Id)
        else:
            ku1 = None

        # T1u1
        if switch_command_line is not None:
            t1u1 = get_.get_cell_id(table=ExcControl.table,
                                    column=ExcControl.T1u1,
                                    Id=Id)
        else:
            t1u1 = None

        # K_P
        if switch_command_line is not None:
            kp = get_.get_cell_id(table=ExcControl.table,
                                  column=ExcControl.K_P,
                                  Id=Id)
        else:
            kp = None

        # K_Ia
        if switch_command_line is not None:
            k_ia = get_.get_cell_id(table=ExcControl.table,
                                    column=ExcControl.K_Ia,
                                    Id=Id)
        else:
            k_ia = None

        # Tf
        if switch_command_line is not None:
            tf = get_.get_cell_id(table=ExcControl.table,
                                  column=ExcControl.Tf,
                                  Id=Id)
        else:
            tf = None

        # Kf
        if switch_command_line is not None:
            kf = get_.get_cell_id(table=ExcControl.table,
                                  column=ExcControl.Kf,
                                  Id=Id)
        else:
            kf = None

        # Kf1
        if switch_command_line is not None:
            kf1 = get_.get_cell_id(table=ExcControl.table,
                                   column=ExcControl.Kf1,
                                   Id=Id)
        else:
            kf1 = None

        # TINT
        if switch_command_line is not None:
            tint = get_.get_cell_id(table=ExcControl.table,
                                    column=ExcControl.TINT,
                                    Id=Id)
        else:
            tint = None

        if switch_command_line is not False:
            print(
                f'{separator_grid}\n'
                f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
                f'- Id: Номер возбудителя: {Id}\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: {ku};\n'
                f'- K_Q: Коэффициент усиления канала по производной тока ротора: {k_q};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора: {kif1};\n'
                f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: {t1if};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения: {ku1};\n'
                f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: {t1u1};\n'
                f'- K_P: Коэффициент усиления выходного сигнала ОМВ: {kp};\n'
                f'- K_Ia: Уставка ограничителя максимального тока ротора: {k_ia};\n'
                f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: {tf};\n'
                f'- Kf: Коэффициент усиления в канале по частоте: {kf};\n'
                f'- Kf1: Коэффициент усиления в канале по производной частоты: {kf1};\n'
                f'- TINT: Постоянная времени интегратора: {tint};\n'
                f'{separator_grid}\n'
            )
        return (
            f'{separator_grid}\n'
            f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
            f'- Id: Номер возбудителя: {Id}\n'
            f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: {ku};\n'
            f'- K_Q: Коэффициент усиления канала по производной тока ротора: {k_q};\n'
            f'- Kif1: Коэффициент усиления канала по производной тока ротора: {kif1};\n'
            f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: {t1if};\n'
            f'- Ku1: Коэффициент усиления канала по производной напряжения: {ku1};\n'
            f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: {t1u1};\n'
            f'- K_P: Коэффициент усиления выходного сигнала ОМВ: {kp};\n'
            f'- K_Ia: Уставка ограничителя максимального тока ротора: {k_ia};\n'
            f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: {tf};\n'
            f'- Kf: Коэффициент усиления в канале по частоте: {kf};\n'
            f'- Kf1: Коэффициент усиления в канале по производной частоты: {kf1};\n'
            f'- TINT: Постоянная времени интегратора: {tint};\n'
            f'{separator_grid}\n'
        )

    if row_id is not None and Id is None:
        # Ku
        if switch_command_line is not False:
            ku = get_.get_cell_row(table=ExcControl.table,
                                   column=ExcControl.Ku,
                                   row_id=row_id)
        else:
            ku = None

        # K_Q
        if switch_command_line is not False:
            k_q = get_.get_cell_row(table=ExcControl.table,
                                    column=ExcControl.K_Q,
                                    row_id=row_id)
        else:
            k_q = None

        # Kif1
        if switch_command_line is not False:
            kif1 = get_.get_cell_row(table=ExcControl.table,
                                     column=ExcControl.Kif1,
                                     row_id=row_id)
        else:
            kif1 = None

        # T1if
        if switch_command_line is not False:
            t1if = get_.get_cell_row(table=ExcControl.table,
                                     column=ExcControl.T1if,
                                     row_id=row_id)
        else:
            t1if = None

        # Ku1
        if switch_command_line is not False:
            ku1 = get_.get_cell_row(table=ExcControl.table,
                                    column=ExcControl.Ku1,
                                    row_id=row_id)
        else:
            ku1 = None

        # T1u1
        if switch_command_line is not False:
            t1u1 = get_.get_cell_row(table=ExcControl.table,
                                     column=ExcControl.T1u1,
                                     row_id=row_id)
        else:
            t1u1 = None

        # K_P
        if switch_command_line is not False:
            kp = get_.get_cell_row(table=ExcControl.table,
                                   column=ExcControl.K_P,
                                   row_id=row_id)
        else:
            kp = None

        # K_Ia
        if switch_command_line is not False:
            k_ia = get_.get_cell_row(table=ExcControl.table,
                                     column=ExcControl.K_Ia,
                                     row_id=row_id)
        else:
            k_ia = None

        # Tf
        if switch_command_line is not False:
            tf = get_.get_cell_row(table=ExcControl.table,
                                   column=ExcControl.Tf,
                                   row_id=row_id)
        else:
            tf = None

        # Kf
        if switch_command_line is not False:
            kf = get_.get_param(table=ExcControl.table,
                                column=ExcControl.Kf,
                                row_id=row_id)
        else:
            kf = None

        # Kf1
        if switch_command_line is not False:
            kf1 = get_.get_param(table=ExcControl.table,
                                 column=ExcControl.Kf1,
                                 row_id=row_id)
        else:
            kf1 = None

        # TINT
        if switch_command_line is not False:
            tint = get_.get_param(table=ExcControl.table,
                                  column=ExcControl.TINT,
                                  row_id=row_id)
        else:
            tint = None

        if switch_command_line is not False:
            print(
                f'{separator_grid}\n'
                f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
                f'- row_id: порядковый номер в таблице (от 0 до [max.count]);: {row_id}\n'
                f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: {ku};\n'
                f'- K_Q: Коэффициент усиления канала по производной тока ротора: {k_q};\n'
                f'- Kif1: Коэффициент усиления канала по производной тока ротора: {kif1};\n'
                f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: {t1if};\n'
                f'- Ku1: Коэффициент усиления канала по производной напряжения: {ku1};\n'
                f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: {t1u1};\n'
                f'- K_P: Коэффициент усиления выходного сигнала ОМВ: {kp};\n'
                f'- K_Ia: Уставка ограничителя максимального тока ротора: {k_ia};\n'
                f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: {tf};\n'
                f'- Kf: Коэффициент усиления в канале по частоте: {kf};\n'
                f'- Kf1: Коэффициент усиления в канале по производной частоты: {kf1};\n'
                f'- TINT: Постоянная времени интегратора: {tint};\n'
                f'{separator_grid}\n'
            )
        return (
            f'{separator_grid}\n'
            f'Таблица: "{ExcControl.table}" - {ExcControl.table_name}:\n'
            f'- row_id: порядковый номер в таблице (от 0 до [max.count]);: {row_id}\n'
            f'- Ku: Коэффициент усиления пропорционального канала регулятора напряжения: {ku};\n'
            f'- K_Q: Коэффициент усиления канала по производной тока ротора: {k_q};\n'
            f'- Kif1: Коэффициент усиления канала по производной тока ротора: {kif1};\n'
            f'- T1if: Постоянная времени дифференцирующего звена в канале по производной тока ротора: {t1if};\n'
            f'- Ku1: Коэффициент усиления канала по производной напряжения: {ku1};\n'
            f'- T1u1: Постоянная времени дифференцирующего звена в канале по производной напряжения: {t1u1};\n'
            f'- K_P: Коэффициент усиления выходного сигнала ОМВ: {kp};\n'
            f'- K_Ia: Уставка ограничителя максимального тока ротора: {k_ia};\n'
            f'- Tf: Постоянная времени дифференцирующего звена в канале по частоте: {tf};\n'
            f'- Kf: Коэффициент усиления в канале по частоте: {kf};\n'
            f'- Kf1: Коэффициент усиления в канале по производной частоты: {kf1};\n'
            f'- TINT: Постоянная времени интегратора: {tint};\n'
            f'{separator_grid}\n'
        )
