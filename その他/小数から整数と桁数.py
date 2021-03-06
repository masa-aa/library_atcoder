def float2int(FLOAT: str) -> tuple:
    """ str型の小数("31.415" etc)が与えられて(31415,3)みたいなのを返す. """
    if "." not in FLOAT:
        return int(FLOAT), 0
    return int(FLOAT.replace(".", "")), len(FLOAT) - FLOAT.index(".") - 1
