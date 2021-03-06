# -*- coding: utf-8 -*-

from RastrWinLib.Load import load_file
from RastrWinLib.Load.shablon import shablon_file_dynamic, test_9_rst, shablon_file_ut_common
from RastrWinLib.Settings.dynamic import set_dynamic
from RastrWinLib.Load.save import save_file

load_file(file_path=test_9_rst,
          shablon=shablon_file_dynamic)
load_file(shablon=shablon_file_ut_common)

# set_regim(switch_command_line=True)
# set_ut_common(switch_command_line=True)
# set_com_ekviv(switch_command_line=True)

set_dynamic(switch_command_line=True)

save_file(file_path=r'C:\Users\Ohrimenko_AG\Desktop\Test_equiPy\test9_123.rst',
          shablon=shablon_file_dynamic)
