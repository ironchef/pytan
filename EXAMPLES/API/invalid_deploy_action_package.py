
"""
Deploy an action using a non-existing package.
"""
# Path to lib directory which contains pytan package
PYTAN_LIB_PATH = '../lib'

# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import sys, tempfile
sys.path.append(PYTAN_LIB_PATH)

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the arguments for the handler method
kwargs = {}
kwargs['report_dir'] = tempfile.gettempdir()
kwargs["run"] = True
kwargs["package"] = u'Invalid Package'


# call the handler with the deploy_action_human method, passing in kwargs for arguments
# this should throw an exception: pytan.utils.HandlerError
import traceback
try:
    handler.deploy_action_human(**kwargs)
except Exception as e:
    traceback.print_exc(file=sys.stdout)



'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
Traceback (most recent call last):
  File "<string>", line 40, in <module>
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1109, in deploy_action_human
    **kwargs
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 919, in deploy_action
    package_def = self._get_package_def(package_def)
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1733, in _get_package_def
    d['package_obj'] = self.get('package', **def_search)[0]
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1509, in get
    return self._get_single(obj_map, **kwargs)
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1693, in _get_single
    for x in self._single_find(obj_map, k, v, **kwargs):
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1703, in _single_find
    obj_ret = self._find(api_obj_single, **kwargs)
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1631, in _find
    raise HandlerError(err(search_str))
HandlerError: No results found searching for PackageSpec, name: u'Invalid Package'!!

'''