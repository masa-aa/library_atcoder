def float_to_int(f: str) -> tuple:
    """ str型の小数("31.415" etc)が与えられて(31415,3)みたいなのを返す. """
    if "." not in f:
        return int(f), 0
    return int(f.replace(".", "")), len(f) - f.index(".") - 1
