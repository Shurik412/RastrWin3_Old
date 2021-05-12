import win32com.client

from RastrWinLib.calculation.regim import SteadyState
from RastrWinLib.getting.get import GettingParameter
from RastrWinLib.loading.load import load_file
from RastrWinLib.loading.save import save_file
from RastrWinLib.loading.shablon import Shabl
from RastrWinLib.tables.Dynamic.Generator import Generator
from RastrWinLib.tables.Node.node import Node
from RastrWinLib.tables.Vetv.vetv import Vetv
from RastrWinLib.tables.area.area import Area
from RastrWinLib.variables.group_correction import GroupCorr
from RastrWinLib.variables.variable_parametrs import FindNextSel, Variable

dir_file = r'L:\SER\Охрименко\03. RastrWin3\18'
file_one_rg2 = rf'{dir_file}\4.rg2'
file_two_rst = rf'{dir_file}\Дин модель Лето минимум.rst'
file_log_gen = rf'{dir_file}\log_set_gen.txt'
file_log_vetv = rf'{dir_file}\log_set_vetv.txt'
file_log_node = rf'{dir_file}\log_set_node.txt'
file_log_area = rf'{dir_file}\log_set_area.txt'

n = open(file_log_node, 'w')
f = open(file_log_gen, 'w')
g = open(file_log_vetv, 'w')
area = open(file_log_area, 'w')

one_rastr = win32com.client.Dispatch("Astra.Rastr")
two_rastr = win32com.client.Dispatch("Astra.Rastr")

load_file(rastr_win=one_rastr, file_path=file_one_rg2, shabl=Shabl.shablon_file_regime, switch_command_line=False)
load_file(rastr_win=two_rastr, file_path=file_two_rst, shabl=Shabl.shablon_file_dynamic, switch_command_line=False)

gen_table_file_one = one_rastr.Tables(Generator.table)
max_column_gen_file_one = gen_table_file_one.Count - 1
print(f'Max Gen file_one: {max_column_gen_file_one}')

get_one = GettingParameter(rastr_win=one_rastr)
get_two = GettingParameter(rastr_win=two_rastr)

# ********** Генератор ****************
for i in range(0, max_column_gen_file_one):
    """
    Извлекает из файла rg2 (файл 1), Название, Номер, Состояние, P, Q из таблиццы Генераторы ИД
    """
    name_gen_file_one = get_one.get_cell_row(table=Generator.table, column=Generator.Name, row_id=i)
    num_gen_file_one = get_one.get_cell_row(table=Generator.table, column=Generator.Num, row_id=i)
    sta_gen_file_one = get_one.get_cell_row(table=Generator.table, column=Generator.sta, row_id=i)
    p_gen_gen_file_one = get_one.get_cell_row(table=Generator.table, column=Generator.P, row_id=i)
    q_gen_gen_file_one = get_one.get_cell_row(table=Generator.table, column=Generator.Q, row_id=i)

    """
    Находит в файле rst (файл 2), генератор по номеру генератора из файла 1 rg2
    Возвращает порядковый номер в таблице
    """
    row_obj_gen_file_two = get_two.get_row_gen(num_gen_file_one)
    row_gen_file_two = row_obj_gen_file_two
    print(f'row_gen_file_two={row_gen_file_two}')
    if row_gen_file_two != (-1):
        p_gen_gen_file_two = get_two.get_cell_row(table=Generator.table,
                                                  column=Generator.P,
                                                  row_id=row_gen_file_two)

        val_file_two = Variable(rastr_win=two_rastr, switch_command_line=False)

        val_file_two.make_changes_row(table=Generator.table,
                                      column=Generator.P,
                                      row_id=row_gen_file_two,
                                      value=p_gen_gen_file_one)

        val_file_two.make_changes_row(table=Generator.table,
                                      column=Generator.Q,
                                      row_id=row_gen_file_two,
                                      value=q_gen_gen_file_one)

        val_file_two.make_changes_row(table=Generator.table,
                                      column=Generator.sta,
                                      row_id=row_gen_file_two,
                                      value=sta_gen_file_one)

        name_gen_file_two = get_two.get_cell_row(table=Generator.table,
                                                 column=Generator.Name,
                                                 row_id=row_gen_file_two)

        p_gen_obj_gen_file_one_afte = Variable(rastr_win=two_rastr,
                                               switch_command_line=False)
        pg_after = p_gen_obj_gen_file_one_afte.make_changes_row(table=Generator.table,
                                                                column=Generator.P,
                                                                row_id=row_gen_file_two)

        f.write(f'{i}. Row_id={row_gen_file_two} - Num={num_gen_file_one} - Name={name_gen_file_one}:'
                f' P до = {p_gen_gen_file_two} => P после = {pg_after}\n')
