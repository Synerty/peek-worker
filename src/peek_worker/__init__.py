__author__ = 'peek'

from rapui.Util import filterModules

for mod in filterModules(__name__, __file__):
    __import__(mod, locals(), globals())

from . import sw_install