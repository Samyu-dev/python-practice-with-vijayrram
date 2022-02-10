# Python Practice

This repository contains a list of simple scripts developed as practice for the following:

* Understanding of Python.
* Understanding of Data Structures and Algorithms.
* Understanding of OOP concepts.

## Linting and Testing

Linting is an important part of the code development cycle. Linting enforces strict formatting rules which
enables the writing of code that is easy to read and understand for humans. The `pylint` module is
considered as a standard for linting Python code. The benchmark linting score is 9.0/10.0

Testing is another cornerstone of the code development cycle. Testing allows us to test
whether the code we have written works in a controlled environment. There are many types of testing.
Some of them are:

1. Unit Testing
2. Acceptance Testing
3. Integration Testing
4. Mutation Testing

Of these, unit testing is easy to implement as a sanity check for the developer. In Python, the
`pytest` and `coverage` modules are especially useful. The `coverage` module calculates the
percentage of the code that has been covered by the unit tests. The benchmark coverage is 85% for
every written module.

*Note*: Neither the linting score nor the coverage needs to be full for the written scripts to work.
They are metrics that determine how well the code is written and how well it behaves respectively.

Since linting and testing are common practices across all Python development, the requisite modules
can be installed globally. Therefore a virtual environment is not necessary for their installation.

```[bash]
python -m pip install pylint pytest pytest-mock coverage
```

After this one can check the linting score by running the following script:

```[bash]
python -m pylint <PATH/TO/PYTHON/SCRIPT>
```

One can run unit tests and the coverage by running the following script:

```[bash]
python -m coverage run -m py.test
python -m coverage report -m
```

## `linked_list.py`

A simple implementation of a Linked List used to understand

* Pointers/References
* Time/Space Complexity of methods.
* Inheritance/Polymorphism
