def  apply_all_func(int_list, *functions):
    return {f.__name__: f(int_list) for f in functions}


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))