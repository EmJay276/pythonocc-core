import warnings
warnings.simplefilter('once', DeprecationWarning)
warnings.warn("OCC.Geom2dConvert is deprecated since pythonocc-0.18.2. Use OCC.Core.Geom2dConvert", DeprecationWarning)

from OCC.Core.Geom2dConvert import *
