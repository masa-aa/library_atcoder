# str型の小数(31.415 etc)が与えられて(31415,3)みたいなのを返す.

def get_int(f):
    return int(f.replace(".","")),len(f)-f.index(".")-1