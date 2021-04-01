# -*- coding: utf-8 -*-

import win32com.client
from R_modules.load_and_save_file.load_file_rastrwin import LoadRUSTab, load_file
from R_modules.load_and_save_file.shablons_dir import shablon_file_dynamic, shablon_file_scenario, shablon_file_regime
from tabl_com_cxema import tb_com_cxema, par_tb_com_cxema
from R_modules.getting_parameters.get_parameter import GettingParameterAttribute, GettingParameter, GetTableCommonInfo
from R_modules.calculation.dyn_rgm_calc import SteadyState

print('*********************************************')
print('*********** Эквивалентирование **************')
print('*********************************************')

rastr = win32com.client.Dispatch('Astra.Rastr')
regime = SteadyState(rastr_win=rastr, switch_command_line=True)

file_rg2 = r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\cx195.rg2'
load_file(rastr_win=rastr, file_path=file_rg2, shablon=shablon_file_regime, switch_command_line=True)

common_info = GetTableCommonInfo(rastr_win=rastr, switch_command_line=True)
common_info.get()

regime.rgm()





