__author__ = 'peek'
__version__ = '0.3.5.1'

from txhttputil.util.ModuleUtil import filterModules

for mod in filterModules(__name__, __file__):
    __import__(mod, locals(), globals())

from . import sw_install