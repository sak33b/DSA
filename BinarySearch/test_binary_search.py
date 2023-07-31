from binary_search import binary_search


def test_middle():
    assert binary_search([13, 11, 10, 7, 4, 3, 1], 7) == 3


def test_not_middle():
    assert binary_search([13, 11, 10, 7, 4, 3, 1, 0], 1) == 6


def test_first_element():
    assert binary_search([4, 2, 1, -1], 4) == 0


def test_last_element():
    assert binary_search([3, -1, -9, -127], -127) == 3


def test_only_element():
    assert binary_search([6], 6) == 0


def test_query_not_found():
    assert binary_search([9, 7, 5, 2, -9], 4) is None


def test_empty_list():
    assert binary_search([], 7) is None


def test_recurring_element():
    assert binary_search([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 3) == 7


def test_recurring_query():
    # Returns any occurrence if there is n query
    assert binary_search(
        [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 6) in range(2, 8)


def test_huge_list():
    assert binary_search(range(int(100e10), 0, -1), 2) == int(100e10) - 2
