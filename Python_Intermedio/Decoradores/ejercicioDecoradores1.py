import time

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        print(f"Parámetros: {args}, kwargs: {kwargs}")
        start_time = time.time()
        result = base_fn(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Tiempo de cocción: {elapsed:.4f} segundos")
        print(f"Return: {result}")
        return result
    return enhanced_fn


@timer_dec
def brew_tea(tea_type, sleep_time):
    print(f"Brewing {tea_type} tea ...")
    time.sleep(sleep_time)
    return f"{tea_type} tea ready"


@timer_dec
def brew_coffee():
    print("Brewing coffee...")
    time.sleep(2)
    return "Coffee is ready!"


brew_tea("green", 3)
brew_coffee()