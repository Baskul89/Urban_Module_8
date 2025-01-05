def is_prime(f):
    def wrap(x, y, z):
        res = f(x, y, z)
        for i in range(2, res):
            if res % i == 0:
                return "Составное"
        return "Простое"

    return wrap

@is_prime
def sum_three(x, y, z):
    return x + y + z

result = sum_three(2, 3, 6)
print(result)

