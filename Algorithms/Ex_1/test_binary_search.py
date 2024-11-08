from binary_search import binary_search


def test_binary_search():
    # Test cases where target is present
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

    # Test cases where target is absent
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 0) == -1

    # Test edge cases
    assert binary_search([], 3) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1], 0) == -1
