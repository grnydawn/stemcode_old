""" hook specifications for stemcode plugins, invoked from main.py and builtin plugins.  """

from pluggy import HookspecMarker

hookspec = HookspecMarker("stemcode")

# -------------------------------------------------------------------------
# Initialization hooks called for every plugin
# -------------------------------------------------------------------------


@hookspec(historic=True)
def stemcode_addhooks(pluginmanager):
    """called at plugin registration time to allow adding new hooks via a call to
    ``pluginmanager.add_hookspecs(module_or_class, prefix)``.


    :param _stemcode.config.StemcodePluginManager pluginmanager: stemcode plugin manager

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def stemcode_namespace():
    """
    (**Deprecated**) this hook causes direct monkeypatching on stemcode, its use is strongly discouraged
    return dict of name->object to be made globally available in
    the stemcode namespace.

    This hook is called at plugin registration time.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def stemcode_plugin_registered(plugin, manager):
    """ a new stemcode plugin got registered.

    :param plugin: the plugin module or instance
    :param _stemcode.config.StemcodePluginManager manager: stemcode plugin manager

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def stemcode_addoption(parser):
    """register argparse-style options and ini-style config values,
    called once at the beginning of a test run.

    .. note::

        This function should be implemented only in plugins or ``conftest.py``
        files situated at the tests root directory due to how stemcode
        :ref:`discovers plugins during startup <pluginorder>`.

    :arg _stemcode.config.Parser parser: To add command line options, call
        :py:func:`parser.addoption(...) <_stemcode.config.Parser.addoption>`.
        To add ini-file values call :py:func:`parser.addini(...)
        <_stemcode.config.Parser.addini>`.

    Options can later be accessed through the
    :py:class:`config <_stemcode.config.Config>` object, respectively:

    - :py:func:`config.getoption(name) <_stemcode.config.Config.getoption>` to
      retrieve the value of a command line option.

    - :py:func:`config.getini(name) <_stemcode.config.Config.getini>` to retrieve
      a value read from an ini-style file.

    The config object is passed around on many internal objects via the ``.config``
    attribute or can be retrieved as the ``stemcodeconfig`` fixture.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """


@hookspec(historic=True)
def stemcode_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.

    This hook is called for every plugin and initial conftest file
    after command line options have been parsed.

    After that, the hook is called for other conftest files as they are
    imported.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.

    :arg _stemcode.config.Config config: stemcode config object
    """

# -------------------------------------------------------------------------
# Bootstrapping hooks called for plugins registered early enough:
# internal and 3rd party plugins.
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def stemcode_cmdline_parse(pluginmanager, args):
    """return initialized config object, parsing the specified args.

    Stops at first non-None result, see :ref:`firstresult`

    .. note::
        This hook will not be called for ``conftest.py`` files, only for setuptools plugins.

    :param _stemcode.config.StemcodePluginManager pluginmanager: stemcode plugin manager
    :param list[str] args: list of arguments passed on the command line
    """


def stemcode_cmdline_preparse(config, args):
    """(**Deprecated**) modify command line arguments before option parsing.

    This hook is considered deprecated and will be removed in a future stemcode version. Consider
    using :func:`stemcode_load_initial_conftests` instead.

    .. note::
        This hook will not be called for ``conftest.py`` files, only for setuptools plugins.

    :param _stemcode.config.Config config: stemcode config object
    :param list[str] args: list of arguments passed on the command line
    """


@hookspec(firstresult=True)
def stemcode_cmdline_main(config):
    """ called for performing the main command line action. The default
    implementation will invoke the configure hooks and runtest_mainloop.

    .. note::
        This hook will not be called for ``conftest.py`` files, only for setuptools plugins.

    Stops at first non-None result, see :ref:`firstresult`

    :param _stemcode.config.Config config: stemcode config object
    """


def stemcode_load_initial_conftests(early_config, parser, args):
    """ implements the loading of initial conftest files ahead
    of command line option parsing.

    .. note::
        This hook will not be called for ``conftest.py`` files, only for setuptools plugins.

    :param _stemcode.config.Config early_config: stemcode config object
    :param list[str] args: list of arguments passed on the command line
    :param _stemcode.config.Parser parser: to add command line options
    """


# -------------------------------------------------------------------------
# collection hooks
# -------------------------------------------------------------------------

@hookspec(firstresult=True)
def stemcode_collection(session):
    """Perform the collection protocol for the given session.

    Stops at first non-None result, see :ref:`firstresult`.

    :param _stemcode.main.Session session: the stemcode session object
    """


def stemcode_collection_modifyitems(session, config, items):
    """ called after collection has been performed, may filter or re-order
    the items in-place.

    :param _stemcode.main.Session session: the stemcode session object
    :param _stemcode.config.Config config: stemcode config object
    :param List[_stemcode.nodes.Item] items: list of item objects
    """


