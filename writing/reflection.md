# Reflection by Add Your Name Here

## Using a fenced code block, please display two correct outputs from running your program

TODO: Please provide two fenced code blocks demonstrating different runs of the program.

## Using a fenced code block, please display the passing output from running the tests with `poetry run pytest -v`

TODO: Please provide the output from running your program.

## What is the purpose of the following test case for the `transform` module?

```
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
```

TODO: Please provide a detailed response that describes the purpose of the source code.

## What is the purpose of the following source code in the `main` function?

```
population_dictionary = transform.transform_string_to_dictionary(data_text)
population_at_year = population_dictionary[year]
```

TODO: Please provide a detailed response that describes the purpose of the source code.

## What was the greatest technical challenge that you faced and how did you overcome it?

TODO: Please provide a response to this question.

## After completing this assignment, what is one task that you want to practice more? Why?

TODO: Please provide a response to this question.

## Although it is not required, you may provide any additional insights about this assignment

At your option, please provide additional insights about this assignment.
