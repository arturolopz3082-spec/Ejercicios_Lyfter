def validate_numbers(base_func):
    def enhanced_func(*args, **kwargs):
        all_params = list(args) + list(kwargs.values())
        for param in all_params:
            if not isinstance(param, (int, float)):
                raise TypeError(
                    f"'{param}' no es un número (tipo: {type(param).__name__})"
                )
        return base_func(*args, **kwargs)
    return enhanced_func


@validate_numbers
def sumar(a, b):
    return a + b


print(sumar(3, 5))
print(sumar(3, "hola"))