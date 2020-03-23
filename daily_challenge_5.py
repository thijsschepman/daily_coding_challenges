import inspect


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def get_element(a, b):
    outer_frame = inspect.getouterframes(inspect.currentframe())[2][3]

    if outer_frame is "car":
        return a
    elif outer_frame is "cdr":
        return b
    else:
        return "HELP, THIS SHOULD NOT BE HAPPENING!!!"


def car(pair):
    return pair(get_element)


def cdr(pair):
    return pair(get_element)
