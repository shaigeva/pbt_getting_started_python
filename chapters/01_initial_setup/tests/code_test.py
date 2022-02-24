from hypothesis import given
import hypothesis.strategies as some
from src.code import qsort as sort_func

def test_very_simple_unit_test():
    assert sort_func([1]) == [1]

@given(some.lists(some.integers()))
def test_sort_doesnt_crash(lst):
    sort_func(lst)
