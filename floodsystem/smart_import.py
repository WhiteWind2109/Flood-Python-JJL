def execute(code):
    """Execute the Python3 code string dynamicly"""
    print(">>>", code)
    exec(code)


def smart_import(module):
    """Try importing a module (passed as string).
    If no such module found, use pip to install it."""
    try:
        from importlib import import_module
        import_module(module)
        print(">>> imoprt", module)
    except:
        print("ImportError: No module named '%s'" % module)
        print("Trying to use pip to install '%s'" % module)
        import pip
        code = "pip.main(['install', '{}'])".format(module)
        exec(code)
        try:
            import_module(module) 
            print(">>> imoprt", module)
        except:
            print(
                "SmartImportError: Module named '%s' cannot be installed by pip." % module)
