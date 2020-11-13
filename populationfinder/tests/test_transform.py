"""Ensure that the data transformation works correctly."""

from populationfinder import transform


def test_transform_empty_text_list_to_empty_dictionary():
    """Ensure that an empty list of textual numbers transforms correctly."""
    data_list_string = ""
    population_dictionary = transform.transform_string_to_dictionary(data_list_string)
    assert population_dictionary == {}


def test_transform_small_text_list_to_dictionary_same_last():
    """Ensure that a small list of textual numbers transforms correctly."""
    data_list_string = """1970-01-0,10
1970-01-0,5
1970-01-0,10
1970-01-0,5
1970-01-0,100"""
    population_dictionary = transform.transform_string_to_dictionary(data_list_string)
    assert population_dictionary != {}
    assert population_dictionary["1970-01-0"] == 100.0


def test_transform_small_text_list_to_dictionary_different_last():
    """Ensure that a small list of textual numbers transforms correctly."""
    data_list_string = """1970-01-0,10
1971-01-0,5
1972-01-0,10
1973-01-0,5
1974-01-0,100"""
    population_dictionary = transform.transform_string_to_dictionary(data_list_string)
    assert population_dictionary != {}
    assert population_dictionary["1970-01-0"] == 10.0
    assert population_dictionary["1974-01-0"] == 100.0
