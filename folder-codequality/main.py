from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_op(n):
    return n * 499500

def slow_func(lst):
    return [expensive_op(i) for i in range(len(lst))]

def main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")

if __name__ == "__main__":
    main()
