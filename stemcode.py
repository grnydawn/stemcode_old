# PYTHON_ARGCOMPLETE_OK
"""
stemcode: Command-line application framework.
"""


# else we are imported

from _stemcode.config import (
    main, UsageError, cmdline,
    hookspec, hookimpl
)

#from _stemcode.fixtures import fixture, yield_fixture
#from _stemcode.assertion import register_assert_rewrite
#from _stemcode.freeze_support import freeze_includes
from _stemcode import __version__
#from _stemcode.debugging import stemcodePDB as __stemcodePDB
#from _stemcode.recwarn import warns, deprecated_call
#from _stemcode.outcomes import fail, skip, importorskip, exit, xfail
#from _stemcode.mark import MARK_GEN as mark, param
#from _stemcode.main import Session
#from _stemcode.nodes import Item, Collector, File
#from _stemcode.fixtures import fillfixtures as _fillfuncargs
#from _stemcode.python import (
#    Module, Class, Instance, Function, Generator,
#)

#from _stemcode.python_api import approx, raises

#set_trace = __stemcodePDB.set_trace

__all__ = [
    'main',
    'UsageError',
    'cmdline',
    'exthookspec',
    'exthookimpl',
    'langhookspec',
    'langhookimpl',
    '__version__',
#    'register_assert_rewrite',
#    'freeze_includes',
#    'set_trace',
#    'warns',
#    'deprecated_call',
#    'fixture',
#    'yield_fixture',
#    'fail',
#    'skip',
#    'xfail',
#    'importorskip',
#    'exit',
#    'mark',
#    'param',
#    'approx',
#    '_fillfuncargs',
#
#    'Item',
#    'File',
#    'Collector',
#    'Session',
#    'Module',
#    'Class',
#    'Instance',
#    'Function',
#    'Generator',
#    'raises',


]

if __name__ == '__main__':
    # if run as a script or by 'python -m stemcode'
    # we trigger the below "else" condition by the following import
    import stemcode
    raise SystemExit(stemcode.main())
else:
    pass
    #from _stemcode.compat import _setup_collect_fakemodule
    #_setup_collect_fakemodule()
