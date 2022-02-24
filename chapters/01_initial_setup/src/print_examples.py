from .code import qsort as sort_func

EXAMPLES = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [1, 1],
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
    [1, 2, 2],
    [1, 1, 2],
    [1, 1, 1],
]

def print_examples():
    for example in EXAMPLES:
        try:
            print(f"sort_func({str(example)}) = {str(sort_func(example))}")
        except:
            print(f"sort_func({str(example)}) => EXCEPTION RAISED")

if __name__ == "__main__":
    print_examples()
