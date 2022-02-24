from .code import qsort as sort_func

EXAMPLES = [
    [],
    [1],
]

def print_examples():
    for example in EXAMPLES:
        try:
            print(f"sort_func({str(example)}) = {str(sort_func(example))}")
        except:
            print(f"sort_func({str(example)}) => EXCEPTION RAISED")

if __name__ == "__main__":
    print_examples()