def stemcode_collection_finish(session):
    """ called after collection has been performed and modified.

    :param _stemcode.main.Session session: the stemcode session object
    """


@hookspec(firstresult=True)
def stemcode_ignore_collect(path, config):
    """ return True to prevent considering this path for collection.
    This hook is consulted for all files and directories prior to calling
    more specific hooks.

    Stops at first non-None result, see :ref:`firstresult`

    :param str path: the path to analyze
    :param _stemcode.config.Config config: stemcode config object
    """


@hookspec(firstresult=True)
def stemcode_collect_directory(path, parent):
    """ called before traversing a directory for collection files.

    Stops at first non-None result, see :ref:`firstresult`

    :param str path: the path to analyze
    """


def stemcode_collect_file(path, parent):
    """ return collection Node or None for the given path. Any new node
    needs to have the specified ``parent`` as a parent.

    :param str path: the path to collect
    """

# logging hooks for collection


def stemcode_collectstart(collector):
    """ collector starts collecting. """


def stemcode_itemcollected(item):
    """ we just collected a test item. """


def stemcode_collectreport(report):
    """ collector finished collecting. """


def stemcode_deselected(items):
    """ called for test items deselected by keyword. """


@hookspec(firstresult=True)
def stemcode_make_collect_report(collector):
    """ perform ``collector.collect()`` and return a CollectReport.

    Stops at first non-None result, see :ref:`firstresult` """

# -------------------------------------------------------------------------
# Python test function related hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def stemcode_pycollect_makemodule(path, parent):
    """ return a Module collector or None for the given path.
    This hook will be called for each matching test module path.
    The stemcode_collect_file hook needs to be used if you want to
    create test modules for files that do not match as a test module.

    Stops at first non-None result, see :ref:`firstresult` """


@hookspec(firstresult=True)
def stemcode_pycollect_makeitem(collector, name, obj):
    """ return custom item/collector for a python object in a module, or None.

    Stops at first non-None result, see :ref:`firstresult` """


@hookspec(firstresult=True)
def stemcode_pyfunc_call(pyfuncitem):
    """ call underlying test function.

    Stops at first non-None result, see :ref:`firstresult` """


def stemcode_generate_tests(metafunc):
    """ generate (multiple) parametrized calls to a test function."""


@hookspec(firstresult=True)
def stemcode_make_parametrize_id(config, val, argname):
    """Return a user-friendly string representation of the given ``val`` that will be used
    by @stemcode.mark.parametrize calls. Return None if the hook doesn't know about ``val``.
    The parameter name is available as ``argname``, if required.

    Stops at first non-None result, see :ref:`firstresult`

    :param _stemcode.config.Config config: stemcode config object
    :param val: the parametrized value
    :param str argname: the automatic parameter name produced by stemcode
    """

# -------------------------------------------------------------------------
# generic runtest related hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def stemcode_runtestloop(session):
    """ called for performing the main runtest loop
    (after collection finished).

    Stops at first non-None result, see :ref:`firstresult`

    :param _stemcode.main.Session session: the stemcode session object
    """


def stemcode_itemstart(item, node):
    """(**Deprecated**) use stemcode_runtest_logstart. """


@hookspec(firstresult=True)
def stemcode_runtest_protocol(item, nextitem):
    """ implements the runtest_setup/call/teardown protocol for
    the given test item, including capturing exceptions and calling
    reporting hooks.

    :arg item: test item for which the runtest protocol is performed.

    :arg nextitem: the scheduled-to-be-next test item (or None if this
                   is the end my friend).  This argument is passed on to
                   :py:func:`stemcode_runtest_teardown`.

    :return boolean: True if no further hook implementations should be invoked.


    Stops at first non-None result, see :ref:`firstresult` """


def stemcode_runtest_logstart(nodeid, location):
    """ signal the start of running a single test item.

    This hook will be called **before** :func:`stemcode_runtest_setup`, :func:`stemcode_runtest_call` and
    :func:`stemcode_runtest_teardown` hooks.

    :param str nodeid: full id of the item
    :param location: a triple of ``(filename, linenum, testname)``
    """


def stemcode_runtest_logfinish(nodeid, location):
    """ signal the complete finish of running a single test item.

    This hook will be called **after** :func:`stemcode_runtest_setup`, :func:`stemcode_runtest_call` and
    :func:`stemcode_runtest_teardown` hooks.

    :param str nodeid: full id of the item
    :param location: a triple of ``(filename, linenum, testname)``
    """


def stemcode_runtest_setup(item):
    """ called before ``stemcode_runtest_call(item)``. """


def stemcode_runtest_call(item):
    """ called to execute the test ``item``. """


def stemcode_runtest_teardown(item, nextitem):
    """ called after ``stemcode_runtest_call``.

    :arg nextitem: the scheduled-to-be-next test item (None if no further
                   test item is scheduled).  This argument can be used to
                   perform exact teardowns, i.e. calling just enough finalizers
                   so that nextitem only needs to call setup-functions.
    """


