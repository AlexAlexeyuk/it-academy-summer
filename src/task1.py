""" Create a runner.

runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import functions


def runner(*args):
    if not args:
        funcs_all = [funcs for funcs in dir(functions) if
                     not funcs.startswith('__') or not funcs.endswith("__") and callable(funcs)]
    else:
        funcs_all = [*args]

    for func in funcs_all:
        try:
            func = getattr(functions, func)
            if func:
                return func()
        except AttributeError:
            print('There is not that func', func)


runner()
runner('dct_')
runner('counter_')
runner('dct_', 'counter_')
