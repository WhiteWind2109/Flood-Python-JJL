def dynamic_import(module):
    """Returns a module object.
    Dynamically importing a module that was created since the
    interpreter began execution (e.g., installed by pip).

    Usage:
    module = dynamic_import(module_as_string)
    e.g.
    np = dynamic_import('numpy')
    Equivalent to:
    import numpy as np"""

    from importlib import import_module, invalidate_caches

    pkg = import_module(module)

    # Call invalidate_caches() in order for the new module to
    # be noticed by the import system.
    invalidate_caches()

    print("Module '%s' successfully imoprted as a module object!" % module)

    return pkg


def smart_import(module, module_pip_name=None):
    """smart_import(module, module_pip_name=None)
    Returns a module object.
    Try dynamically importing a module (passed as string).
    If no such module found, use pip to install module_pip_name then import it.
    If not specified, module_pip_name = module
    This makes our scripts independent of Anaconda. Only pip is required.

    Usage:
    module = smart_import(module_as_string)
    e.g.
    np = smart_import('numpy')
    Equivalent to:
    import numpy as np"""

    # Default module_pip_name is module
    if module_pip_name is None:
        module_pip_name = module

    try:
        return dynamic_import(module)
    except ImportError:
        print("ImportError: No module named '%s'" % module)
        print("Trying to use pip to install '%s'" % module)
        import pip
        pip.main(['install', module_pip_name])
        try:
            return dynamic_import(module)
        except:
            print(
                "SmartImportError: Module named '%s' cannot be installed by pip." % module)