@hookspec(firstresult=True)
def stemcode_runtest_makereport(item, call):
    """ return a :py:class:`_stemcode.runner.TestReport` object
    for the given :py:class:`stemcode.Item <_stemcode.main.Item>` and
    :py:class:`_stemcode.runner.CallInfo`.

    Stops at first non-None result, see :ref:`firstresult` """


def stemcode_runtest_logreport(report):
    """ process a test setup/call/teardown report relating to
    the respective phase of executing a test. """

# -------------------------------------------------------------------------
# Fixture related hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def stemcode_fixture_setup(fixturedef, request):
    """ performs fixture setup execution.

    :return: The return value of the call to the fixture function

    Stops at first non-None result, see :ref:`firstresult`

    .. note::
        If the fixture function returns None, other implementations of
        this hook function will continue to be called, according to the
        behavior of the :ref:`firstresult` option.
    """


def stemcode_fixture_post_finalizer(fixturedef, request):
    """ called after fixture teardown, but before the cache is cleared so
    the fixture result cache ``fixturedef.cached_result`` can
    still be accessed."""

# -------------------------------------------------------------------------
# test session related hooks
# -------------------------------------------------------------------------


def stemcode_sessionstart(session):
    """ before session.main() is called.

    :param _stemcode.main.Session session: the stemcode session object
    """


def stemcode_sessionfinish(session, exitstatus):
    """ whole test run finishes.

    :param _stemcode.main.Session session: the stemcode session object
    :param int exitstatus: the status which stemcode will return to the system
    """


def stemcode_unconfigure(config):
    """ called before test process is exited.

    :param _stemcode.config.Config config: stemcode config object
    """


# -------------------------------------------------------------------------
# hooks for customizing the assert methods
# -------------------------------------------------------------------------

def stemcode_assertrepr_compare(config, op, left, right):
    """return explanation for comparisons in failing assert expressions.

    Return None for no custom explanation, otherwise return a list
    of strings.  The strings will be joined by newlines but any newlines
    *in* a string will be escaped.  Note that all but the first line will
    be indented slightly, the intention is for the first line to be a summary.

    :param _stemcode.config.Config config: stemcode config object
    """

# -------------------------------------------------------------------------
# hooks for influencing reporting (invoked from _stemcode_terminal)
# -------------------------------------------------------------------------


def stemcode_report_header(config, startdir):
    """ return a string or list of strings to be displayed as header info for terminal reporting.

    :param _stemcode.config.Config config: stemcode config object
    :param startdir: py.path object with the starting dir

    .. note::

        This function should be implemented only in plugins or ``conftest.py``
        files situated at the tests root directory due to how stemcode
        :ref:`discovers plugins during startup <pluginorder>`.
    """


def stemcode_report_collectionfinish(config, startdir, items):
    """
    .. versionadded:: 3.2

    return a string or list of strings to be displayed after collection has finished successfully.

    This strings will be displayed after the standard "collected X items" message.

    :param _stemcode.config.Config config: stemcode config object
    :param startdir: py.path object with the starting dir
    :param items: list of stemcode items that are going to be executed; this list should not be modified.
    """


@hookspec(firstresult=True)
def stemcode_report_teststatus(report):
    """ return result-category, shortletter and verbose word for reporting.

    Stops at first non-None result, see :ref:`firstresult` """


def stemcode_terminal_summary(terminalreporter, exitstatus):
    """ add additional section in terminal summary reporting.  """


@hookspec(historic=True)
def stemcode_logwarning(message, code, nodeid, fslocation):
    """ process a warning specified by a message, a code string,
    a nodeid and fslocation (both of which may be None
    if the warning is not tied to a particular node/location).

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """

# -------------------------------------------------------------------------
# doctest hooks
# -------------------------------------------------------------------------


@hookspec(firstresult=True)
def stemcode_doctest_prepare_content(content):
    """ return processed content for a given doctest

    Stops at first non-None result, see :ref:`firstresult` """

# -------------------------------------------------------------------------
# error handling and internal debugging hooks
# -------------------------------------------------------------------------


def stemcode_internalerror(excrepr, excinfo):
    """ called for internal errors. """


def stemcode_keyboard_interrupt(excinfo):
    """ called for keyboard interrupt. """


def stemcode_exception_interact(node, call, report):
    """called when an exception was raised which can potentially be
    interactively handled.

    This hook is only called if an exception was raised
    that is not an internal exception like ``skip.Exception``.
    """


def stemcode_enter_pdb(config):
    """ called upon pdb.set_trace(), can be used by plugins to take special
    action just before the python debugger enters in interactive mode.

    :param _stemcode.config.Config config: stemcode config object
    """
