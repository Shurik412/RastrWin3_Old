from RastrWinLib.ActionsObject.Get import GettingParameter
from RastrWinLib.Load import load_file
from RastrWinLib.Load.shablon import Shabl
from RastrWinLib.AstraRastr import RASTR

file = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst'
load_file(file_path=file,
          shabl=Shabl.shablon_file_dynamic)

get_ = GettingParameter(rastr_win=RASTR)

t = get_.get_row_vetv_a_node(ny=349)
print(t)
# r = get_.get_cell_id(table=ExcControl.table, column=ExcControl.Ku, Id=1320)
# print(r)
#
# trr = get_.get_cell_id(table=ExcControl.table,
#                        column=ExcControl.Tf,
#                        Id=1320)
# print(trr)
