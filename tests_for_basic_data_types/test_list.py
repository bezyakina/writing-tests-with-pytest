import pytest


@pytest.fixture(scope="function")
def return_list():
    """
    This function returns a list.
    """
    l = [1, 2, 3, 4, 5, 6, 7]
    return l


@pytest.fixture(scope="function")
def return_list_comprehension():
    """
    This function returns a list built with a list comprehension.
    """
    l = [x for x in range(7) if x % 2 == 0]
    return l


def test_list_type(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks that the object is a list.
    """
    assert type(return_list) is list


def test_list_append(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks that the number is added to the end of the list.
    """
    return_list.append(8)
    assert 8 in return_list


def test_list_extend(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks that the list of numbers is added to the end of the list.
    """
    return_list.extend([8, 9])
    assert 8 and 9 in return_list


def test_list_insert(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks the update of numbers by index in the list.
    """
    return_list[0] = "One"
    return_list.insert(1, "Two")
    assert return_list[0] == "One"
    assert return_list[1] == "Two"


def test_list_len(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks the length of the list.
    """
    assert len(return_list) == 7


def test_list_del(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks whether the list is deleted.
    """
    del return_list
    with pytest.raises(UnboundLocalError):
        assert return_list


def test_list_comprehension(
    return_list_comprehension,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks the creation of a list with list comprehension.
    """
    assert return_list_comprehension == [0, 2, 4, 6]


def test_list_slice(
    return_list_comprehension,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks whether the list is split into slices.
    """
    assert return_list_comprehension[:2] == [0, 2]
    assert return_list_comprehension[2:] == [4, 6]
    assert return_list_comprehension[1:3] == [2, 4]


def test_list_iterate(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks the creation of a new list by iterating the original list.
    """
    l = []
    for i in return_list:
        l.append(i)
    assert l == return_list


def test_list_copy_first(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks whether the list is copied.
    """
    l = return_list.copy()
    l.extend("+")
    assert "+" not in return_list
    assert "+" in l


def test_list_copy_second(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks whether the list is copied.
    """
    l = return_list[:]
    l.extend("+")
    assert "+" not in return_list
    assert "+" in l


def test_list_reverse_first(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks the reverse of the list.
    """
    return_list.reverse()
    assert return_list == [7, 6, 5, 4, 3, 2, 1]


def test_list_reverse_second(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks the reverse of the list.
    """
    l = reversed(return_list)
    assert list(l) == [7, 6, 5, 4, 3, 2, 1]


def test_list_reverse_third(
    return_list,
    function_fixture,
    class_fixture,
    module_fixture,
    session_fixture,
):
    """
    This test checks the reverse of the list.
    """
    l = return_list[::-1]
    assert list(l) == [7, 6, 5, 4, 3, 2, 1]
