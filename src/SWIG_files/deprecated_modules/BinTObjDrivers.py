import warnings
warnings.simplefilter('once', DeprecationWarning)
warnings.warn("OCC.BinTObjDrivers is deprecated since pythonocc-0.18.2. Use OCC.Core.BinTObjDrivers", DeprecationWarning)

from OCC.Core.BinTObjDrivers import *
