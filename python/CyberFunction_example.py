import importlib
import subprocess
import os
import sys

from CyberFunction import *

cbf = CyberFunction()
        
np = cbf._import("numpy")
plt = cbf._import("matplotlib.pyplot")
odeint = cbf._import("scipy.integrate", "odeint")

ts = np.linspace(0,10,101)