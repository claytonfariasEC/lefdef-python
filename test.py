import lefdef
from lefdef import C_LefReader
from lefdef import C_DefReader



def_reader = C_DefReader()
_def = def_reader.read(".\datapath.def")
_def.print()


#COMO MANIPULAR ISSO
lista = _def.c_g_cell_grid_x


#for i in lista:
#    print(i)