f.close()

# ********** Ветвь ****************
vetv_table_file_one = one_rastr.Tables(Vetv.table)
max_col_vetv_file_one = vetv_table_file_one.Count - 1
print(f'Max VETV file_one: {max_col_vetv_file_one}')

for j in range(0, max_col_vetv_file_one):
    # файл 1
    ip_vetv_file_one = get_one.get_cell_row(table=Vetv.table, column=Vetv.ip, row_id=j)
    iq_vetv_file_one = get_one.get_cell_row(table=Vetv.table, column=Vetv.iq, row_id=j)
    np_vetv_file_one = get_one.get_cell_row(table=Vetv.table, column=Vetv.np, row_id=j)
    name_vetv_file_one = get_one.get_cell_row(table=Vetv.table, column=Vetv.sta, row_id=j)
    sta_vetv_file_one = get_one.get_cell_row(table=Vetv.table, column=Vetv.name, row_id=j)

    # файл 2
    row_vetv_file_two = get_two.get_row_vetv(ip=ip_vetv_file_one, iq=iq_vetv_file_one, np=np_vetv_file_one)

    if row_vetv_file_two != (-1):
        sta_vetv_file_two_do = get_two.get_cell_row(table=Vetv.table,
                                                    column=Vetv.sta,
                                                    row_id=row_vetv_file_two)

        var_vetv_file_two = Variable(rastr_win=two_rastr, switch_command_line=False)
        var_vetv_file_two.make_changes_row(table=Vetv.table,
                                           column=Vetv.sta,
                                           row_id=row_vetv_file_two,
                                           value=sta_vetv_file_one)

        sta_vetv_file_two_posle = get_two.get_cell(table=Vetv.table,
                                                   column=Vetv.sta,
                                                   row_id=row_vetv_file_two)

        g.write(
            f'{j}. Row_id={row_vetv_file_two} - Name={name_vetv_file_one}: sta_FILE 1 = {sta_vetv_file_one} => sta_FILE 2 = {sta_vetv_file_two_do} => sta_FILE New = {sta_vetv_file_two_posle}\n')
g.close()

node_fl = 0

if node_fl == 1:
    # # ********** Узлы ****************
    node_table_file_one = one_rastr.Tables(Node.table)
    max_col_node_file_one = node_table_file_one.Count - 1
    print(f'Max Node file_one: {max_col_node_file_one}')

    ny_obj_node_file_one = GettingParameter(rastr_win=one_rastr)
    name_obj_node_file_one = GettingParameter(rastr_win=one_rastr)
    sta_obj_node_file_one = GettingParameter(rastr_win=one_rastr)
    vzd_obj_node_file_one = GettingParameter(rastr_win=one_rastr)
    p_obj_node_file_one = GettingParameter(rastr_win=one_rastr)
    q_obj_node_file_one = GettingParameter(rastr_win=one_rastr)

    for y in range(0, max_col_node_file_one):
        # файл 1
        ny_node_file_one = ny_obj_node_file_one.get_cell_row(table=Node.table, column=Node.ny, row_id=y)
        p_node_file_one = p_obj_node_file_one.get_cell_row(table=Node.table, column=Node.name, row_id=y)
        q_node_file_one = q_obj_node_file_one.get_cell(table=Node.table, column=Node.sta, row_id=y)
        name_node_file_one = name_obj_node_file_one.get_cell(table=Node.table, column=Node.vzd, row_id=y)
        sta_node_file_one = sta_obj_node_file_one.get_cell(table=Node.table, column=Node.pg, row_id=y)
        vzd_node_file_one = vzd_obj_node_file_one.get_cell(table=Node.table, column=Node.qg, row_id=y)

        # файл 2
        get_two = GettingParameter(rastr_win=two_rastr)
        row_node_file_two = get_two.get_row_node(node_ny=ny_node_file_one)

        if row_node_file_two != (-1):
            ny_node_file_two = get_two.get_cell(table=Node.table,
                                                column=Node.ny,
                                                row_id=row_node_file_two)

            name_node_file_two = get_two.get_cell(table=Node.table,
                                                  column=Node.name,
                                                  row_id=row_node_file_two)

            sta_node_file_two_do = get_two.get_cell(table=Node.table,
                                                    column=Node.sta,
                                                    row_id=row_node_file_two)

            p_obj_node_file_two = Variable(rastr_win=two_rastr, switch_command_line=False)
            p_obj_node_file_two.make_changes_row(table=Node.table,
                                                 column=Node.pg,
                                                 row_id=row_node_file_two,
                                                 value=p_node_file_one)

            q_obj_node_file_two = Variable(rastr_win=two_rastr, switch_command_line=False)
            q_obj_node_file_two.make_changes_row(table=Node.table,
                                                 column=Node.qg,
                                                 row_id=row_node_file_two,
                                                 value=q_node_file_one)

            sta_obj_node_file_two = Variable(rastr_win=two_rastr, switch_command_line=False)
            sta_obj_node_file_two.make_changes_row(table=Node.table,
                                                   column=Node.sta,
                                                   row_id=row_node_file_two,
                                                   value=sta_node_file_one)

            vzd_obj_node_file_two = Variable(rastr_win=two_rastr, switch_command_line=False)
            vzd_obj_node_file_two.make_changes_row(table=Node.table,
                                                   column=Node.vzd,
                                                   row_id=row_node_file_two,
                                                   value=vzd_node_file_one)

            sta_node_obj_file_two_posle = Variable(rastr_win=two_rastr,
                                                   switch_command_line=False)
            sta_node_file_two_posle = sta_node_obj_file_two_posle.make_changes_row(table=Node.table,
                                                                                   column=Node.sta,
                                                                                   row_id=row_node_file_two)

            vzd_node_obj_file_two_posle = Variable(rastr_win=two_rastr,
                                                   switch_command_line=False)
            vzd_node_file_two_posle = vzd_node_obj_file_two_posle.make_changes_row(table=Node.table,
                                                                                   column=Node.vzd,
                                                                                   row_id=row_node_file_two)

            n.write(
                f'{y}. Row_id={row_node_file_two}; File_1: ny={ny_node_file_one}; name={name_node_file_one}; sta={sta_node_file_one}; vzd={vzd_node_file_one} -> File_2 ny={ny_node_file_two}; name={name_node_file_two}; sta_FILE До = {sta_node_file_two_do} => sta_FILE New = {sta_node_file_two_posle}; vzd_posle={vzd_node_file_two_posle}\n')
    n.close()

