"""Transform the data."""

from typing import Dict

# Reference for the data set:
# https://fred.stlouisfed.org/series/PACRAW0POP

# Sample of the data set:

# 1970-01-01,81.342
# 1971-01-01,83.300
# 1972-01-01,84.700
# 1973-01-01,85.500
# 1974-01-01,86.100
# 1975-01-01,87.000
# 1976-01-01,87.600
# 1977-01-01,87.600
# 1978-01-01,88.000
# 1979-01-01,88.100
# 1980-01-01,88.869


def transform_string_to_dictionary(data_text: str) -> Dict[str, float]:
    """Transform a string of (date, float) values to a list of floats."""
    # TODO: create an empty population dictionary
    # TODO: iterate through each line of the data set
        # TODO: extract the ordered pair on this line
        # the ordered pair has the format:
        # (Date, population count in thousands of persons)
        # TODO: extract the dat and store it as a string
        # TODO: convert the population count to a float and store it
        # TODO: add the new key-value pair to the dictionary where
        # the key is the date and the population is the value
    # TODO: return the population dictionary
