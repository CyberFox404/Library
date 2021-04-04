
'''
https://softwareengineering.stackexchange.com/questions/418300/python-dynamically-import-modules
https://pypi.org/project/dynamic-import/
https://www.tutorialspoint.com/How-I-can-dynamically-import-Python-module
https://www.blog.pythonlibrary.org/2012/07/31/advanced-python-how-to-dynamically-load-modules-or-classes/
https://stackoverflow.com/questions/11108628/python-dynamic-from-import

'''

class CyberFunction(object):
    
    def __init__(self):
        pass

    def _pip_install(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    def _import(self, _from, _import = ""):       
        _from_package = _from.split('.')              
                
        if _import:
            try:
                _ans = getattr(importlib.import_module(_from), _import)
            except ImportError:
                self._pip_install(_from_package[0])
            finally:
                _ans = getattr(importlib.import_module(_from), _import)
        else:
            _import = _from
            try:
                _ans = importlib.import_module(_import)
            except ImportError:
                self._pip_install(_from_package[0])
            finally:
                _ans = importlib.import_module(_import)

        return _ans
