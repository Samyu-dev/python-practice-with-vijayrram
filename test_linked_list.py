"""Script used by the pytest module to run and validate the code written in linkedlist_prac.py"""

import typing

import pytest

from linked_list import LinkedList


def test_should_instantiate_empty_linked_list():
    """Tests whether an empty linked list can be instantiated."""

    linked_list = LinkedList()

    assert linked_list.head is None


def __make_linked_list(*args: typing.Any) -> LinkedList:
    linked_list = LinkedList()

    for value in args:
        linked_list.append(value)

    return linked_list


@pytest.mark.parametrize("linked_list, value", [
    (__make_linked_list(), 1),
    (__make_linked_list(1), 2),
    (__make_linked_list(1, 2), 3),
])
def test_should_append_given_value_to_given_linked_list(linked_list: LinkedList, value: typing.Any):
    """Checks if you can append values to linked lists"""

    linked_list.append(value)

    assert linked_list.head is not None

    curr = linked_list.head
    while curr.next is not None:
        curr = curr.next

    assert curr.data == value
    assert curr.next is None


@pytest.mark.parametrize("linked_list, value", [
    (__make_linked_list(), 'None'),
    (__make_linked_list(1), "(1)->X"),
    (__make_linked_list(1, 2), "(1)->(2)->X"),
])
def test_should_print_given_linked_list(linked_list: LinkedList, value: str):
    """Checks if you can append values to linked lists"""

    assert str(linked_list) == value
