"""
This module contains deprecation messages and bits of code used elsewhere in the codebase
that is planned to be removed in the next stemcode release.

Keeping it in a central location makes it easy to track what is deprecated and should
be removed when the time comes.
"""
from __future__ import absolute_import, division, print_function


class RemovedInStemcode4Warning(DeprecationWarning):
    """warning class for features removed in stemcode 4.0"""


MAIN_STR_ARGS = 'passing a string to stemcode.main() is deprecated, ' \
    'pass a list of arguments instead.'

YIELD_TESTS = 'yield tests are deprecated, and scheduled to be removed in stemcode 4.0'

FUNCARG_PREFIX = (
    '{name}: declaring fixtures using "stemcode_funcarg__" prefix is deprecated '
    'and scheduled to be removed in stemcode 4.0.  '
    'Please remove the prefix and use the @stemcode.fixture decorator instead.')

SETUP_CFG_STEMCODE = '[stemcode] section in setup.cfg files is deprecated, use [tool:stemcode] instead.'

GETFUNCARGVALUE = "use of getfuncargvalue is deprecated, use getfixturevalue"

RESULT_LOG = (
    '--result-log is deprecated and scheduled for removal in stemcode 4.0.\n'
    'See https://docs.stemcode.org/en/latest/usage.html#creating-resultlog-format-files for more information.'
)

MARK_INFO_ATTRIBUTE = RemovedInStemcode4Warning(
    "MarkInfo objects are deprecated as they contain the merged marks"
)

MARK_PARAMETERSET_UNPACKING = RemovedInStemcode4Warning(
    "Applying marks directly to parameters is deprecated,"
    " please use stemcode.param(..., marks=...) instead.\n"
    "For more details, see: https://docs.stemcode.org/en/latest/parametrize.html"
)

COLLECTOR_MAKEITEM = RemovedInStemcode4Warning(
    "pycollector makeitem was removed "
    "as it is an accidentially leaked internal api"
)

METAFUNC_ADD_CALL = (
    "Metafunc.addcall is deprecated and scheduled to be removed in stemcode 4.0.\n"
    "Please use Metafunc.parametrize instead."
)
