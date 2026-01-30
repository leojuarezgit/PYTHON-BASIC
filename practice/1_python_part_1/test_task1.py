import pytest
from task1 import delete_from_list


def test_examples():
    assert delete_from_list([1, 2, 3, 4, 3], 3) == [1, 2, 4]
    assert delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b') == ['a', 'c', 'd']
    assert delete_from_list([1, 2, 3], 'b') == [1, 2, 3]
    assert delete_from_list([], 'b') == []


def test_all_occurrences_removed():
    l = [2, 2, 2]
    assert delete_from_list(l, 2) == []
    assert l == []


def test_return_is_same_object_and_mutated():
    l = [1, 2, 3, 2]
    res = delete_from_list(l, 2)
    assert res is l
    assert res == [1, 3]


def test_no_match_keeps_list():
    l = [1, 2, 3]
    before = l.copy()
    res = delete_from_list(l, 4)
    assert res == before
    assert l == before


def test_delete_false_removes_zero_and_false():
    l = [0, False, 0.0, 1]
    res = delete_from_list(l, False)
    # bool False is equal to 0, so behavior depends on equality; ensure only equal elements removed
    assert res == [1]


def test_mixed_types_and_none():
    l = [None, 'None', 0, False]
    res = delete_from_list(l, None)
    assert res == ['None', 0, False]