area_fl = 0

if area_fl == 1:
    # ********** Районы ****************
    area_table_file_one = one_rastr.Tables(Area.table)
    max_col_area_file_one = area_table_file_one.Count - 1
    print(f'Max Area file_one: {max_col_area_file_one}')

    for x in range(0, max_col_area_file_one):
        na_area_node_file_one = get_.get_cell(table=Area.table, column=Area.na, row_id=x)

        name_area_node_file_one = get_.get_cell(table=Area.table, column=Area.name, row_id=x)

        pg_area_node_file_one = get_.get_cell(table=Area.table, column=Area.pg, row_id=x)

        pn_area_file_one = get_.get_cell(table=Area.table, column=Area.pn, row_id=x)

        if na_area_node_file_one > 0:
            row_obj_area_file_two = FindNextSel(rastr_win=two_rastr, table=Area.table, key=f"na={pn_area_file_one}")
            row_area_file_two = row_obj_area_file_two.row()

            if row_area_file_two != (-1):
                na_file_two = get_two.get_cell(table=Area.table, column=Area.na, row_id=row_area_file_two)

                pg_area_file_two = get_two.get_cell(table=Area.table, column=Area.pg, row_id=row_area_file_two)

                if pg_area_file_two > 0:
                    k_pg = pg_area_node_file_one / pg_area_file_two
                else:
                    k_pg = 1

                grupCorr_pg_file_two = GroupCorr(rastr_win=two_rastr, table=Node.table, column=Node.pg,
                                                 switch_command_line=True)
                grupCorr_pg_file_two.calc(key=f'na={na_file_two}', formula=f'pg*{k_pg}')

                na_area_node_file_two = get_two.get_cell(table=Area.table, column=Area.na, row_id=row_area_file_two)

                name_area_file_two = get_two.get_cell(table=Area.table, column=Area.name, row_id=row_area_file_two)

                pg_area_node_file_two = get_two.get_cell(table=Area.table, column=Area.pg, row_id=row_area_file_two)

                pn_area_node_file_two = get_two.get_cell(table=Area.table, column=Area.pn, row_id=row_area_file_two)

                area.write(
                    f'{x}. na_f1={na_area_node_file_one}; name_f1={name_area_node_file_one}; pg_f1={pg_area_node_file_one} => na_f2={na_area_node_file_two}; name_f2={name_area_file_two}; pg_f2={pg_area_node_file_two}; k_pg={k_pg}\n')

    area.close()

save_file(rastr_win=two_rastr, file_path=rf'{dir_file}\Режим 14.rst',
          shabl=Shabl.shablon_file_dynamic, switch_command_line=True)
