def arrayExtend(f):
    def ap_xs(xs):    
        return tuple(f(xs[i:]) for i in range(len(xs)))
    return ap_xs

# print(arrayExtend(lambda x: len(x))([1, 2, 3]))
