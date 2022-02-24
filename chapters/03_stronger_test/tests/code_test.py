from collections import Counter

# I'm intentionally leaving some unused imports because there's some 
# commented-out code that uses these imports
from hypothesis import given, example, settings, Phase
import hypothesis.strategies as some
from src.code import qsort as sort_func

def test_very_simple_unit_test():
    assert sort_func([1]) == [1]

@given(some.lists(some.integers()))
def test_sort_doesnt_crash(lst):
    sort_func(lst)

@given(some.lists(some.integers()))
def test_sort_is_idempotent(lst):
    assert sort_func(sort_func(lst)) == sort_func(lst)

# @given(some.lists(some.integers()))
# def test_sort_has_same_elements(lst):
#     assert Counter(sort_func(lst)) == Counter(lst)


# @given(some.lists(some.integers()))
# def test_sort_is_ordered(lst):
#     sort_res = sort_func(lst)
#     for i in range(len(sort_res) - 1):
#         assert sort_res[i] <= sort_res[i+1]
